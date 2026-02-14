import uvicorn
from fastapi import FastAPI

from app.celery_app import celery_app
from app.tasks import send_email

app = FastAPI()


@app.post("/send-email")
def send_mail_endpoint(email: str):
    task = send_email.delay(email)
    return {
        "message": "Zadanie przyjęte",
        "task_id": task.id
    }

@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    async_result = celery_app.AsyncResult(task_id)
    response = {
        "task_id": task_id,
        "state": async_result.state,
        "info": async_result.info,
    }

    # include result only when ready/success
    if async_result.ready():
        try:
            response["result"] = async_result.result
        except Exception as e:
            response["result_error"] = str(e)

    return response


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
