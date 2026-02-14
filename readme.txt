unzip rabbitmq_celery_fastapi.zip
cd rabbitmq_celery_project
docker compose up --build - uruchomienie dockera


curl -X POST "http://localhost:8000/send-email?email=test@example.com"

	•	API: http://localhost:8000
	•	RabbitMQ UI: http://localhost:15672
login: guest / guest

sprawdzanie statusu:
curl http://localhost:8000/tasks/15fe9501-6633-403e-831b-ef9ae24cfff4

(.venv) radoslawjaniak@mac rabbitmq_celery_fastapi % curl -X POST "http://localhost:8000/send-email?email=test@example.com"

{"message":"Zadanie przyjęte","task_id":"15fe9501-6633-403e-831b-ef9ae24cfff4"}%                                                                            (.venv) radoslawjaniak@mac rabbitmq_celery_fastapi % curl http://localhost:8000/tasks/15fe9501-6633-403e-831b-ef9ae24cfff4
{"task_id":"15fe9501-6633-403e-831b-ef9ae24cfff4","state":"PROGRESS","info":{"step":"Wysyłanie treści wiadomości","progress":70}}%                          (.venv) radoslawjaniak@mac rabbitmq_celery_fastapi % curl http://localhost:8000/tasks/15fe9501-6633-403e-831b-ef9ae24cfff4
{"task_id":"15fe9501-6633-403e-831b-ef9ae24cfff4","state":"SUCCESS","info":{"status":"ok","email":"test@example.com","progress":100},"result":{"status":"ok","email":"test@example.com","progress":100}}%