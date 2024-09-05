import math

def BMICalculator():
    WeightKG = float(input("Enter your weight in Kg: "))
    Height = float(input("Enter your height in cm: "))
    
    HeightInMeters = Height / 100
    
    BMI = WeightKG/HeightInMeters**2
    print(f"Your BMI is: {BMI:.2f}")

BMICalculator()