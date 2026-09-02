from flask import Flask, render_template, request
from model import predict_fitness_plan

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    # When website is opened normally
    if request.method == "GET":
        return render_template("index.html")

    # When user submits the fitness form
    try:
        age = float(request.form.get("age", 0))
        weight = float(request.form.get("weight", 0))
        height = float(request.form.get("height", 0))
        goal = request.form.get("goal", "")
        activity = request.form.get("activity", "")

        # Validate inputs
        if age <= 0 or weight <= 0 or height <= 0:
            return render_template(
                "index.html",
                error="Please enter valid age, weight and height."
            )

        # Calculate BMI
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        # Get prediction from model
        try:
            prediction = predict_fitness_plan(age, weight, height, goal, activity)
        except Exception:
            prediction = "Personalized Fitness Plan"

        return render_template(
            "index.html",
            bmi=bmi,
            prediction=prediction,
            age=age,
            weight=weight,
            height=height,
            goal=goal,
            activity=activity
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=f"Something went wrong: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
