import os

class LogLogic:
    """ Implementation of log logic."""

    def __init__(self, log_path, log_line):
        self.log_path = log_path
        self.log_line = log_line

    def write_events_to_logfile(self):
        self.make_folder_for_logs()
        file = open("log.text", "w")
        file.write(self.log_line)
        file.close()
        print(self.log_line)
    
    def make_folder_for_logs(self):
        try:
            os.mkdir(self.log_path)
        except:
            print("Folder alread exists. ")