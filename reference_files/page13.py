import threading
import time

def function_to_call():
    print("Function called within thread")
    time.sleep(10)
    print("Function execution completed")

def start_thread():
    # Create a new thread
    thread = threading.Thread(target=function_to_call)
    
    # Start the thread
    thread.start()
    
    # Do other tasks in the main thread
    print("Main thread continues execution while the function runs in the thread")
    time.sleep(1)
    print("Main thread execution completed")

# Call the function to start the thread
# start_thread()

