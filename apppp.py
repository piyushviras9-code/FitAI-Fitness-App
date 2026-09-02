from flask import Flask, render_template, request
from model import predict_fitness_plan

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":
        try:
            age = request.form.get("age")
            weight = request.form.get("weight")
            height = request.form.get("height")
            goal = request.form.get("goal")
            activity_level = request.form.get("activity_level")

            # Check if all fields are filled
            if not all([age, weight, height, goal, activity_level]):
                error = "Please fill in all the fields."

            else:
                age = int(age)
                weight = float(weight)
                height = float(height)

                # Calculate BMI
                height_in_meters = height / 100
                bmi = weight / (height_in_meters ** 2)

                # Get AI Fitness Plan
                fitness_plan = predict_fitness_plan(
                    bmi,
                    activity_level,
                    goal
                )

                result = {
                    "age": age,
                    "bmi": round(bmi, 2),
                    "plan": fitness_plan["plan"],
                    "workout": fitness_plan["workout"],
                    "diet": fitness_plan["diet"],
                    "schedule": fitness_plan["schedule"]
                }

        except Exception as e:
            error = f"Something went wrong: {str(e)}"

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
