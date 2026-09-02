def predict_fitness_plan(bmi, activity_level, goal):
    """
    Simple fitness recommendation model.
    Returns a suitable fitness plan based on BMI,
    activity level, and fitness goal.
    """

    goal = goal.lower()
    activity_level = activity_level.lower()

    # Weight Loss Plan
    if "weight loss" in goal or "lose" in goal:
        return {
            "plan": "Weight Loss Plan",
            "workout": "Cardio • Running • Cycling • HIIT",
            "diet": "Calorie-controlled meals • High protein • Vegetables • Adequate water",
            "schedule": "4-5 days per week"
        }

    # Muscle Gain Plan
    elif "muscle gain" in goal or "gain" in goal:
        return {
            "plan": "Muscle Gain Plan",
            "workout": "Strength Training • Squats • Push-ups • Weight Training • Shoulder Exercises",
            "diet": "Protein-rich foods • Balanced meals • Healthy carbohydrates • Adequate water intake",
            "schedule": "4-5 days per week"
        }

    # General Fitness Plan
    else:
        return {
            "plan": "General Fitness Plan",
            "workout": "Walking • Jogging • Basic Strength Training • Stretching",
            "diet": "Balanced meals • Fruits • Vegetables • Protein-rich foods • Adequate water",
            "schedule": "3-5 days per week"
        }
