from celery import Celery

#defini string de conexão com redis
BROKER_URL = "redis://" + "253b5d509e87"

#instancia objeto Celery com bocker e backend
app = Celery('tasks', backend=BROKER_URL ,broker=BROKER_URL)

#defini função para teste
@app.task
def add(x,y):
	return x + y