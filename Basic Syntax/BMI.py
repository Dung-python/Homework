__author__="Dung"

height = 69
weight = 185

bmi = (weight*0.45)/(height*0.025)**2
print (bmi)

if bmi <= 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25.0:
    print("Normal")
elif 25.0 <= bmi < 30.0:
    print("Overweight")
else:
    print ("Obese")