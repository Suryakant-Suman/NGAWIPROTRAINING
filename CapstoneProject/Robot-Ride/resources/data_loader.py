import csv
import os

class data_loader:
    def load_common_test_data(self, file_path):
        # Path ko Windows ke hisaab se sahi karta hai
        normalized_path = os.path.normpath(file_path)
        
        if not os.path.exists(normalized_path):
            raise Exception(f"File nahi mili bhai! Check path: {normalized_path}")

        data_list = []
        with open(normalized_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data_list.append(row)
        return data_list