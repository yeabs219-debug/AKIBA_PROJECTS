
generateId = input("genenrate id ? :")
num = 1


while generateId=="yes" :
  akiba_id= (f"AKI-{num:04d}")
  name= input("name :")
  age= input("age :")
  university=  input("university: ")
  department= input("department: ")
  year= input("year:")
  phone= input("phone: ")
  print(f"""
  +--------------------------------+
  |       AKIBA STUDENT CARD       |
  +--------------------------------+
  | Name:{name}                    |
  | ID: {akiba_id}                 |
  | Department: {department}       |
  | Year: {year}                   |
  | University: {university}       |
  | Phone: {phone}                 |
  +--------------------------------+

    """)
  num+=1
  generateId=input("genenrate id ? :")
