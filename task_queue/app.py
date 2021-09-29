from flask import Flask, request
from redis import Redis
#from celery import Celery
from rq import Queue
from utils import simulated_task

app = Flask(__name__)

r = Redis()
q = Queue(connection=r)


@app.route("/task")
def add_task_to_queue():

    n = request.args.get("n")

    if n:
        job = q.enqueue(simulated_task, n)
        
        return f'{job.id} added to queue at {job.enqueued_at} ------ {len(q)} tasks in queue'
    return "No task to add"



if __name__ == "__main__":
    app.run()