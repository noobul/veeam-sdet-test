import sched
import time

# Define the function to be scheduled
def my_func():
    print("Hello, World!")

# Create a scheduler object
scheduler = sched.scheduler(time.time, time.sleep)

# Define the time interval for running the function
interval = 5 # Run the function every 5 seconds

# Schedule the function to run periodically
def schedule_func(scheduler, interval):
    scheduler.enter(interval, 1, schedule_func, argument=(scheduler, interval))
    my_func()

# Start the scheduler
scheduler.enter(0, 1, schedule_func, argument=(scheduler, interval))
scheduler.run()
