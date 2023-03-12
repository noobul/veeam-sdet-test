import os
import hashlib
import LogLogic as lg
import shutil

class FolderLogic:
    def __init__(self, source_folder, replica_folder, log_path):
        self.source_folder = source_folder
        self.replica_folder =  replica_folder
        self.log_path = log_path

    def log_folder_logic(self, message):
        """ Initialize log logic from LogLogic class. """
        log = lg.LogLogic(self.log_path, message)
        return log.write_events_to_logfile()

    def get_all_files_in_folder(self, directory_path):
        """ Gets all the files in a folder and checks if the folder is empty. """
        if os.listdir(directory_path) == []:
            self.log_folder_logic("No files in folder "+directory_path+".")
            return None
        else:
            dir_list = os.listdir(directory_path)

            return dir_list
        
    def md5(self, file_path):
        """ Get md5hash of files in folder. """
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
        
    def compare_folder_contents_and_update(self):
        """ Compares files in the folders. """
        source_files = self.get_all_files_in_folder(self.source_folder)
        replica_files = self.get_all_files_in_folder(self.replica_folder)

        # Get the list of files in both folders
        if source_files is not None and replica_files is not None:
            source_files_set = set(source_files)
            replica_files_set = set(replica_files)
        
            # Compare the two sets of files and find the differences
            files_only_in_source = source_files_set - replica_files_set
            files_only_in_replica = replica_files_set - source_files_set
            common_files = source_files_set.intersection(replica_files_set)
            different_files = set()
        
            # Check if the content of the common files is different in the two folders
            for file in common_files:
                path1 = os.path.join(self.source_folder, file)
                path2 = os.path.join(self.replica_folder, file)
                if os.path.isfile(path1) and os.path.isfile(path2):
                    if self.md5(path1) != self.md5(path2):
                        different_files.add(file)
            
            if files_only_in_source.issubset(files_only_in_replica):
                for file in different_files:
                    os.remove(file)
                    self.log_folder_logic("Deleting "+file+" from "+self.replica_folder+".")
            elif self.md5(files_only_in_source) != self.md5(files_only_in_replica):
                for file in files_only_in_source:
                    shutil.copy2(os.path.join(self.source_folder, file), self.replica_folder)
                    self.log_folder_logic("Updateting "+file+" from "+self.replica_folder+".")
        
        elif replica_files == None:
                for file in source_files:
                    shutil.copy2(os.path.join(self.source_folder, file), self.replica_folder)
                    self.log_folder_logic("Copying "+file+" to "+self.replica_folder+"")