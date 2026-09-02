from flask import Flask, render_template, request
from model import predict_fitness_plan

app = Flask(__name__)


# ==========================================
# BMI CALCULATION
# ==========================================

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# ==========================================
# FITNESS SCORE
# ==========================================

def calculate_fitness_score(bmi, activity):

    score = 50

    # BMI score
    if 18.5 <= bmi < 25:
        score += 30
    elif 17 <= bmi < 30:
        score += 20
    else:
        score += 10

    # Activity score
    if activity == "high":
        score += 20
    elif activity == "medium":
        score += 15
    else:
        score += 5

    return min(score, 100)


def get_fitness_score_category(score):

    if score >= 85:
        return "Excellent 🔥"
    elif score >= 70:
        return "Good 💪"
    elif score >= 50:
        return "Average 👍"
    else:
        return "Needs Improvement 📈"


# ==========================================
# CALORIE CALCULATOR
# ==========================================

def calculate_calories(age, weight, height, activity, goal):

    # Basic calorie estimation
    # Mifflin-style simplified formula
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    # Activity multiplier
    if activity == "low":
        multiplier = 1.2
    elif activity == "medium":
        multiplier = 1.55
    else:
        multiplier = 1.725

    daily_calories = bmr * multiplier

    # Goal-based calorie target
    if goal == "weight_loss":
        target_calories = daily_calories - 500
    elif goal == "muscle_gain":
        target_calories = daily_calories + 300
    else:
        target_calories = daily_calories

    return {
        "maintenance": round(daily_calories),
        "target": round(target_calories)
    }


# ==========================================
# AI HEALTH INSIGHTS
# ==========================================

def get_ai_insights(bmi, activity, goal):

    insights = []

    # BMI insight
    if bmi < 18.5:
        insights.append(
            "Your BMI is below the normal range. Focus on healthy nutrition and gradual strength building."
        )

    elif bmi < 25:
        insights.append(
            "Your BMI is within the normal range. Maintain your current healthy lifestyle."
        )

    elif bmi < 30:
        insights.append(
            "Your BMI is above the normal range. Regular exercise and balanced nutrition may help improve fitness."
        )

    else:
        insights.append(
            "Your BMI is in a high range. Focus on gradual lifestyle improvements and consider consulting a qualified professional."
        )

    # Activity insight
    if activity == "low":
        insights.append(
            "Your activity level is low. Try gradually increasing daily movement such as walking and light exercise."
        )

    elif activity == "medium":
        insights.append(
            "Your activity level is moderate. Maintaining consistency can help improve your fitness."
        )

    else:
        insights.append(
            "Your activity level is high. Remember to include proper rest and recovery."
        )

    # Goal insight
    if goal == "weight_loss":
        insights.append(
            "AI suggests focusing on regular exercise, strength training, and balanced nutrition for your weight-loss goal."
        )

    elif goal == "muscle_gain":
        insights.append(
            "AI suggests focusing on progressive strength training, sufficient protein, and adequate recovery for muscle gain."
        )

    else:
        insights.append(
            "AI suggests maintaining a balanced combination of cardio, strength exercises, and flexibility training."
        )

    return insights


# ==========================================
# FITNESS RECOMMENDATIONS
# ==========================================

def get_fitness_recommendation(goal):

    if goal == "weight_loss":

        return {
            "workout": """Cardio and Full Body Workout
• Walking or Running
• Squats
• Push-ups
• Jumping Jacks""",

            "diet": """Focus on:
• Vegetables and fruits
• Protein-rich foods
• Balanced meals
• Adequate water intake""",

            "days": "5 days per week"
        }

    elif goal == "muscle_gain":

        return {
            "workout": """Strength Training
• Squats
• Push-ups
• Weight Training
• Shoulder Exercises""",

            "diet": """Focus on:
• Protein-rich foods
• Balanced meals
• Healthy carbohydrates
• Adequate water intake""",

            "days": "4-5 days per week"
        }

    else:

        return {
            "workout": """General Fitness Routine
• Walking or Jogging
• Stretching
• Push-ups
• Squats""",

            "diet": """Maintain a healthy balanced diet with:
• Fruits
• Vegetables
• Protein
• Sufficient water""",

            "days": "3-4 days per week"
        }


# ==========================================
# MAIN APPLICATION
# ==========================================

@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        # Get user input
        age = int(request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        goal = request.form["goal"]
        activity = request.form["activity"]

        # BMI
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        # Machine Learning Prediction
        ai_prediction = predict_fitness_plan(
            bmi,
            activity,
            goal
        )

        # Fitness Score
        fitness_score = calculate_fitness_score(
            bmi,
            activity
        )

        score_category = get_fitness_score_category(
            fitness_score
        )

        # AI Health Insights
        insights = get_ai_insights(
            bmi,
            activity,
            goal
        )

        # Calorie Calculation
        calories = calculate_calories(
            age,
            weight,
            height,
            activity,
            goal
        )

        # Fitness Recommendations
        recommendation = get_fitness_recommendation(goal)

        # Store all results
        result = {
            "age": age,
            "bmi": bmi,
            "category": category,

            "ai_prediction": ai_prediction,

            "fitness_score": fitness_score,
            "score_category": score_category,

            "insights": insights,

            "maintenance_calories": calories["maintenance"],
            "target_calories": calories["target"],

            "workout": recommendation["workout"],
            "diet": recommendation["diet"],
            "days": recommendation["days"]
        }

    return render_template("index.html", result=result)


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)