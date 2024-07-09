import pickle
import os

# Define the file path
file_path = "data.pkl"

def createDataFile():
    # Check if the file exists
    try:
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        # If the file does not exist, create an empty pickle file
        print("No Data yet, we will fill it together!")
        Weight = input("What is your current weight in kg: ")
        Calories = input("What is your daily calorie intake in kcal: ")
        diet = input("What is your diet? (Bulking[B]/Cutting[c]/Maintenance[m]): ")
        if diet == "b":
            diet = "Bulking"
        elif diet == "c":
            diet = "Cutting"
        elif diet == "m":
            diet = "Maintenance"
        elif diet != "b" and diet != "c" and diet != "m":
            print("Please enter a valid input!")
            exit()
        if Weight == "" or Calories == "":
            print("Please enter a valid input!")
            exit()
        Day = 0
        data = {Day:{"globalWeight": float(Weight), "gloabalCalories": int(Calories), "diet": diet}}
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)

def changeDataFile():
    # Load the data from the file
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    # Change the data
    changing = "a"
    while changing != "w" and changing != "c" and changing != "d":
        print(changing)
        changing = input("What do you want to change? (Weight[w]/Calories[c]/Diet[d]): ")
        if changing == "w":
            realyChange = input("Do not Change this Weight, if you don't want to reset the Calculation. Still wanna change the weight? (yes/no): ")
            if realyChange == "yes":
                Weight = input("What is your current weight in kg: ")
                data[0]["globalWeight"] = float(Weight)
        elif changing == "c":
            realyChange = input("Do not Change this Calories, if you don't want to reset the Calculation. Still wanna change the Calories? (yes/no): ")
            if realyChange == "yes":
                Calories = input("What is your daily calorie intake in kcal: ")
                data[0]["gloabalCalories"] = int(Calories)
        elif changing == "d":
            diet = input("What is your diet? (Bulking[b]/Cutting[c]/Maintenance[m]): ")
            if diet == "b":
                diet = "Bulking"
            elif diet == "c":
                diet = "Cutting"
            elif diet == "m":
                diet = "Maintenance"
            data[0]["diet"] = diet
        else:
            exitWhile = input("Please enter a valid input. Do you want to exit? (yes/no): ")
            if exitWhile == "yes":
                exit()
        # Save the data
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)

def showDataFile():
    # Load the data from the file
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    currentDay = 0
    for i in data:
        currentDay = i
    # Print the data
    print("Your current day is: " + str(currentDay))
    if currentDay == 0:
        print("Your startweight is: " + str(data[0]["globalWeight"]) + " kg")
        print("Your daily calorie intake is: " + str(data[0]["gloabalCalories"]) + " kcal")
        print("Your diet is: " + str(data[0]["diet"]))
    else:
        print("Your startweight/current Weight is: " + str(data[0]["globalWeight"]) + "/" + str(data[currentDay]["currentWeight"]) + " kg")
        print("Your daily calorie intake/today's calorie is: " + str(data[0]["gloabalCalories"]) + "/" + str(data[currentDay]["totalCalories"]) + " kcal")
        print("Your diet is: " + str(data[0]["diet"]))
        analyst = dataAnalysis()
        print("Your current status is: " + analyst)
        weeklyweightDif = weeklyWeightDif()
        print(weeklyweightDif)

def dataAnalysis():
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    currentDay = 0
    for i in data:
        currentDay = i
    if data[0]["diet"] == "Bulking":
        if data[currentDay]["totalCalories"] > int(data[0]["gloabalCalories"] + 500):
            return "You are over 500 kcal over your daily intake. Even when you are Bulking, you should not eat to much. You should eat less!"
        elif data[currentDay]["totalCalories"] <= int(data[0]["gloabalCalories"]):
            return "You are eating to less. You should eat more!"
        elif data[currentDay]["totalCalories"] + 200 > int(data[0]["gloabalCalories"]) and data[currentDay]["totalCalories"] <= int(data[0]["gloabalCalories"] + 500):
            return "You are eating enough. Keep going!"
        else:
            return "You are minimal over your daily intake. You should eat at least 200 kcal more then your daily intake!"
    elif data[0]["diet"] == "Cutting":
        if data[currentDay]["totalCalories"] > int(data[0]["gloabalCalories"]):
            return "You are eating to much. You should eat less!"
        elif data[currentDay]["totalCalories"] <= int(data[0]["gloabalCalories"] - 700):
            return "You are eating to less. You should eat more!"
        elif data[currentDay]["totalCalories"] > int(data[0]["gloabalCalories"] - 700) and data[currentDay]["totalCalories"] <= int(data[0]["gloabalCalories"]) - 200:
            return "You are perfectly cutting. Keep going!"
        else:
            return "You are minimal under your daily intake. You should eat at least 200 kcal less then your daily intake!"
    elif data[0]["diet"] == "Maintenance":
        if data[currentDay]["totalCalories"] > int(data[0]["gloabalCalories"] + 200 or data[currentDay]["totalCalories"] < int(data[0]["gloabalCalories"] - 200)):
            return "You are perftectly eating. Keep going!"
        elif data[currentDay]["totalCalories"] > int(data[0]["gloabalCalories"] + 200):
            return "You are eating to much. You should eat less!"
        else:
            return "You are eating to less. You should eat more!"
        
    
        
