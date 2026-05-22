# 2Care AI Voice Agent

## Features

- Appointment booking
- Appointment cancellation
- Appointment rescheduling
- Conflict resolution
- Patient memory
- English, Hindi, Tamil support
- Voice interaction
- Reminder campaigns

## Tech Stack

Frontend:
- Next.js
- TypeScript

Backend:
- FastAPI
- SQLite
- SQLAlchemy

## Run Backend

```bash
uvicorn app:app --reload
```

## Run Frontend

```bash
npm run dev
```

## Memory Design

Session Memory:
conversation_memory.py

Long-Term Memory:
patient_memory.py

## Architecture

See docs/architecture.png