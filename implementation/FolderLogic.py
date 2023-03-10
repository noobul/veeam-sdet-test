import os
import hashlib
from LogLogic import write_events_to_logfile

class FolderLogic:
    def __init__(self, source, replica):
        self.source = source
        self.replica =  replica

    def get_all_files_in_folder(self, directory_path, log_path):
        if os.listdir(directory_path) == []:
            write_events_to_logfile(log_path, "No files in folder "+directory_path+".")
            return None
        else:
            dir_list = os.listdir(directory_path)
            write_events_to_logfile(log_path, "Files and directoris in "+dir_list+" : ")
            return dir_list
        
    def compare_folder_contents(self, source_folder, replica_folder):
    