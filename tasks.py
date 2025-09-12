from celery import Celery

from main import main

app = Celery("tasks", backend="redis://localhost", broker="redis://localhost")


@app.task
def main_task():
    main()

if __name__ == "__main__":
    main_task.delay()
