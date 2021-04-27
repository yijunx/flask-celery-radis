from celery import Celery


# use //redis because this is docker compose network
app = Celery('tasks', broker='redis://redis')

@app.task
def add(x, y):
    return x + y