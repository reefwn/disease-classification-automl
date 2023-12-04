from flask import Flask
import coremltools as ct

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Disease Classification</h1>'


@app.route('/predict')
def predict():
    diabetes_model = ct.models.MLModel('models/diabetes.mlmodel')
    return diabetes_model.predict({
        'Age': 13,
        'Sex': 0,
        'HighChol': 0,
        'CholCheck': 1,
        'BMI': 25,
        'Smoker': 0,
        'HeartDiseaseorAttack': 0,
        'PhysActivity': 0,
        'Fruits': 0,
        'Veggies': 0,
        'HvyAlcoholConsump': 4,
        'GenHlth': 14,
        'MentHlth': 14,
        'PhysHlth': 1,
        'DiffWalk': 0,
        'Stroke': 1,
        'HighBP': 0
    })


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
