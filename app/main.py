import uvicorn
from fastapi import FastAPI
from tasks import send_email

app = FastAPI()


@app.post("/send-mail")
def send_mail_endpoint(email: str):
    task = send_email.dealy(email)
    return {
        "message": "Zadanie przyjęte",
        "task_id": task.id
    }


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
