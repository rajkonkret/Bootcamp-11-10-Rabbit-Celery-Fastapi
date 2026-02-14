import time
import requests
from datetime import datetime

API_BASE = "http://localhost:8000"

TASKS = []  # lista task_id


def send_email_via_api(email: str):
    resp = requests.post(
        f"{API_BASE}/send-email",
        params={"email": email},
        timeout=5,
    )
    resp.raise_for_status()
    data = resp.json()

    task_id = data["task_id"]
    TASKS.append(task_id)

    print(f"📤 {datetime.now()} API → wysłano maila | task_id={task_id}")


def check_statuses_via_api():
    print(f"\n🔍 {datetime.now()} SPRAWDZANIE STATUSÓW (API)")
    for task_id in TASKS:
        resp = requests.get(
            f"{API_BASE}/tasks/{task_id}",
            timeout=5,
        )
        resp.raise_for_status()
        data = resp.json()

        print(
            f"  • {task_id[:8]} | "
            f"state={data.get('state')} | "
            f"data={data.get('meta') or data.get('result')}"
        )
    print("-" * 60)


if __name__ == "__main__":
    email = "test@example.com"
    last_status_check = time.time()

    try:
        while True:
            # 1️⃣ co 1 sekundę wysyłamy request do API
            send_email_via_api(email)
            time.sleep(10)

            # 2️⃣ co 30 sekund sprawdzamy statusy
            if time.time() - last_status_check >= 30:
                check_statuses_via_api()
                last_status_check = time.time()

    except KeyboardInterrupt:
        print("\n🛑 Zatrzymano klienta API")
