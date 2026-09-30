"""The shape of what the model returns for one document (the capture list, R-21).

The same schema is given to the `claude` tool, which checks the result, and is
applied again here by `validate`, so a malformed result is caught twice.

Only the parts of JSON Schema used below are supported by `validate`.
"""

from __future__ import annotations

import re

SERVICE_CLASSES = [
    "individual_therapy",
    "group_therapy",
    "family_therapy",
    "medication_management",
    "care_coordination",
    "questionnaire_review",
    "scheduling_contact",
    "collateral_contact",
    "other",
]

SECTION_KINDS = [
    "plan",
    "clinical_note",
    "attendance_record",
    "schedule_export",
    "correction",
    "draft_note",
    "billing_extract",
    "questionnaire_review",
    "import_receipt",
    "authorization",
    "scheduling_log",
    "cancellation_notice",
    "platform_export",
    "cover_sheet",
    "other",
]

DATE_KINDS = [
    "service",
    "signed",
    "received",
    "exported_or_prepared",
    "entered",
    "created",
    "posted",
    "reviewed",
    "completed",
    "period_start",
    "period_end",
    "other",
]

TIME_WHAT = [
    "contact_interval",
    "patient_present",
    "patient_arrival",
    "patient_departure",
    "no_therapy_interval",
    "patient_absent_interval",
    "connection",
    "other",
]

TIME_LABELS = ["scheduled", "actual", "not_labelled"]
POSITIONS = ["header", "body", "table"]

ATTENDANCE = [
    "attended",
    "attended_part",
    "absent",
    "no_show",
    "cancelled_by_patient",
    "cancelled_by_clinic",
    "completed",
    "other",
]

ROLES = ["patient", "clinician", "family_or_partner", "outside_professional", "staff", "other"]
PRESENCE = ["present", "present_part", "absent", "not_stated"]
MODALITIES = ["in_person", "video", "telephone", "message", "other"]
MINUTES_OF = ["patient_present", "contact_total", "without_patient", "other"]
CORRECTION_FIELDS = [
    "arrival",
    "departure",
    "start",
    "end",
    "status",
    "minutes",
    "score",
    "date",
    "other",
]
SCORE_RELATIONS = ["completion", "copy", "mention"]
SPEAKERS = ["patient", "clinician", "family_or_partner", "outside_professional", "staff", "other"]
TOPICS = [
    "mood",
    "anxiety",
    "sleep",
    "safety",
    "functioning",
    "progress",
    "reason_for_contact",
    "medication",
    "other",
]
PLAN_RULES = [
    "episode_period",
    "requirement",
    "week_definition",
    "therapy_day_definition",
    "counted_service",
    "excluded_service",
    "clinical_goal",
    "other",
]
MEASURES = ["therapy_days", "minutes", "sessions"]
PERIODS = ["week", "month", "episode"]
WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
STATEMENTS = [
    "no_therapy_provided",
    "no_patient_contact",
    "not_a_visit",
    "no_clinical_service",
    "no_new_signature",
    "no_new_assessment",
    "not_an_attendance_record",
    "is_copy_or_resend",
    "is_draft_or_unsigned",
    "made_before_the_service",
    "prepared_from_signed_record",
    "same_contact_continued",
    "separate_contact",
    "other",
]

# The lists of items the model returns. Each becomes claims of one type.
CLAIM_LISTS = {
    "contacts": "contact",
    "modalities": "modality",
    "times": "time",
    "attendance": "attendance",
    "participants": "participant",
    "stated_minutes": "stated_minutes",
    "corrections": "correction",
    "scores": "score",
    "observations": "observation",
    "plan_rules": "plan_rule",
    "charges": "charge",
    "statements": "statement",
}

DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}$"
TIME_PATTERN = r"^([01]\d|2[0-3]):[0-5]\d$"

STRING = {"type": "string"}
TEXT = {"type": ["string", "null"]}
INTEGER = {"type": "integer"}
NUMBER = {"type": ["number", "null"]}
DATE = {"type": ["string", "null"], "pattern": DATE_PATTERN}
TIME = {"type": ["string", "null"], "pattern": TIME_PATTERN}


def enum(values, nullable=False):
    if nullable:
        return {"enum": list(values) + [None]}
    return {"enum": list(values)}


def item(required: dict, optional: dict | None = None, *, contact=True, cited=True) -> dict:
    """One kind of item. Every item names its section and carries a quote and a line."""
    properties = {"section": INTEGER}
    needed = ["section"]
    if contact:
        properties["contact"] = TEXT
    properties.update(required)
    needed += list(required)
    properties.update(optional or {})
    if cited:
        properties["quote"] = STRING
        properties["line"] = INTEGER
        needed += ["quote", "line"]
    return {
        "type": "object",
        "properties": properties,
        "required": needed,
        "additionalProperties": False,
    }


def array(schema: dict) -> dict:
    return {"type": "array", "items": schema}


SECTION = {
    "type": "object",
    "properties": {
        "id": INTEGER,
        "heading": TEXT,
        "kind": enum(SECTION_KINDS),
        "kind_as_written": TEXT,
        "first_line": INTEGER,
        "last_line": INTEGER,
        "author_name": TEXT,
        "author_role": TEXT,
        "signature": enum(["signed", "unsigned", "not_stated"]),
        "signed_by": TEXT,
        "signed_date": DATE,
        "signed_time": TIME,
        "signature_line": {"type": ["integer", "null"]},
        "status_as_written": TEXT,
        "is_copy": {"type": "boolean"},
        "original_signed_by": TEXT,
        "original_signed_date": DATE,
        "original_signed_time": TIME,
        "dates": array(
            {
                "type": "object",
                "properties": {
                    "kind": enum(DATE_KINDS),
                    "date": DATE,
                    "time": TIME,
                    "quote": STRING,
                    "line": INTEGER,
                },
                "required": ["kind", "date", "quote", "line"],
                "additionalProperties": False,
            }
        ),
    },
    "required": ["id", "kind", "first_line", "last_line", "signature", "is_copy", "dates"],
    "additionalProperties": False,
}

