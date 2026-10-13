name = input("Enter your name: ")
python_score = min(float(input("Enter your python score: ")) ,100)
math_score = min(float(input("Enter your math score: ")),100)
english_score = min(float(input("Enter your english score: ")) ,100)

average = round((python_score + math_score + english_score) / 3 , 2)


print(f"""
========================================
             STUDENT REPORT CARD
========================================

Student Name: {name}

Math Score: {math_score} 
Python Score: {python_score} 
English Score: {english_score} 
----------------------------------------
Average Score: {average}
========================================

""")