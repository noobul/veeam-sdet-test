import sched
import time

class SchedulerLogic:
    def __init__(self, sync_interval, method_to_delay, instance):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.sync_interval = sync_interval
        self.method_to_delay = method_to_delay
        self.instance = instance
        self.counter = 0

    def sync(self):
        self.scheduler.enter(0, 1, self.schedule_sync, argument=(self.scheduler, ))
        self.scheduler.run()

    def schedule_sync(self, scheduler):
        method = getattr(self.instance, self.method_to_delay, None)
        if method is not None:
            method()
        self.counter += 1
        if self.counter < self.sync_interval:
            scheduler.enter(self.sync_interval, 1, self.schedule_sync, argument=(scheduler, ))

    def stop(self):
        self.scheduler.cancel()