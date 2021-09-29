# Redis-Task-Queue
Simple task queue with rq (celery later) to see how background tasks operate with Redis as a message broker.

## Setup
Ensure python 3.9 is installed.

Install requirements:
```bash
pip install -r requirements.txt
```

Or, access virtual environment:
```bash
pip install pipenv
pipenv shell
```

### Running the Server
In separate terminal windows, you must set up Redis (needs to be installed locally), run an rq worker, and run the flask server.
Linux/Mac:
```
redis-server
```

```
rq worker
```

```
cd task_queue
python app.py
```

## Making Requests
Go to the /task endpoint (http://127.0.0.1:5000/task). You should see that there are no tasks in the queue. Add to the URL your query: '?n=<whatever-you-want>' and hit enter. You should see it added to the queue, and in your flask terminal, the prints defined in the simulated_task method. You can either update n or just keep refreshing to keep adding tasks.

For example:
http://127.0.0.1:5000/task?n=hey should show something like:

567a103f-17bd-4618-905e-7a45dd2bc01f added to queue at 2021-09-29 03:18:57.394759 ------ 0 tasks in queue

You see zero, because the only task that was in the queue is being executed. Refresh the page and you'll have multiple tasks lined up.
