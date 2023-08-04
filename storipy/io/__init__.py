import csv
from datetime import datetime


def read_csv(file_name):
    """Read a csv file

    :param file_name: File to read
    """
    rows = []
    with open(file_name) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            v = validate(row)
            if v is None:
                rows += [row]
            else:
                print(v)
                exit()
    return rows


def validate(row):
    for k, v in row.items():
        if k == "id":
            try:
                row["id"] = int(v)
            except:
                return "ID is not valid."

        if k == "created_at":
            try:
                datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
            except:
                return "Date format is not valid."

        if k == "amount":
            amount = as_float(v)
            if not amount:
                return "Amount must be a valid number and not equal to 0."
            row["amount"] = amount


def as_float(v):
    try:
        rv = float(v)
    except:
        rv = 0.0

    return rv
