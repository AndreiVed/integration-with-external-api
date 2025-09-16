from celery import Celery

from main import main

app = Celery(
    "tasks", backend="redis://redis:6379", broker="redis://redis:6379"
)


@app.task
def main_task():
    main()


if __name__ == "__main__":
    main_task.delay()
