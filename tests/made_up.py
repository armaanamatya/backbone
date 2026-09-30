"""Builds the claims of made-up documents, so that one rule can be tried at a time.

The patient, the clinic, the numbers and the times here are invented. Nothing
comes from the supplied documents.
"""

from __future__ import annotations

import hashlib

PATIENT = "NF-P001"
DAY = "2025-03-04"  # a Tuesday


class Record:
    def __init__(self, patient: str = PATIENT):
        self.patient = patient
        self.claims: list[dict] = []
        self.sections: dict = {}

    def document(self, name, kind="clinical_note", signed=f"{DAY}T17:00", copy_signed=None, is_copy=False, dates=()):
        """One document of one section. `signed` is when it was signed, or
        None. For a copy, `copy_signed` is when its original was signed."""
        doc_hash = hashlib.sha256(f"{self.patient}/{name}".encode()).hexdigest()
        section = {
            "id": 1,
            "kind": kind,
            "signature": "signed" if signed and not is_copy else ("unsigned" if is_copy else "not_stated"),
            "signed_by": "Dana Ortiz" if signed and not is_copy else None,
            "signed_date": signed[:10] if signed and not is_copy else None,
            "signed_time": signed[11:] if signed and not is_copy else None,
            "is_copy": is_copy,
            "original_signed_by": "Dana Ortiz" if copy_signed else None,
            "original_signed_date": copy_signed[:10] if copy_signed else None,
            "original_signed_time": copy_signed[11:] if copy_signed else None,
            "dates": [{"kind": kind_, "date": date, "quote": date, "line": 1} for kind_, date in dates],
        }
        self.sections[(doc_hash, 1)] = section
        return Document(self, doc_hash, name)

    def shuffled(self, seed: int) -> list[dict]:
        import random

        claims = list(self.claims)
        random.Random(seed).shuffle(claims)
        return claims


class Document:
    def __init__(self, record: Record, doc_hash: str, name: str):
        self.record = record
        self.doc_hash = doc_hash
        self.name = name
        self.contacts: dict[str, dict] = {}
        self.count = 0

    def _add(self, kind, value, ref="c1", label=None):
        self.count += 1
        about = self.contacts.get(ref, {})
        self.record.claims.append(
            {
                "claim_id": f"{self.doc_hash[:12]}:{self.count:03d}",
                "doc_hash": self.doc_hash,
                "document": self.name,
                "section": 1,
                "patient_key": self.record.patient,
                "type": kind,
                "contact_ref": ref,
                "encounter_id": about.get("encounter_id"),
                "appointment_id": about.get("appointment_id"),
                "service_date": about.get("service_date"),
                "service_class": about.get("service_class"),
                "service_as_written": about.get("service_as_written"),
                "value": value,
                "time_label": label,
                "quote": "made up",
                "line": 1,
                "quote_status": "verified",
                "valid": 1,
            }
        )
        return self

    def contact(self, encounter=None, date=DAY, service="group_therapy", ref="c1", appointment=None, written="as written"):
        self.contacts[ref] = {
            "encounter_id": encounter,
            "appointment_id": appointment,
            "service_date": date,
            "service_class": service,
            "service_as_written": written,
        }
        return self._add("contact", {"ref": ref}, ref)

    def time(self, what, start=None, end=None, label="actual", position="body", ref="c1", detail=None):
        value = {"what": what, "start": start, "end": end, "label": label, "position": position, "detail": detail}
        return self._add("time", value, ref, label)

    def scheduled(self, start, end, ref="c1"):
        return self.time("contact_interval", start, end, "scheduled", "header", ref)

    def arrived(self, start, ref="c1", label="actual"):
        return self.time("patient_arrival", start, None, label, "table", ref)

    def left(self, end, ref="c1", label="actual"):
        return self.time("patient_departure", None, end, label, "table", ref)

    def present(self, start, end, ref="c1", label="actual", position="header"):
        return self.time("patient_present", start, end, label, position, ref)

    def no_therapy(self, start, end, ref="c1", detail="break"):
        return self.time("no_therapy_interval", start, end, "actual", "body", ref, detail)

    def attendance(self, status, ref="c1", **more):
        return self._add("attendance", {"status": status, "status_as_written": status, **more}, ref)

    def participant(self, role, presence="not_stated", name=None, ref="c1"):
        return self._add("participant", {"role": role, "presence": presence, "name": name}, ref)

    def minutes(self, minutes, of="patient_present", ref="c1"):
        return self._add("stated_minutes", {"minutes": minutes, "of": of}, ref)

    def correction(self, field, old, new, ref="c1"):
        return self._add("correction", {"field": field, "old_value": old, "new_value": new, "reason": "made up"}, ref)

    def charge(self, number="CH-1", ref="c1"):
        return self._add("charge", {"charge_id": number, "description": "Group session", "quantity": 1}, ref)

    def statement(self, says, ref="c1"):
        return self._add("statement", {"says": says}, ref)

    def modality(self, modality, ref="c1"):
        return self._add("modality", {"modality": modality}, ref)

    def score(self, score, date, relation="completion", instrument="GAD-7", form=None, time=None, item=None):
        value = {
            "instrument": instrument,
            "score": score,
            "item_number": item,
            "completed_date": date,
            "completed_time": time,
            "form_id": form,
            "relation": relation,
        }
        return self._add("score", value, None)

    def rule(self, rule, **value):
        return self._add("plan_rule", {"rule": rule, **value}, None)

    def plan(self, start="2025-03-03", end="2025-03-28", days=2, minutes=100, counted=("group_therapy", "individual_therapy"), excluded=("medication_management",)):
        self.rule("episode_period", start_date=start, end_date=end)
        self.rule("requirement", measure="therapy_days", minimum=days, period="week")
        self.rule("requirement", measure="minutes", minimum=minutes, period="week")
        self.rule("week_definition", week_starts_on="monday")
        self.rule("therapy_day_definition", service_classes=list(counted), patient_must_be_present=True)
        self.rule("counted_service", service_classes=list(counted), patient_must_be_present=True)
        self.rule("excluded_service", service_classes=list(excluded))
        return self
