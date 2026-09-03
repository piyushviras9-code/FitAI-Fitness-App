from flask import Flask, render_template, request

app = Flask(__name__)


def predict_fitness_plan(bmi, activity_level, goal):

    # BMI Category
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal Weight"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # AI Fitness Recommendation Logic

    if goal == "Weight Loss":

        if activity_level == "Low":
            plan = "Begin with light cardio and walking. Gradually increase your workout intensity. Focus on a calorie-controlled balanced diet."

        elif activity_level == "Moderate":
            plan = "Follow regular cardio workouts combined with strength training. Exercise 4–5 days per week and maintain a healthy calorie deficit."

        else:
            plan = "Continue high-intensity cardio and strength training. Focus on proper recovery, hydration and a balanced calorie-controlled diet."

    elif goal == "Muscle Gain":

        if activity_level == "Low":
            plan = "Start with beginner strength training 3 days per week. Focus on basic exercises and gradually increase your workout intensity. Consume sufficient protein."

        elif activity_level == "Moderate":
            plan = "Follow a structured strength training program with progressive overload. Train 4–5 days per week and maintain a protein-rich balanced diet."

        else:
            plan = "Follow an advanced strength training routine with progressive overload. Ensure sufficient protein intake, proper recovery and adequate sleep."

    else:

        if activity_level == "Low":
            plan = "Start with light physical activity such as walking, stretching and basic exercises. Gradually build a consistent fitness routine."

        elif activity_level == "Moderate":
            plan = "Maintain a balanced combination of cardio and strength training. Exercise regularly and follow a healthy balanced diet."

        else:
            plan = "Maintain your current fitness level with a balanced workout routine. Include strength training, cardio, flexibility exercises and proper recovery."

    return bmi_category, plan


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form.get("age"))
    weight = float(request.form.get("weight"))
    height = float(request.form.get("height"))
    goal = request.form.get("goal")
    activity_level = request.form.get("activity_level")

    # BMI Calculation
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    bmi_category, prediction = predict_fitness_plan(
        bmi,
        activity_level,
        goal
    )

    return render_template(
        "index.html",
        prediction=prediction,
        bmi=bmi,
        bmi_category=bmi_category,
        goal=goal,
        activity_level=activity_level
    )


if __name__ == "__main__":
    app.run(debug=True)
