def calculate_calorie_intake(weight, height, age):
    # Harris-Benedict equation for calculating Basal Metabolic Rate (BMR)
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    
    # Adjust BMR based on activity level
    activity_level = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    
    activity = input("Enter your activity level (sedentary, lightly active, moderately active, very active, extra active): ")
    if activity.lower() not in activity_level:
        print("Invalid activity level. Using sedentary as default.")
        activity = 'sedentary'
    
    calorie_intake = bmr * activity_level[activity]
    return calorie_intake


def generate_diet_plan(calorie_intake):
    # Define macronutrient ratio (adjust as needed)
    protein_ratio = 0.3
    carbs_ratio = 0.4
    fat_ratio = 0.3
    
    protein = protein_ratio * calorie_intake / 4
    carbs = carbs_ratio * calorie_intake / 4
    fat = fat_ratio * calorie_intake / 9
    
    return protein, carbs, fat


def generate_workout_plan():
    # Define workout plan based on goals and preferences
    workout_plan = '''
    Monday: Chest and Triceps
    Tuesday: Back and Biceps
    Wednesday: Rest
    Thursday: Legs
    Friday: Shoulders and Abs
    Saturday: Rest
    Sunday: Rest
    '''
    
    return workout_plan


def main():
    print("Welcome to the Weight and Muscle Gain Bot!")
    
    # Get user input for weight, height, and age
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age in years: "))
    
    # Calculate recommended calorie intake
    calorie_intake = calculate_calorie_intake(weight, height, age)
    print("Recommended daily calorie intake:", calorie_intake)
    
    # Generate diet plan
    protein, carbs, fat = generate_diet_plan(calorie_intake)
    print("Diet Plan:")
    print("Protein:", protein, "grams")
    print("Carbs:", carbs, "grams")
    print("Fat:", fat, "grams")
    
    # Generate workout plan
    workout_plan = generate_workout_plan()
    print("Workout Plan:")
    print(workout_plan)


if __name__ == "__main__":
    main()