def weeklyWeightDif():
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    daysrecorded = 0
    for i in data:
        daysrecorded = i
    if daysrecorded < 8:
        return "You need at least 8 days to get a weekly weight difference."
    else:
        weeklyWeightDif = 0
        weeklycaloriesaverage = 0
        for i in range(0, 7):
            weeklyWeightDif = weeklyWeightDif + float(data[daysrecorded - i]["currentWeight"]) - float(data[daysrecorded - i - 1]["currentWeight"])
            weeklycaloriesaverage  = weeklycaloriesaverage + data[daysrecorded - i]["totalCalories"]
        weeklyWeightDif = round(weeklyWeightDif / 7, 2)
        weeklycaloriesaverage = round(weeklycaloriesaverage / 7, 0)
        whatchanged = ""
        caloriesDif = round(weeklycaloriesaverage - int(data[0]["gloabalCalories"]), 0)
        if data[0]["diet"] == "Bulking":
            if weeklycaloriesaverage >= int(data[0]["gloabalCalories"] and weeklyWeightDif <= 0):
                data[0]["gloabalCalories"] = round(data[0]["gloabalCalories"] + caloriesDif)
                whatchanged = "and maitanance calories have been changed to: " + str(data[0]["gloabalCalories"])
            elif weeklycaloriesaverage <= int(data[0]["gloabalCalories"] and weeklyWeightDif >= 0):
                data[0]["gloabalCalories"] = round(data[0]["gloabalCalories"] + caloriesDif)
                whatchanged = "and maitanance calories have been changed to: " + str(data[0]["gloabalCalories"])
        elif data[0]["diet"] == "Cutting":
            if weeklycaloriesaverage <= int(data[0]["gloabalCalories"] and weeklyWeightDif >= 0):
                data[0]["gloabalCalories"] = round(data[0]["gloabalCalories"]) + caloriesDif
                whatchanged = "and maitanance calories have been changed to: " + str(data[0]["gloabalCalories"])
            elif weeklycaloriesaverage >= int(data[0]["gloabalCalories"] and weeklyWeightDif <= 0):
                data[0]["gloabalCalories"] = round(data[0]["gloabalCalories"]) + caloriesDif
                whatchanged = "and maitanance calories have been changed to: " + str(data[0]["gloabalCalories"])
            elif weeklycaloriesaverage >= int(data[0]["gloabalCalories"] - 700 and weeklyWeightDif <= 0):
                data[0]["gloabalCalories"] = round(data[0]["gloabalCalories"]) + caloriesDif
                whatchanged = "and maitanance calories have been changed to: " + str(data[0]["gloabalCalories"])
        elif data[0]["diet"] == "Maintenance":
            if weeklycaloriesaverage >= int(data[0]["gloabalCalories"] and weeklyWeightDif <= 0):
                data[0]["gloabalCalories"] = round(data[0]["gloabalCalories"]) + caloriesDif
                whatchanged = "and maitanance calories have been changed to: " + str(data[0]["gloabalCalories"])
            elif weeklycaloriesaverage <= int(data[0]["gloabalCalories"] and weeklyWeightDif >= 0):
                data[0]["gloabalCalories"] = round(data[0]["gloabalCalories"]) + caloriesDif
                whatchanged = "and maitanance calories have been changed to: " + str(data[0]["gloabalCalories"])
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
        return "Your weekly weight difference is: " + str(round(weeklyWeightDif, 2)) + " kg " + whatchanged
        
def addDailyData():
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    currentDay = 0
    for i in data:
        currentDay = i
    currentDay = currentDay + 1
    print("Your current day is: " + str(currentDay)) 
    currentWeight = input("What is your weight today in kg(you should weight yourself in the morning after going to the toilet): ")
    currentCalories = input("What is your calorie intake today in kcal: ")
    train = input("Did you do any Training today? (yes/no): ")
    if train == "yes":
        todaysTraining = input("How many Calories did you burn today in Training in kcal: ")
    else:
        todaysTraining = 0
    totalCalories = int(currentCalories) - int(todaysTraining)
    data2 = {currentDay:{"currentWeight": float(currentWeight), "totalCalories": totalCalories}}
    data3 = {**data, **data2}
    with open(file_path, 'wb') as af:
        pickle.dump(data3, af)
    print("Your Data was added successfully!")

