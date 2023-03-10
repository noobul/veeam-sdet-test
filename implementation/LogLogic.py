class LogLogic:

    def __init__(self, log_path, file, log_line):
        self.log_path = log_path
        self.file = file
        self.log_line = log_line

    def write_events_to_logfile(log_path, log_line):
        file = open(log_path, "w")
        file.write(log_line)
        print(log_line)
        file.close()