import os
from datetime import datetime

class LogLogic:
    """ Implementation of log logic."""

    def __init__(self, log_path, log_line):
        self.log_path = log_path
        self.log_line = log_line

    def write_events_to_logfile(self): 
        self.make_folder_for_logs()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.join(self.log_path, "log.txt"), "a") as f:
            f.write(now + " " + self.log_line + "\n")
        print(self.log_line)
    
    def make_folder_for_logs(self):
        try:
            os.mkdir(self.log_path)
        except:
            pass