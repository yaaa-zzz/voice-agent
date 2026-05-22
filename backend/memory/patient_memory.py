from database import SessionLocal
from models import Patient


def save_patient_memory(
    name,
    language,
    doctor
):

    db = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.name == name
    ).first()

    if patient:

        patient.preferred_language = language
        patient.preferred_doctor = doctor

    else:

        patient = Patient(
            name=name,
            preferred_language=language,
            preferred_doctor=doctor
        )

        db.add(patient)

    db.commit()

    return patient


def get_patient_memory(name):

    db = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.name == name
    ).first()

    return patient