READING_SCHEMA = {
    "type": "object",
    "properties": {
        "document": {
            "type": "object",
            "properties": {
                "declared_id": TEXT,
                "organization": TEXT,
                "patient_name": TEXT,
                "patient_dob": DATE,
                "patient_record_number": TEXT,
            },
            "required": ["declared_id", "patient_name", "patient_dob", "patient_record_number"],
            "additionalProperties": False,
        },
        "sections": array(SECTION),
        "contacts": array(
            item(
                {
                    "ref": STRING,
                    "encounter_id": TEXT,
                    "appointment_id": TEXT,
                    "service_date": DATE,
                    "service_as_written": TEXT,
                    "service_class": enum(SERVICE_CLASSES, nullable=True),
                },
                contact=False,
            )
        ),
        "modalities": array(item({"modality": enum(MODALITIES)})),
        "times": array(
            item(
                {
                    "what": enum(TIME_WHAT),
                    "start": TIME,
                    "end": TIME,
                    "label": enum(TIME_LABELS),
                    "position": enum(POSITIONS),
                },
                {"detail": TEXT},
            )
        ),
        "attendance": array(
            item(
                {"status": enum(ATTENDANCE), "status_as_written": STRING},
                {
                    "reason": TEXT,
                    "entry_signed_by": TEXT,
                    "entry_signed_date": DATE,
                    "entry_signed_time": TIME,
                    "entry_entered_by": TEXT,
                    "entry_entered_date": DATE,
                    "entry_entered_time": TIME,
                },
            )
        ),
        "participants": array(
            item(
                {"name": TEXT, "role": enum(ROLES), "presence": enum(PRESENCE)},
                {"role_as_written": TEXT},
            )
        ),
        "stated_minutes": array(item({"minutes": INTEGER, "of": enum(MINUTES_OF)})),
        "corrections": array(
            item(
                {
                    "field": enum(CORRECTION_FIELDS),
                    "old_value": TEXT,
                    "new_value": TEXT,
                },
                {"field_as_written": TEXT, "reason": TEXT},
            )
        ),
        "scores": array(
            item(
                {
                    "instrument": STRING,
                    "score": INTEGER,
                    "item_number": {"type": ["integer", "null"]},
                    "completed_date": DATE,
                    "relation": enum(SCORE_RELATIONS),
                },
                {"completed_time": TIME, "form_id": TEXT},
                contact=False,
            )
        ),
        "observations": array(
            item(
                {
                    "date": DATE,
                    "speaker": enum(SPEAKERS),
                    "topic": enum(TOPICS),
                    "summary": STRING,
                },
                {"speaker_name": TEXT},
            )
        ),
        "plan_rules": array(
            item(
                {"rule": enum(PLAN_RULES)},
                {
                    "start_date": DATE,
                    "end_date": DATE,
                    "measure": enum(MEASURES, nullable=True),
                    "minimum": NUMBER,
                    "period": enum(PERIODS, nullable=True),
                    "week_starts_on": enum(WEEKDAYS, nullable=True),
                    "service_classes": array(enum(SERVICE_CLASSES)),
                    "patient_must_be_present": {"type": ["boolean", "null"]},
                    "goal_number": {"type": ["integer", "null"]},
                    "text": TEXT,
                },
                contact=False,
            )
        ),
        "charges": array(
            item(
                {"charge_id": TEXT, "description": TEXT},
                {
                    "quantity": NUMBER,
                    "unit_as_written": TEXT,
                    "status_as_written": TEXT,
                    "posted_date": DATE,
                    "posted_time": TIME,
                },
            )
        ),
        "statements": array(item({"says": enum(STATEMENTS)})),
    },
    "required": ["document", "sections"] + list(CLAIM_LISTS),
    "additionalProperties": False,
}


def _type_ok(value, name: str) -> bool:
    if name == "null":
        return value is None
    if name == "string":
        return isinstance(value, str)
    if name == "boolean":
        return isinstance(value, bool)
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if name == "object":
        return isinstance(value, dict)
    if name == "array":
        return isinstance(value, list)
    raise ValueError(f"type not supported by the validator: {name}")


def validate(value, schema: dict = READING_SCHEMA, path: str = "result") -> list[str]:
    """Returns the ways `value` fails `schema`. An empty list means it fits."""
    errors: list[str] = []
    if "enum" in schema:
        if value not in schema["enum"]:
            errors.append(f"{path}: {value!r} is not one of {schema['enum']}")
        return errors
    if "type" in schema:
        names = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_ok(value, name) for name in names):
            errors.append(f"{path}: expected {' or '.join(names)}, got {type(value).__name__}")
            return errors
    if isinstance(value, str) and "pattern" in schema:
        if not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} does not match {schema['pattern']}")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            if name not in value:
                errors.append(f"{path}: missing {name!r}")
        for name, inner in value.items():
            if name in properties:
                errors.extend(validate(inner, properties[name], f"{path}.{name}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected {name!r}")
    if isinstance(value, list) and "items" in schema:
        for index, inner in enumerate(value):
            errors.extend(validate(inner, schema["items"], f"{path}[{index}]"))
    return errors
