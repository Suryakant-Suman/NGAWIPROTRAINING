import csv
with open("eg.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Id", "Name", "Age"])
        writer.writerow(["01", "Surya", "21"])
        writer.writerow(["02", "Surya", "22"])
        writer.writerow(["03", "Surya", "23"])
        writer.writerow(["04", "Surya", "24"])