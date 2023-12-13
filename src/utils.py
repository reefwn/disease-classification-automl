from typing import Any


def to_diabetes_form(data: dict[str, Any]):
    return {
        'Age': int(data['age']),
        'Sex': int(data['sex']),
        'HighChol': int(data['high_chol']),
        'CholCheck': int(data['chol_check']),
        'BMI': data['bmi'],
        'Smoker': int(data['smoker']),
        'HeartDiseaseorAttack': int(data['heart_disease_or_attack']),
        'PhysActivity': int(data['phys_activity']),
        'Fruits': int(data['fruits']),
        'Veggies': int(data['veggies']),
        'HvyAlcoholConsump': int(data['hvy_alcohol_consump']),
        'GenHlth': int(data['gen_hlth']),
        'MentHlth': data['men_hlth'],
        'PhysHlth': data['phys_hlth'],
        'DiffWalk': int(data['diff_walk']),
        'Stroke': int(data['stroke']),
        'HighBP': int(data['high_bp'])
    }


def to_stroke_form(data: dict[str, Any]):
    return {
        'Sex': int(data['sex']),
        'Age': int(data['age']),
        'Hypertension': int(data['hypertension']),
        'HeartDisease': int(data['heart_disease']),
        'EverMarried': int(data['ever_married']),
        'WorkType': int(data['work_type']),
        'ResidenceType': int(data['residence_type']),
        'AvgGlucoseLevel': data['avg_glucose_level'],
        'BMI': data['bmi'],
        'SmokingStatus': int(data['smoking_status'])
    }


def to_display(name: str, result: dict[str, Any]):
    capitalized = name.capitalize()
    predict = result[capitalized]
    confidence = result[f'{capitalized}Probability'][predict]
    return {
        'name': capitalized,
        'predict': bool(predict),
        'confidence': f'{confidence:.0%}'
    }
