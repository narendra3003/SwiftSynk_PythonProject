###To get last modified time and to get size
import os
import datetime

def get_last_modified_time(file_path):
    modified_timestamp = os.path.getmtime(file_path)
    modified_datetime = datetime.datetime.fromtimestamp(modified_timestamp)
    return modified_datetime

def get_file_size(file_path):
    # Get the size of the file in bytes
    file_size_bytes = os.path.getsize(file_path)
    return file_size_bytes

if __name__ == "__main__":
    # Replace with the path to your file
    file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\test.txt"  
    last_modified_time = get_last_modified_time(file_path)
    print(f"Last modified time of {file_path}: {last_modified_time}")
    file_size = get_file_size(file_path)
    print(f"Size of '{file_path}': {file_size} bytes")
