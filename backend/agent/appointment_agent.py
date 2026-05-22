from tools.appointment_tools import (
    book_appointment,
    cancel_appointment,
    reschedule_appointment
)

from memory.patient_memory import (
    get_patient_memory,
    save_patient_memory
)

from utils.language_detector import detect_language


def ask_agent(user_message):

    language = detect_language(user_message)

    patient_name = "Mohamed"

    patient_memory = get_patient_memory(
        patient_name
    )

    text = user_message.lower()

    # --------------------------------
    # CANCEL
    # --------------------------------

    if "cancel" in text:

        result = cancel_appointment(
            "Dr Kumar",
            "10AM"
        )

        return result["message"]

    # --------------------------------
    # RESCHEDULE
    # --------------------------------

    if "reschedule" in text:

        result = reschedule_appointment(
            "Dr Kumar",
            "10AM",
            "11AM"
        )

        return result["message"]

    # --------------------------------
    # BOOK
    # --------------------------------

    if (
        "book" in text
        or "appointment" in text
        or "अपॉइंटमेंट" in user_message
        or "அப்பாயின்ட்மென்ட்" in user_message
    ):

        doctor = "Dr Kumar"

        if "11am" in text:
            slot = "11AM"

        elif "12pm" in text:
            slot = "12PM"

        else:
            slot = "10AM"

        save_patient_memory(
            patient_name,
            language,
            doctor
        )

        result = book_appointment(
            patient_name,
            doctor,
            slot
        )

        if result["success"]:

            if language == "Hindi":

                return (
                    f"{doctor} के साथ "
                    f"{slot} पर अपॉइंटमेंट बुक हो गया है।"
                )

            elif language == "Tamil":

                return (
                    f"{doctor} உடன் "
                    f"{slot} நேரத்திற்கு "
                    f"அப்பாயின்ட்மென்ட் பதிவு செய்யப்பட்டது."
                )

            return (
                f"Appointment booked successfully "
                f"with {doctor} at {slot}."
            )

        else:

            alternatives = ", ".join(
                result["alternatives"]
            )

            return (
                f"Requested slot unavailable. "
                f"Available slots: {alternatives}"
            )

    # --------------------------------
    # MEMORY
    # --------------------------------

    if patient_memory:

        return (
            f"Welcome back. "
            f"Your preferred doctor is "
            f"{patient_memory.preferred_doctor}."
        )

    # --------------------------------
    # DEFAULT
    # --------------------------------

    return (
        "I can help with booking, "
        "cancelling or rescheduling appointments."
    )