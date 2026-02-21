import csv
import os

# Go 2 levels up (from utilities → PytestSalenium → CapstoneProject)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_FILE = os.path.join(BASE_DIR, "TestData", "e2e_master_data.csv")


def load_all_data():
    data = []

    with open(DATA_FILE, newline="") as f:
        reader = csv.reader(f, delimiter=';')
        rows = list(reader)

        # Extract headers (ignore first column)
        headers = rows[0][1:]
        headers = [h.replace("${", "").replace("}", "") for h in headers]

        for row in rows[1:]:
            row_dict = dict(zip(headers, row[1:]))
            data.append(row_dict)

    return data


# Since testcase column no longer exists,
# treat all users as valid
def load_valid_users():
    return load_all_data()


# No invalid users in this new CSV
def load_invalid_users():
    return []


def load_products():
    return list({row["product"] for row in load_all_data()})