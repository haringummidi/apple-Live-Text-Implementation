import os
import sys
import subprocess


def list_directories(directory_path):
    try:
        # Use os.listdir to get a list of directories in the specified path
        directories = [d for d in os.listdir(directory_path)]

        # Print the list of directories
        for f in directories:
            file = os.path.join(directory_path, f)
            print(file)

            # Define the command you want to execute
            command = f'litex {file}'  # Replace with your desired command

            # Execute the command and capture the output
            try:
                result = subprocess.check_output(command, shell=True, text=True)
                print("Litex output:")
                print(result)
            except subprocess.CalledProcessError as e:
                print(f"Command failed with error: {e}")

            # Define the command you want to execute
            command = f'tesseract {file} - -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\ \-\:\\\/'  # Replace with your desired command

            # Execute the command and capture the output
            try:
                result = subprocess.check_output(command, shell=True, text=True)
                print("Tesseract output:")
                print(result)
            except subprocess.CalledProcessError as e:
                print(f"Command failed with error: {e}")


    except FileNotFoundError:
        print("Directory not found.")


if __name__ == "__main__":
    # Check if an argument was provided
    if len(sys.argv) != 2:
        print("Usage: python list_directories.py /path/to/directory")
    else:
        directory_path = sys.argv[1]
        list_directories(directory_path)
