from tools.appointment_tools import (
    get_all_appointments
)

def generate_reminders():

    appointments = get_all_appointments()

    reminders = []

    for appointment in appointments:

        if appointment["status"] == "BOOKED":

            reminders.append(
                {
                    "patient": appointment["patient"],
                    "message":
                        f"Hello {appointment['patient']}, "
                        f"this is a reminder for your "
                        f"appointment with "
                        f"{appointment['doctor']} "
                        f"at {appointment['slot']}."
                }
            )

    return reminders