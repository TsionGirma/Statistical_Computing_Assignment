#BMI Calculation
Weight=float(input("Enter your weight in kg\n"))
Height=float(input("Enter your height in meters\n"))
BMI= Weight/(Height**2)
if BMI <=18.5:
    print("You are underweight")
elif BMI>=25:
    print("You are overweight")
else:
    print("You are normal")
