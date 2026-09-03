from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from form
    age = int(request.form.get("age"))
    weight = float(request.form.get("weight"))
    height = float(request.form.get("height"))
    goal = request.form.get("goal")
    activity_level = request.form.get("activity_level")

    # Calculate BMI
    height_m = height / 100
    bmi = round(weight / (height_m * height_m), 2)

    # Generate Fitness Recommendation
    if goal == "Weight Loss":
        prediction = (
            "Focus on cardio exercises, calorie control, "
            "healthy food and regular workouts."
        )

    elif goal == "Muscle Gain":
        prediction = (
            "Focus on strength training, protein-rich food "
            "and regular muscle-building exercises."
        )

    else:
        prediction = (
            "Follow a balanced workout routine with proper diet "
            "and regular physical activity."
        )

    # Add activity level recommendation
    if activity_level == "Low":
        prediction += " Start with light exercises and gradually increase intensity."

    elif activity_level == "Moderate":
        prediction += " Maintain a balanced combination of cardio and strength training."

    elif activity_level == "High":
        prediction += " Continue advanced workouts with proper rest and recovery."

    # Send result back to same page
    return render_template(
        "index.html",
        prediction=prediction,
        bmi=bmi
    )


if __name__ == "__main__":
    app.run(debug=True)
