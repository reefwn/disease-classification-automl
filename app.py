import secrets
from flask import Flask, render_template
import coremltools as ct
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from src.forms.diabetes import DiabetesForm

app = Flask(__name__, template_folder='src/templates')
app.secret_key = secrets.token_urlsafe(16)

bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)

diabetes_model = ct.models.MLModel('models/diabetes.mlmodel')


@app.route('/', methods=['GET', 'POST'])
def index():
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

    return render_template('form.html', form=form)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
