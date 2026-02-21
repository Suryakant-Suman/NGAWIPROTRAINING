import csv
import os

# Go 2 levels up (from utilities → PytestSalenium → CapstoneProject)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_FILE = os.path.join(BASE_DIR, "TestData", "test_data.csv")


def load_all_data():
    with open(DATA_FILE, newline="") as f:
        return list(csv.DictReader(f))


def load_valid_users():
    return [row for row in load_all_data() if row["testcase"].startswith("valid")]


def load_invalid_users():
    return [row for row in load_all_data() if row["testcase"].startswith("invalid")]


def load_products():
    return list({row["product"] for row in load_all_data()})