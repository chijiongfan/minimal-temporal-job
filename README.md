<PASTE THE README CONTENT HERE>
System Design
Client
  ↓
FastAPI API
  ↓
Temporal Server
  ↓
Python Worker
  ↓
Activities (business logic)

Project Structure
app/        → API endpoints (start/query jobs)
worker/     → Temporal workflows & activities
docker/     → Local Temporal infrastructure

Examples Use Case
POST /jobs
→ returns job_id

GET /jobs/{job_id}
→ returns job status and result

Example Result
{
  "status": "COMPLETED",
  "result": 10
}

🖥️ Observability

Temporal UI available at http://localhost:8080

View workflow history, retries, and failures in real time