import FolderLogic as fl
import SchedulerLogic as sl

active = True

while active:

    prompt = ("\nWelcome to the test beackup utility.")
    prompt += ("\nPress Ctrl+C to close script.")
    prompt += ("\nType 'start' or 'help' to either start the utilty, or get documentation:")
    prompt = input(prompt)


    if prompt == 'start':
        source_prompt = "Enter source path: "
        source_path = input(source_prompt)

        replica_prompt = "Enter replica path: "
        replica_path = input(replica_prompt)

        logfile_prompt = "Enter logfile path: "
        logfile_path = input(logfile_prompt)

        sync_interval_prompt = "Enter sync interval (in seconds): "
        sync_interval = input(sync_interval_prompt)
        sync_interval = int(sync_interval)
        
        folder_logic = fl.FolderLogic(source_path, replica_path, logfile_path)
        s = sl.SchedulerLogic(sync_interval, 'compare_folder_contents_and_update', folder_logic)
        
        while active:
            s.sync()

    elif prompt == 'help':
        print("Documentation placeholder.")
    
    else:
        print("Unknwon command.")