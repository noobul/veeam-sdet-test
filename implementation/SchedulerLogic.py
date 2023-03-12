import sched
import time

class SchedulerLogic:
    def __init__(self, sync_interval, method_to_delay):
        self.sync_interval = sync_interval
        self.method_to_delay = method_to_delay
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def sync(self):
        self.scheduler(0, 1, self.schedule_sync,
                        arguments=(self.scheduler, self.scheduler))
        self.scheduler.run()

    def schedule_sync(self, scheduler):
        self.method_to_delay()
        scheduler.enter(self.sync_interval, 1, self.schedule_sync, arguments = (scheduler,))

    def stop(self):
        self.scheduler.cancel()