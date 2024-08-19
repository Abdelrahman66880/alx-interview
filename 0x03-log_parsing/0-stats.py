#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

log_parts = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""

import sys

# Dictionary to store the count of each status code
status_code_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_file_size = 0
line_counter = 0  # Track the number of processed lines

try:
    for log_entry in sys.stdin:
        log_parts = log_entry.split(" ")

        if len(log_parts) > 4:
            code = log_parts[-2]
            size = int(log_parts[-1])

            # Check if the status code exists in the dictionary and increment its count
            if code in status_code_count.keys():
                status_code_count[code] += 1

            # Update the total file size
            total_file_size += size

            # Update the line counter
            line_counter += 1

        if line_counter == 10:
            line_counter = 0  # Reset the line counter
            print('File size: {}'.format(total_file_size))

            # Print the count of each status code
            for code, count in sorted(status_code_count.items()):
                if count != 0:
                    print('{}: {}'.format(code, count))

except Exception as e:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for code, count in sorted(status_code_count.items()):
        if count != 0:
            print('{}: {}'.format(code, count))

