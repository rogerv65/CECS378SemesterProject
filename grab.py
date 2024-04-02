import subprocess
import os
import time
import shutil


# Function to run Sherlock and capture its output
def run_sherlock(username, sherlock_path):
    start_time = time.time()  # Record the start time

    try:
        # Run Sherlock as a subprocess and capture its output

        cmd = ['python3', os.path.join(sherlock_path, 'sherlock'), username, '--timeout', '1']

        result = ""

        with open(os.devnull, 'w') as null_device:
            # Run Sherlock as a subprocess with output suppression
            result = subprocess.run(cmd, stdout=null_device, stderr=null_device)

        return result.stdout

    except Exception as e:
        print(f"Error running Sherlock: {e}")
        return None

    finally:
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")


# Function to move Sherlock output files to a specific folder
def move_output_files(username, output_folder):
    file_path = username + ".txt"
    destination_folder = output_folder
    # Copy the file to the destination folder

    shutil.copy(file_path, destination_folder)

    # Remove the original file
    os.remove(file_path)



def grab(username):
    sherlock_path = '/Users/lucnguyen/Documents/VSCode/378Project/python/sherlock'
    run_sherlock(username, sherlock_path)
    output_folder = '/sherlock_outputs'

    file_path = username + ".txt"

    file_contents = " "
    # Open the text file in read mode
    with open((file_path), 'r') as file:
        # Read the entire contents of the file
        file_contents = file.read()

    # Print the contents of the file
    print(file_contents)

    # Check if the file exists before attempting to delete it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully")
    else:
        print(f"File '{file_path}' does not exist")
    
    return file_contents

# Main function
def main():
    grab()

if __name__ == "__main__":
    main()
