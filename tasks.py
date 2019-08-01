from celery import Celery

BROKER_URL = "redis://" + "253b5d509e87"

app = Celery('tasks', backend=BROKER_URL ,broker=BROKER_URL)

@app.task
def add(x,y):
	return x + y