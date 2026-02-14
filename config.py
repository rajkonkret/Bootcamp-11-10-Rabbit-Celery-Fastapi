import os

RABBITMQ_URL = os.environ.get("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672//")
REDIS_URL = os.environ.get("REDIS_URL", "redis://redis:6379/0")
