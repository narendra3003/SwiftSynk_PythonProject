### using watchdog checking file is modified or not
# pip install watchdog
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been modified.')
        
        # Add your custom code to be executed when a file is modified
        # For example, you can call a function or run specific tasks.

if __name__ == "__main__":
    folder_to_watch = 'C:\\Users\\tupti\\OneDrive\\Desktop\\curr\\tp'  # Replace with the path to your folder

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)
    observer.start()

    try:
        print(f'Watching folder: {folder_to_watch}')
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
