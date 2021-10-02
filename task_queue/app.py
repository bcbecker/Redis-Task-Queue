from flask import request, Blueprint
from redis import Redis
from rq import Queue

queue = Blueprint('queue', __name__)

r = Redis()
q = Queue(connection=r)


@queue.route("/task")
def add_task_to_queue():

    n = request.args.get('n')

    if n:
        #use import string as first arg
        job = q.enqueue('task_queue.tasks.simulated_task', n)
        
        return f'{job.id} added to queue at {job.enqueued_at} ------ {len(q)} tasks in queue'
    return "No task to add"
