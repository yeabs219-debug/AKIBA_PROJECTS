name = input("Enter your name: ")
math_score = min(float(input("Enter your Math score: ")) , 100)
python_score = min(float(input("Enter your python score: ")), 100)
english_score = min(float(input("Enter your English score: ")) , 100)

average = round((math_score + python_score + english_score) / 3 , 2) 

print(f"""
========================================
          STUDENT RESULT
========================================

Student: {name}

Python:       {python_score}
English:      {english_score}
Mathematics:  {math_score}
----------------------------------------
Average:      {average}
========================================


""")