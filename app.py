import secrets
from flask import Flask, render_template
import coremltools as ct
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from src.forms.diabetes import DiabetesForm
from src.forms.stroke import StrokeForm

app = Flask(__name__, template_folder='src/templates')
app.secret_key = secrets.token_urlsafe(16)

bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)

diabetes_model = ct.models.MLModel('models/diabetes.mlmodel')
stroke_model = ct.models.MLModel('models/stroke.mlmodel')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    form = DiabetesForm()

    if form.validate_on_submit():
        data = form.data
        return diabetes_model.predict({
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
        })

    return render_template('form.html', form=form, name='diabetes')


@app.route('/stroke', methods=['GET', 'POST'])
def stroke():
    form = StrokeForm()

    if form.validate_on_submit():
        data = form.data
        return stroke_model.predict({
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
        })

    return render_template('form.html', form=form, name='stroke')


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
