import os
import rarfile
import time

# Get the current directory
current_dir = os.getcwd()

# Concatenate the RAR file name to the current directory
rar_path = os.path.join(current_dir, 'open_data_peru.rar')

with rarfile.RarFile(rar_path) as rar:
    # Get a list of all files in the RAR archive
    file_list = rar.namelist()

    # Loop through each file in the RAR archive
    for file_name in file_list:
        # Get the file info
        file_info = rar.getinfo(file_name)

        # Get the modification time in seconds since the epoch
        mod_time = time.mktime(file_info.date_time + (0, 0, -1))

        # Convert the modification time to a human-readable string
        mod_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))

        # Print the file name and modification time
        print(f'{file_name}: {mod_time_str}')