def changeDailyData():
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    currentDay = 0
    for i in data:
        currentDay = i
    currentDay = currentDay
    print("Your current day is: " + str(currentDay))
    print("Your Data for today is: ")
    print("Your weight today is: " + str(data[currentDay]["currentWeight"]) + " kg")
    print("Your calorie intake today is: " + str(data[currentDay]["totalCalories"]) + " kcal") 
    whichDay = input("Which day do you want to change: ")
    whichDay = int(whichDay)
    if whichDay not in data:
        print("This day does not exist yet. Please add the day first.")
    elif whichDay == 0:
        print("You can't change the startweight and the startcalories. Please change the global data instead.")
    else:
        print("Your Data for this day is: ")
        print("Your weight today is: " + str(data[whichDay]["currentWeight"]) + " kg")
        print("Your calorie intake today is: " + str(data[whichDay]["totalCalories"]) + " kcal")
        whatChange = input("What do you want to change? (Weight[w]/Calories[c]/TrainingCalories[t]/exit[e]): ")
        if whatChange == "w":
            currentWeight = input("What is your weight today in kg: ")
            data[whichDay]["currentWeight"] = float(currentWeight)
            print("You Data was changed successfully!")
        elif whatChange == "c":
            changeWhat = input("Do you wanna add, subtract or change the total calories? (add[a]/sub[b]/change[c]): ")
            if changeWhat == "a":
                currentCalories = input("How manny Calories you wanna add: ")
                data[whichDay]["totalCalories"] = int(data[whichDay]["totalCalories"]) + int(currentCalories)
                print("You Data was changed successfully!")
            elif changeWhat == "b":
                currentCalories = input("How manny Calories you wanna subtract: ")
                data[whichDay]["totalCalories"] = int(data[whichDay]["totalCalories"]) - int(currentCalories)
                print("You Data was changed successfully!")
            elif changeWhat == "c":
                currentCalories = input("What is your calorie intake today in kcal: ")
                todaysTraining = input("How many Calories did you burn today in Training in kcal: ")
                totalCalories = int(currentCalories) - int(todaysTraining)
                data[whichDay]["totalCalories"] = int(totalCalories)
                print("You Data was changed successfully!")
        elif whatChange == "t":
            changeWhat = input("Do you wanna add or subtract the training calories? (add[a]/sub[b]): ")
            if changeWhat == "a":
                todaysTraining = input("How manny Calories did you burn: ")
                data[whichDay]["totalCalories"] = int(data[whichDay]["totalCalories"]) - int(todaysTraining)
                print("You Data was changed successfully!")
            elif changeWhat == "b":
                todaysTraining = input("How manny Calories you wanna subtract from Training: ")
                data[whichDay]["totalCalories"] = int(data[whichDay]["totalCalories"]) + int(todaysTraining)
                print("You Data was changed successfully!")
        elif whatChange == "e":
            exit()
        else:
            exitWhile = input("Please enter a valid input. Do you want to exit? (yes/no): ")
            if exitWhile == "yes":
                exit()
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def deleteDailyData():
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    currentDay = 0
    for i in data:
        currentDay = i
    currentDay = currentDay
    print("Your current day is: " + str(currentDay))
    whichDay = input("Which day do you want to delete: ")
    whichDay = int(whichDay)
    if whichDay not in data:
        print("This day does not exist yet. Please add the day first.")
    elif whichDay == 0:
        print("You can't delete the startweight and the startcalories. Please change the global data instead.")
    else:
        print("Your Data for this day is: ")
        print("Your weight today is: " + str(data[whichDay]["currentWeight"]) + " kg")
        print("Your calorie intake today is: " + str(data[whichDay]["totalCalories"]) + " kcal")
        delete = input("Do you really wanna delete this day? (yes/no): ")
        if delete == "yes":
            del data[whichDay]
            print("Your Data was deleted successfully!")
        elif delete == "no":
            print("Your Data was not deleted!")
        else:
            exitWhile = input("Please enter a valid input. Do you want to exit? (yes/no): ")
            if exitWhile == "yes":
                exit()
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def deleteAllData():
    delete = input("Do you really wanna delete all data? (yes/no): ")
    if delete == "yes":
        os.remove("data.pkl")
        print("All Data was deleted successfully!")
    elif delete == "no":
        print("Your Data was not deleted!")
    exit()

def showDailyData():
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    whichDay = input("Which day do you want to show: ")
    whichDay = int(whichDay)
    if whichDay not in data:
        print("This day does not exist yet. Please add the day first.")
    else:
        print("Your Data for this day is: ")
        print("Your weight on that day is: " + str(data[whichDay]["currentWeight"]) + " kg")
        print("Your calorie intake on that day is: " + str(data[whichDay]["totalCalories"]) + " kcal")

print("Welcome to GymDietHelper!")
createDataFile()
while True:
    print("---------------------------------------------------------------------------------------------------------------------------------")
    showDataFile()
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("Options:")
    print("1. Change Gloabal Data")
    print("2. Add Daily Data")
    print("3. Change Daily Data")
    print("4. Delete Daily Data")
    print("5. Show Data")
    print("6. Delete All Data")
    print("7. Exit")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    option = input("What do you want to do? (Change Global Data[1]/Add Daily Data[2]/Change Daily Data[3]/Delete Daily Data[4]/Show Data[5]/Exit[6]): ")
    if option == "1":
        changeDataFile()
    elif option == "2":
        addDailyData()
    elif option == "3":
        changeDailyData()
    elif option == "4":
        deleteDailyData()
    elif option == "5":
        showDailyData()
    elif option == "6":
        deleteAllData()
    elif option == "7":
        exit()
    else:
        print("Please enter a valid input")
        continue


