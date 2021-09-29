"""
Moved to separate file due to issue with rq worker:
'ValueError: Functions from the _main_ module cannot be processed by workers'
"""
import time

def simulated_task(n):
    simulated_task_delay = 3 

    print("Task running")
    print(f'Delay: {simulated_task_delay} seconds')

    time.sleep(simulated_task_delay)

    print(n)
    print("Task complete")

    return n
