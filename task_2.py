
generateId = input("genenrate id ? :")
num = 1


while generateId.strip().lower()=="yes" :
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
  | {"Name : " + name:<31}|
  | {"ID: " + akiba_id:<31}|
  | {"Department: " + department:<31}|
  | {"Year: " + year:<31}|
  | {"University: " + university:<31}|
  | {"Phone: " + phone:<31}|
  +--------------------------------+

    """)
  num+=1
  generateId=input("genenrate id ? :")
