"""
Moved to separate file due to issue with rq worker:
'ValueError: Functions from the _main_ module cannot be processed by workers'
"""
import time

def simulated_task(n):
    simulated_task_delay = 2 

    print("Task running")
    print(f'Delay: {simulated_task_delay}')

    time.sleep(simulated_task_delay)

    print(len(n))
    print("Task complete")

    return len(n)
