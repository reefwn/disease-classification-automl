import secrets
from flask import Flask, render_template
import coremltools as ct
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from src.forms.diabetes import DiabetesForm
from src.forms.stroke import StrokeForm
from src.utils import to_diabetes_form, to_stroke_form, to_display

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
    name = 'diabetes'
    form = DiabetesForm()

    if form.validate_on_submit():
        data = to_diabetes_form(form.data)
        result = diabetes_model.predict(data)
        display = to_display(name, result)
        return render_template(
            'result.html',
            name=display['name'],
            predict=display['predict'],
            confidence=display['confidence']
        )

    return render_template('form.html', form=form, name=name)


@app.route('/stroke', methods=['GET', 'POST'])
def stroke():
    name = 'stroke'
    form = StrokeForm()

    if form.validate_on_submit():
        data = to_stroke_form(form.data)
        result = stroke_model.predict(data)
        display = to_display(name, result)
        return render_template(
            'result.html',
            name=display['name'],
            predict=display['predict'],
            confidence=display['confidence']
        )

    return render_template('form.html', form=form, name=name)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
