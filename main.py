# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def getGenderInput():
    try:
        return str(input("What is your gender?: "))
    except:
        print("Invalid entry")
        return getGenderInput()

gender = getGenderInput()
while str(gender) != "male" and str(gender) != "female":
    print("Enter male or female")
    gender = getGenderInput()
print("Your selected gender is", gender)
def getInput(prompt):
    try:
        return float(input(prompt))
    except:
        print("Invalid entry, please enter a number")
        return getInput(prompt)


age = getInput("Please enter your age?: ")
print("Your selected age is", age)

height = getInput("What is your height in cm?: ")
print("Your selected height is", height, "cm")

weight = getInput("What is your weight in kg?: ")
print("Your selected weight is", weight, "kg")

def calcbmi(height, weight):
    bmi = float(weight) / ((float(height) / 100) ** 2)
    return bmi


bmi = calcbmi(height, weight)
print("Your BMI is: ", round(bmi, 2))
if float(bmi) < 18.5:
    print("You are underweight")
elif 18.5 <= float(bmi) <= 24.9:
    print("You are at a healthy weight")
elif 25 <= float(bmi) <= 29.9:
    print("You are overweight")
elif float(bmi) >= 30:
    print("You are obese")

def calcbmr(gender, height, weight, age):
    if str(gender) == "male":
        bmr = (88.4 + 13.4 * weight) + (4.8 * height) - (5.68 * age)
        return bmr
    else:
        bmr = (447.6 + 9.25 * weight) + (3.10 * height) - (4.33 * age)
        return bmr


bmr = calcbmr(gender, height, weight, age)
print("Your BMR is: ", round(bmr, 2))

def getActivityInput():
    try:
        return str(input("What is your activity level?: "))
    except:
        print("Invalid entry")
        return getActivityInput()

print("What activity level are you:\nsedentary(little to no exercise\nlightly active(exercise 1–3 days/week)\nmoderately active(exercise 3–5 days/week)\nactive(exercise 5–7 days/week)\nvery active(hard exercise 5–7 days/week)")
activity = getActivityInput()

while str(activity) != "sedentary" and str(activity) != "lightly active" and str(activity) != "moderately active" and \
str(activity) != "active" and str(activity) != "very active":
    print("Enter sedentary, lightly active, moderately active, active, very active")
    gender = getActivityInput()
print("Your selected activity level is", activity)

def calcCaloricBurn(bmr, activity):
    if activity == "sedentary":
        burn = float(bmr) * 1.2
        return burn
    elif activity == "lightly active":
        burn = float(bmr)* 1.375
        return burn
    elif activity == "moderately active":
        burn = float(bmr) * 1.55
        return burn
    elif activity == "active":
        burn = float(bmr) * 1.725
        return burn
    elif activity == "very active":
        burn = float(bmr) * 1.9
        return burn

burn = calcCaloricBurn(bmr, activity)
print("Your caloric burn is approximately", burn, "per day")

def getInput(prompt):
    try:
        return float(input(prompt))
    except:
        print("Invalid entry, please enter a number")
        return getInput(prompt)

protein = getInput("How much protein did you eat today?: ")
carbs = getInput("How much carbs did you eat today?: ")
fats = getInput("How much fats did you eat today?: ")
sugar = getInput("How much sugar did you eat today?: ")

print("You ate ", protein, "proteins, ", carbs, "carbs, ", fats, "fats and ", sugar, "sugars today.")
totalEnergy = (protein * 4) + (carbs * 4) + (fats * 9) + (sugar * 4)
print("That's ", totalEnergy, "calories in total!")
print ("Protein should be 10-35% of your calories, yours is", round(float((protein*4)/totalEnergy) * 100, 2), "%")male
proteinreq = float(weight) * 1.8

print("You should be eating at least", proteinreq, "per day")

