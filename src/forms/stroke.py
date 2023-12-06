from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class StrokeForm(FlaskForm):
    sex = RadioField(
        'What is your sex?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Male'),
            ('0', 'Female')
        ]
    )
    age = IntegerField(
        'What is your age?',
        validators=[DataRequired(), NumberRange(min=1, max=100)]
    )
    hypertension = RadioField(
        'Do you have hypertension?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No')
        ]
    )
    heart_disease = RadioField(
        'Do you have heart disease?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No')
        ]
    )
    ever_married = RadioField(
        'Are you married?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No')
        ]
    )
    work_type = SelectField(
        'What is your work type?',
        validators=[DataRequired()],
        choices=[
            ('0', 'Never worked'),
            ('1', 'Children'),
            ('2', 'Government job'),
            ('3', 'Self-employed'),
            ('4', 'Private')
        ]
    )
    residence_type = RadioField(
        'What is your residence type?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Urban'),
            ('0', 'Rural')
        ]
    )
    avg_glucose_level = FloatField(
        'What is your average glucose level?',
        validators=[DataRequired(), NumberRange(min=1, max=300)]
    )
    bmi = FloatField(
        'What is your BMI?',
        validators=[DataRequired(), NumberRange(min=1, max=100)]
    )
    smoking_status = SelectField(
        'Do you smoke cigarettes?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Smokes'),
            ('0', 'Never smoked'),
        ]
    )

    submit = SubmitField('Submit')
