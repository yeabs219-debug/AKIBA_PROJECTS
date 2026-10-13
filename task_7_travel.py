destination = input("Enter your destination: ")
distance = float(input("Enter distance in kilometers: "))
speed = float(input("Enter speed in kilometers per hour: "))

time_hour= distance/speed
time_minutes = time_hour *60
eat =0 
if time_hour < 1 :
   eat = f"{time_minutes} minutes"
else : 
   eat = f"{time_hour} hours"
print(f"""
destination : {destination}
distance: {distance}
speed : {speed}
estimated arrival time = {eat}""")


