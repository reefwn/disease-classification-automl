from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class DiabetesForm(FlaskForm):
    age = SelectField(
        'Select your age',
        validators=[DataRequired()],
        choices=[
            ('1', '18-24'),
            ('2', '25-30'),
            ('3', '31-35'),
            ('4', '36-40'),
            ('5', '41-45'),
            ('6', '46-50'),
            ('7', '51-55'),
            ('8', '56-60'),
            ('9', '60-64'),
            ('10', '65-69'),
            ('11', '70-74'),
            ('12', '75-79'),
            ('13', '80+'),
        ]
    )
    sex = RadioField(
        'What is your sex?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Male'),
            ('0', 'Female'),
        ]
    )
    high_chol = RadioField(
        'Have you been told by a doctor or other health professional that you have high cholesterol?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    chol_check = RadioField(
        'Have you had your cholesterol checked within the past 5 years?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    bmi = IntegerField(
        'What is your BMI?',
        validators=[DataRequired(), NumberRange(min=10, max=50)],
    )
    smoker = RadioField(
        'Do you smoke cigarettes? (If you have smoked at least 100 cigarettes in your entire life, then you are considered a smoker.)',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    heart_disease_or_attack = RadioField(
        'Have you ever been told by a doctor or other health professional that you had a heart attack, a coronary heart disease, or a stroke?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    phys_activity = RadioField(
        'During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    fruits = RadioField(
        'Do you eat fruit or drink 100% fruit juices one or more time per day?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    veggies = RadioField(
        'Do you eat vegetables one or more times per day?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    hvy_alcohol_consump = RadioField(
        'Are you an alcoholic? (adult men >=14 drinks per week and adult women>=7 drinks per week)',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    gen_hlth = RadioField(
        'In general, would you say your health is:',
        validators=[DataRequired()],
        choices=[
            ('1', 'Excellent'),
            ('2', 'Very good'),
            ('3', 'Good'),
            ('4', 'Fair'),
            ('5', 'Poor'),
        ]
    )
    men_hlth = IntegerField(
        'Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?',
        validators=[InputRequired(), NumberRange(min=0, max=30)],
    )
    phys_hlth = IntegerField(
        'Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?',
        validators=[InputRequired(), NumberRange(min=0, max=30)],
    )
    diff_walk = RadioField(
        'Do you have serious difficulty walking or climbing stairs?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    stroke = RadioField(
        'Have you ever been told by a doctor or other health professional that you had a stroke?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )
    high_bp = RadioField(
        'Have you ever been told by a doctor or other health professional that you have high blood pressure?',
        validators=[DataRequired()],
        choices=[
            ('1', 'Yes'),
            ('0', 'No'),
        ]
    )

    submit = SubmitField('Submit')
