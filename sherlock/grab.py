import subprocess
import os
import time

# Function to run Sherlock and capture its output
def run_sherlock(username, sherlock_path):
    start_time = time.time()  # Record the start time

    try:
        # Run Sherlock as a subprocess and capture its output

        cmd = ['python', os.path.join(sherlock_path, 'sherlock'), username, '--timeout', '5']

        result = ""

        with open(os.devnull, 'w') as null_device:
            # Run Sherlock as a subprocess with output suppression
            # result = subprocess.run(cmd, stdout=null_device, stderr=null_device)
            result = subprocess.run(cmd)
            print(result)

        return result.stdout

    except Exception as e:
        print(f"Error running Sherlock: {e}")
        return None

    finally:
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Function to move Sherlock output files to a specific folder
def grab(username, sherlock_path = './'):
    
    run_sherlock(username, sherlock_path)

    file_path = username + ".txt"

    file_contents = " "
    # Open the text file in read mode
    with open((file_path), 'r') as file:
        # Read the entire contents of the file
        file_contents = file.read()

    # Check if the file exists before attempting to delete it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully")
    else:
        print(f"File '{file_path}' does not exist")
    
    return file_contents