from database import SessionLocal
from models import Appointment


# -----------------------------------
# BOOK APPOINTMENT
# -----------------------------------

def book_appointment(patient, doctor, slot):

    db = SessionLocal()

    existing = db.query(Appointment).filter(
        Appointment.doctor == doctor,
        Appointment.slot == slot,
        Appointment.status == "BOOKED"
    ).first()

    if existing:

        return {
            "success": False,
            "message": "Slot unavailable",
            "alternatives": [
                "11AM",
                "12PM",
                "2PM"
            ]
        }

    appointment = Appointment(
        patient=patient,
        doctor=doctor,
        slot=slot,
        status="BOOKED"
    )

    db.add(appointment)
    db.commit()

    return {
        "success": True,
        "message": "Appointment booked successfully"
    }


# -----------------------------------
# CANCEL APPOINTMENT
# -----------------------------------

def cancel_appointment(
    doctor,
    slot
):

    db = SessionLocal()

    appointment = db.query(
        Appointment
    ).filter(
        Appointment.doctor == doctor,
        Appointment.slot == slot,
        Appointment.status == "BOOKED"
    ).first()

    if not appointment:

        return {
            "success": False,
            "message": "Appointment not found"
        }

    appointment.status = "CANCELLED"

    db.commit()

    return {
        "success": True,
        "message": "Appointment cancelled successfully"
    }


# -----------------------------------
# RESCHEDULE APPOINTMENT
# -----------------------------------

def reschedule_appointment(
    doctor,
    old_slot,
    new_slot
):

    db = SessionLocal()

    appointment = db.query(
        Appointment
    ).filter(
        Appointment.doctor == doctor,
        Appointment.slot == old_slot,
        Appointment.status == "BOOKED"
    ).first()

    if not appointment:

        return {
            "success": False,
            "message": "Original appointment not found"
        }

    conflict = db.query(
        Appointment
    ).filter(
        Appointment.doctor == doctor,
        Appointment.slot == new_slot,
        Appointment.status == "BOOKED"
    ).first()

    if conflict:

        return {
            "success": False,
            "message": "New slot unavailable"
        }

    appointment.slot = new_slot

    db.commit()

    return {
        "success": True,
        "message": f"Appointment moved to {new_slot}"
    }


# -----------------------------------
# GET ALL APPOINTMENTS
# -----------------------------------

def get_all_appointments():

    db = SessionLocal()

    appointments = db.query(
        Appointment
    ).all()

    result = []

    for a in appointments:

        result.append(
            {
                "id": a.id,
                "patient": a.patient,
                "doctor": a.doctor,
                "slot": a.slot,
                "status": a.status
            }
        )

    return result