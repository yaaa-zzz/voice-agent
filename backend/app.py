from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

from tools.appointment_tools import (
    book_appointment,
    get_all_appointments
)

from agent.appointment_agent import ask_agent

from campaigns.reminder_service import (
    generate_reminders
)

app = FastAPI(
    title="2Care AI Voice Agent",
    description="Multilingual Clinical Appointment Booking Assistant",
    version="1.0.0"
)

# ---------------------------------------
# CORS
# ---------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------
# Request Models
# ---------------------------------------

class AppointmentRequest(BaseModel):
    patient: str
    doctor: str
    slot: str


class ChatRequest(BaseModel):
    message: str


# ---------------------------------------
# HOME
# ---------------------------------------

@app.get("/")
def home():
    return {
        "message": "2Care AI Voice Agent Running"
    }


# ---------------------------------------
# HEALTH CHECK
# ---------------------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# ---------------------------------------
# BOOK APPOINTMENT
# ---------------------------------------

@app.post("/book")
def book(request: AppointmentRequest):

    result = book_appointment(
        patient=request.patient,
        doctor=request.doctor,
        slot=request.slot
    )

    return result


# ---------------------------------------
# CHAT WITH AGENT
# ---------------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    start_time = time.time()

    try:

        reply = ask_agent(
            request.message
        )

        latency = round(
            (time.time() - start_time) * 1000,
            2
        )

        return {
            "success": True,
            "reply": reply,
            "latency_ms": latency
        }

    except Exception as e:

        latency = round(
            (time.time() - start_time) * 1000,
            2
        )

        return {
            "success": False,
            "error": str(e),
            "latency_ms": latency
        }


# ---------------------------------------
# VIEW ALL APPOINTMENTS
# ---------------------------------------

@app.get("/appointments")
def appointments():

    return get_all_appointments()


# ---------------------------------------
# OUTBOUND REMINDER CAMPAIGNS
# ---------------------------------------

@app.get("/campaigns/reminders")
def reminders():

    return generate_reminders()