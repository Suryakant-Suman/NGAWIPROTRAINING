import csv
import os

BASE = os.path.dirname(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE, "TestData", "test_data.csv")


def load_all_data():
    with open(DATA_FILE, newline="") as f:
        return list(csv.DictReader(f))


def load_valid_users():
    return [row for row in load_all_data() if "valid" in row["testcase"]]


def load_invalid_users():
    return [row for row in load_all_data() if "invalid" in row["testcase"]]


def load_products():
    return list({row["product"] for row in load_all_data()})