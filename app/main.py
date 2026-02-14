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

# nie jest konieczne gdy uruchmmiamy w dockerze
# if __name__ == '__main__':
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
# {"task_id":"57fa9d2c-f9a7-414a-80b6-f0e9ff866e34","state":"PROGRESS","info":{"step":"Łączenie z serwerem SMTP","progress":30}}%                                 radoslawjaniak@mac ~ % curl http://localhost:8000/tasks/57fa9d2c-f9a7-414a-80b6-f0e9ff866e34
# {"task_id":"57fa9d2c-f9a7-414a-80b6-f0e9ff866e34","state":"SUCCESS","info":{"status":"ok","email":"test@example.com","progress":100},"result":{"status":"ok","email":"test@example.com","progress":100}}%                                       radoslawjaniak@mac ~ %