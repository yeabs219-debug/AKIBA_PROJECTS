try:
  width= int(input("width of rectangle : "))
  length= int(input("length of rectangle : "))
except ValueError:
  print("Please enter valid integers for width and length.")

perimeter = 2 *( width + length)
area = length * width

if width<0 or length<0:
  print("width and length can not be negative")


print (f"""
perimeter = {perimeter}
area ={area}
""")
