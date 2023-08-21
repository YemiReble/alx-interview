#!/usr/bin/python3
import sys


status_code = [200, 301, 400, 401, 403, 404, 405, 500]


def read_stdin_line_by_line():
    counterr = 0
    file_size = 0
    set_status = set(status_code)
    for line in sys.stdin:
        counterr += 1
        # print(line, end="")
        # Split the line into fields
        fields = line.strip().split()
        # print(fields)
        # for i, status_code in fields[8]:
        for code in fields[8]:
            if code in set_status:
                print("some code not found")

        print("{}: {}".format(fields[7], fields[8]))
        file_size += int(fields[8])
        if counterr == 9:
            print("File size: {}".format(file_size))  # {}". format(for i in ))
            break


if __name__ == "__main__":
    while True:
        read_stdin_line_by_line()
        # print(file_size())
