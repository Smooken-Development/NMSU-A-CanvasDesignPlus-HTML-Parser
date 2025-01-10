import re

def readFromInput(inputText, outputText):
    """
    Reads a subtitle file, adjusts timestamps by subtracting 9 seconds, 
    and writes the updated content to a new file.

    Args:
        inputText (str): Path to the input subtitle file.
        outputText (str): Path to the output subtitle file.
    """
    try:
        # Open the input file and read all lines
        with open(inputText, 'r') as file:
            lines = file.readlines()

        # List to store the updated lines
        new_content = []

        def adjust_timestamp(timestamp, seconds):
            """
            Adjusts a timestamp by subtracting a given number of seconds.

            Args:
                timestamp (str): The timestamp in the format hh:mm:ss,ms.
                seconds (int): Number of seconds to subtract.

            Returns:
                str: The adjusted timestamp in the same format.
            """
            # Split the timestamp into hours, minutes, seconds, and milliseconds
            h, m, s_ms = timestamp.split(':')
            s, ms = s_ms.split(',')

            # Convert time components to total seconds and subtract the given seconds
            total_seconds = int(h) * 3600 + int(m) * 60 + int(s) - seconds
            if total_seconds < 0:
                total_seconds = 0  # Prevent negative times

            # Convert total seconds back to hours, minutes, and seconds
            new_h, remainder = divmod(total_seconds, 3600)
            new_m, new_s = divmod(remainder, 60)

            # Return the adjusted timestamp in the original format
            return f"{int(new_h):02}:{int(new_m):02}:{int(new_s):02},{ms}"

        # Process each line in the input file
        for line in lines:
            # Check if the line contains a timestamp
            match = re.search(r'(\d{2}:\d{2}:\d{2},\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2},\d{3})', line)
            if match:
                # Extract the start and end timestamps
                start_time = match.group(1)
                end_time = match.group(2)

                # Adjust both timestamps by subtracting 9 seconds
                adjusted_start = adjust_timestamp(start_time, 9)
                adjusted_end = adjust_timestamp(end_time, 9)

                # Add the adjusted timestamps to the new content
                new_content.append(f"{adjusted_start} --> {adjusted_end}\n")
            else:
                # If the line does not contain a timestamp, keep it unchanged
                new_content.append(line)

        # Write the updated content to the output file
        with open(outputText, 'w') as file:
            file.writelines(new_content)

        print(f"Adjusted content written to {outputText}")

    except FileNotFoundError:
        # Handle the case where the input file does not exist
        print(f"Error: File '{inputText}' not found.")
    except Exception as e:
        # Catch and display any other errors
        print(f"An error occurred: {e}")

# File paths for input and output subtitle files
path = "C:\\Users\\Xlaye\\Desktop\\Latest.srt"  # Path to the input file
outputPath = "C:\\Users\\Xlaye\\Desktop\\NewLatest.srt"  # Path to the output file

# Call the function to process the file
readFromInput(path, outputPath)
