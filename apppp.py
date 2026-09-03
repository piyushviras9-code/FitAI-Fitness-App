from flask import Flask, render_template, request

app = Flask(__name__)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_fitness_score(bmi, activity):
    score = 100

    # BMI score
    if bmi < 18.5:
        score -= 20
    elif bmi < 25:
        score -= 5
    elif bmi < 30:
        score -= 15
    else:
        score -= 30

    # Activity score
    activity_scores = {
        "Low": 20,
        "Moderate": 5,
        "High": 0
    }

    score -= activity_scores.get(activity, 10)

    return max(40, min(score, 100))


def get_status(score):
    if score >= 90:
        return "Excellent 🔥"
    elif score >= 75:
        return "Good 👍"
    elif score >= 60:
        return "Average 🙂"
    else:
        return "Needs Improvement 💪"


def get_calories(age, weight, height, activity, goal):
    # Simple calorie estimation
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    activity_multiplier = {
        "Low": 1.2,
        "Moderate": 1.55,
        "High": 1.725
    }

    maintenance = round(
        bmr * activity_multiplier.get(activity, 1.2)
    )

    if goal == "Weight Loss":
        target = maintenance - 400
    elif goal == "Muscle Gain":
        target = maintenance + 300
    else:
        target = maintenance

    return maintenance, target


def get_recommendation(goal, activity, bmi_category):

    if goal == "Weight Loss":
        plan = "Weight Loss Plan"

        workout = [
            "Brisk Walking or Jogging",
            "Cycling",
            "Bodyweight Squats",
            "Push-ups",
            "Core Exercises"
        ]

        diet = [
            "High-protein foods",
            "More vegetables and fruits",
            "Controlled carbohydrate intake",
            "Adequate water intake"
        ]

        schedule = "4-6 days per week"

        insight = "AI suggests combining regular cardio with strength training and maintaining a healthy calorie deficit."

    elif goal == "Muscle Gain":
        plan = "Muscle Gain Plan"

        workout = [
            "Squats",
            "Push-ups",
            "Weight Training",
            "Shoulder Exercises",
            "Progressive Strength Training"
        ]

        diet = [
            "Protein-rich foods",
            "Balanced meals",
            "Healthy carbohydrates",
            "Adequate water intake"
        ]

        schedule = "4-5 days per week"

        insight = "AI suggests focusing on progressive strength training, sufficient protein, and adequate recovery for muscle gain."

    else:
        plan = "Fitness Maintenance Plan"

        workout = [
            "Walking or Light Jogging",
            "Strength Training",
            "Stretching",
            "Core Exercises",
            "Cardio Workouts"
        ]

        diet = [
            "Balanced meals",
            "Protein-rich foods",
            "Fresh fruits and vegetables",
            "Adequate water intake"
        ]

        schedule = "3-5 days per week"

        insight = "AI suggests maintaining a balanced combination of cardio, strength training, flexibility, and healthy nutrition."

    return plan, workout, diet, schedule, insight


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        age = int(request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        goal = request.form["goal"]
        activity = request.form["activity_level"]

        # BMI Calculation
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        bmi_category = get_bmi_category(bmi)

        # Fitness Score
        fitness_score = calculate_fitness_score(bmi, activity)
        status = get_status(fitness_score)

        # Calories
        maintenance_calories, target_calories = get_calories(
            age, weight, height, activity, goal
        )

        # AI Recommendation
        plan, workout, diet, schedule, insight = get_recommendation(
            goal, activity, bmi_category
        )

        # Health insights
        insights = []

        if bmi_category == "Normal Weight":
            insights.append(
                "Your BMI is within the normal range. Maintain your current healthy lifestyle."
            )
        elif bmi_category == "Underweight":
            insights.append(
                "Your BMI is below the normal range. Focus on healthy nutrition and strength-building exercises."
            )
        elif bmi_category == "Overweight":
            insights.append(
                "Your BMI is above the normal range. Regular exercise and a balanced diet can help improve fitness."
            )
        else:
            insights.append(
                "Your BMI is in a higher range. Focus on gradual lifestyle improvements, regular activity, and healthy nutrition."
            )

        if activity == "Low":
            insights.append(
                "Your activity level is low. Start gradually and increase your physical activity consistently."
            )
        elif activity == "Moderate":
            insights.append(
                "Your activity level is moderate. Maintaining consistency can help improve your fitness."
            )
        else:
            insights.append(
                "Your activity level is high. Ensure proper recovery, sleep, and balanced nutrition."
            )

        insights.append(insight)

        return render_template(
            "index.html",
            result=True,
            bmi=bmi,
            bmi_category=bmi_category,
            fitness_score=fitness_score,
            status=status,
            insights=insights,
            plan=plan,
            maintenance_calories=maintenance_calories,
            target_calories=target_calories,
            workout=workout,
            diet=diet,
            schedule=schedule
        )

    except Exception as e:
        return render_template(
            "index.html",
            error="Please enter valid information in all fields."
        )


if __name__ == "__main__":
    app.run(debug=True)
