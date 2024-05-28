#!/usr/bin/python3
import sys
import signal

# Initialize the total size of files
total_size = 0

# Dictionary to count the occurrences of specific status codes
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Counter for the number of processed lines
line_count = 0


def print_stats():
    """
    Print the current statistics: total file size and counts of status codes.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """
    Signal handler for SIGINT (Ctrl+C). Prints the current statistics and exits.
    """
    print_stats()
    sys.exit(0)


# Set up the signal handler to catch SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    # Process each line from standard input
    for line in sys.stdin:
        # Split the line into parts based on whitespace
        parts = line.split()

        # Check if the line format matches the expected pattern
        if len(parts) < 9 or parts[4] != '"GET' or parts[5] != '/projects/260' or parts[6] != 'HTTP/1.1"':
            continue

        try:
            # Extract the status code and file size from the appropriate parts
            status_code = int(parts[7])
            file_size = int(parts[8])
        except (ValueError, IndexError):
            # Skip the line if conversion fails or parts are missing
            continue

        # Accumulate the total file size
        total_size += file_size

        # Increment the count for the status code if it is one of the tracked codes
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Increment the line counter
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    # Print statistics and exit gracefully on Ctrl+C
    print_stats()
    sys.exit(0)
