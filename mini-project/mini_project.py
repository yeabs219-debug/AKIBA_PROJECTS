
generateId = input("generate id(yes/no): ")
num = 0

while generateId.strip().lower() == "yes":
  name= input("name :")
  age= input("age :")
  city= input("city: ")
  university=  input("university: ")
  department= input("department: ")
  email= input("email: ")
  phone= input("phone: ")
  favProgLang= input("favourite programing language :")
  goal= input("goal: ")
  num +=1
  id = f"AKB-00{num}"
  print(f"""
================================================
              AKIBA STUDENT PROFILE
================================================

Name:                 {name}
Student ID:           {id}
Age:                  {age}
City:                 {city}
University:            {university}
Department:            {department}
Email:                 {email}
Phone:                 {phone}
Favorite Language:     {favProgLang}

Programming Goal:
{goal}.

================================================



========================================

""")
  generateId =input("generate id(yes/no): ")

