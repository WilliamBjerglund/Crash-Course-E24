
# Da jeg ikke gad inputte en masse test forsøg selv lavede jeg en ekstraopgave og lavede et array med test muligheder som displayes hvis funktionen køres.
# Dette vil blive fjernet skulle programmet releases men da det er lokalt ser jeg intet problem i at gemme en ekstra opgave :)
def DogFoodRecommendation(Age, Weight):
    if Age < 0:
        return "Invalid age."

    if Age < 0.5:
        return "Dogs under 6 months old are recommended to eat puppy food."

    if (Weight < 10 and Age >= 12) or (Weight >= 10 and Age >= 10):
        return "Older dogs are recommended to be on soft food."
    else:
        return "Adult dogs are recommended to be on standard dog food."


def DogFoodInput():
    Age = float(input("Enter your dog's age in years: "))
    Weight = float(input("Enter your dog's weight in kg: "))
    recommend = DogFoodRecommendation(Age, Weight)
    print(f"Dog age: {Age} years, Dog weight: {Weight} kg - {recommend}")


def DogFoodTest():
    test_cases = [
        (2, 21),    
        (0.3, 5),   
        (12, 9),    
        (11, 25),   
        (5, 7),     
    ]

    for age, weight in test_cases:
        recommendation = DogFoodRecommendation(age, weight)
        print(f"Dog age: {age} years, Weight: {weight} kg - {recommendation}")


DogFoodInput()


print("\nTesting predefined dog ages and weights:")
DogFoodTest()
