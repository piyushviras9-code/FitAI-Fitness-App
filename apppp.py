from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get user input
    age = int(request.form.get("age"))
    weight = float(request.form.get("weight"))
    height = float(request.form.get("height"))
    goal = request.form.get("goal")
    activity_level = request.form.get("activity_level")

    # Calculate BMI
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    # BMI Category
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal Weight"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # Generate detailed fitness recommendation
    if goal == "Weight Loss":

        prediction = f"""
Your BMI is {bmi}, which falls under the {bmi_category} category.

Recommended Fitness Plan: Weight Loss Program

Exercise Recommendation:
• Cardio exercises such as running, cycling and skipping.
• Strength training 3 to 4 times per week.
• Aim for 30 to 45 minutes of physical activity daily.

Diet Recommendation:
• Focus on a balanced and calorie-controlled diet.
• Eat more vegetables, fruits and protein-rich foods.
• Reduce sugary drinks and processed food.

Activity Level Advice:
• Your current activity level is {activity_level}.
• Gradually increase your daily physical activity.

Final Recommendation:
Maintain consistency, proper sleep and a healthy diet for better results.
"""

    elif goal == "Muscle Gain":

        prediction = f"""
Your BMI is {bmi}, which falls under the {bmi_category} category.

Recommended Fitness Plan: Muscle Gain Program

Exercise Recommendation:
• Focus on strength training and progressive overload.
• Include exercises such as squats, push-ups, bench press and rows.
• Train major muscle groups 4 to 5 days per week.

Diet Recommendation:
• Consume protein-rich foods such as eggs, chicken, paneer, milk and pulses.
• Include healthy carbohydrates for energy.
• Drink enough water throughout the day.

Activity Level Advice:
• Your current activity level is {activity_level}.
• Balance intense workouts with proper rest and recovery.

Final Recommendation:
Follow a consistent workout routine and maintain proper nutrition to support muscle growth.
"""

    else:

        prediction = f"""
Your BMI is {bmi}, which falls under the {bmi_category} category.

Recommended Fitness Plan: Fitness Maintenance Program

Exercise Recommendation:
• Follow a combination of cardio and strength training.
• Exercise at least 4 to 5 days per week.
• Include stretching and flexibility exercises.

Diet Recommendation:
• Maintain a balanced diet with protein, carbohydrates and healthy fats.
• Eat fresh fruits and vegetables.
• Stay properly hydrated.

Activity Level Advice:
• Your current activity level is {activity_level}.
• Maintain a regular and active lifestyle.

Final Recommendation:
Continue following a balanced fitness routine to maintain your overall health and fitness.
"""

    return render_template(
        "index.html",
        prediction=prediction,
        bmi=bmi,
        bmi_category=bmi_category
    )


if __name__ == "__main__":
    app.run(debug=True)
