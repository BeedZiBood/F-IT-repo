import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as read_file:
        reader = [item for item in csv.DictReader(read_file, delimiter=",", quotechar="\n")]

    with open(OUTPUT_FILENAME, 'w') as write_file:
        json.dump(reader, write_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
