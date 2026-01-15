import xml.etree.ElementTree as ET

# Reading XML
tree = ET.parse("stud.xml")
root = tree.getroot()

for student in root.findall("student"):
    print(
        student.find("id").text,
        student.find("name").text,
        student.find("marks").text
    )

# Writing XML
root = ET.Element("employees")

emp1 = ET.SubElement(root, "emp")
ET.SubElement(emp1, "name").text = "Rama"
ET.SubElement(emp1, "id").text = "101"
ET.SubElement(emp1, "salary").text = "1000000"

emp2 = ET.SubElement(root, "emp")
ET.SubElement(emp2, "name").text = "Sita"
ET.SubElement(emp2, "id").text = "102"
ET.SubElement(emp2, "salary").text = "900000"

tree = ET.ElementTree(root)
ET.indent(tree, space="  ")
tree.write("test.xml")

print("Employee file written successfully")
