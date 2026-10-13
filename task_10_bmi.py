name = input("Enter your name: ")
weight = round(float(input( "Enter your weight(in kg): ")) ,2)
height = round(float(input( "Enter your height(in  M): ")) ,2)

bmi = round(weight / (height * height))

print(f"""
================================
          BMI REPORT
================================

Name: {name}
Weight: {weight} kg
Height: {height} m

BMI: {bmi}
================================

""")