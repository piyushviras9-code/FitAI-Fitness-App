from sklearn.tree import DecisionTreeClassifier


# Sample training data
# BMI, Activity Level, Goal
X = [
    [17, 0, 0],
    [18, 1, 0],
    [20, 1, 2],
    [22, 2, 2],
    [24, 1, 2],
    [26, 0, 0],
    [27, 1, 0],
    [29, 2, 0],
    [21, 0, 1],
    [23, 1, 1],
    [25, 2, 1],
    [28, 1, 1],
    [30, 0, 0],
    [32, 1, 0],
    [19, 2, 2]
]

# Output labels
y = [
    "Weight Gain Plan",
    "Weight Gain Plan",
    "General Fitness Plan",
    "General Fitness Plan",
    "General Fitness Plan",
    "Weight Loss Plan",
    "Weight Loss Plan",
    "Weight Loss Plan",
    "Muscle Gain Plan",
    "Muscle Gain Plan",
    "Muscle Gain Plan",
    "Muscle Gain Plan",
    "Weight Loss Plan",
    "Weight Loss Plan",
    "General Fitness Plan"
]


# Create Decision Tree AI model
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)


def predict_fitness_plan(bmi, activity, goal):

    # Convert activity into numbers
    activity_map = {
        "low": 0,
        "medium": 1,
        "high": 2
    }

    # Convert goal into numbers
    goal_map = {
        "weight_loss": 0,
        "muscle_gain": 1,
        "fitness": 2
    }

    activity_value = activity_map[activity]
    goal_value = goal_map[goal]

    # AI Prediction
    prediction = model.predict([
        [bmi, activity_value, goal_value]
    ])

    return prediction[0]