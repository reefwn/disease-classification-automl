# Disease Classification (AutoML) Web Application

## Dataset

[Kaggle | Diabetes, Hypertension and Stroke Prediction](https://www.kaggle.com/datasets/prosperchuks/health-dataset)

## Create ML

### Data

![data](https://github.com/reefwn/disease-classification-automl/blob/main/images/data.png?raw=true)

### Training

![training](https://github.com/reefwn/disease-classification-automl/blob/main/images/training.png?raw=true)

### Output

![output](https://github.com/reefwn/disease-classification-automl/blob/main/images/output.png?raw=true)

## Model

### Diabetes

#### Settings

- Algorithm: Boosted Tree
- Max Iterations: 10
- Max Depth: 6
- Min Loss Reduction: 0
- Min Child Weight: 0.1
- Row Subsample Ratio: 1
- Column Subsample Ratio: 1
- Step Size: 0.3

#### Evaluation

|class|count|precision|recall|f1-score|
|---|---|---|---|---|
|1|101|69%|94%|0.8|
|0|100|91%|58%|0.71|

### Stroke

#### Settings

- Algorithm: Random Forest
- Max Iterations: 10
- Max Depth: 6
- Min Loss Reduction: 0
- Min Child Weight: 0.1
- Row Subsample Ratio: 0.8
- Column Subsample Ratio: 0.8

#### Evaluation

|class|count|precision|recall|f1-score|
|---|---|---|---|---|
|1|100|91%|92%|0.92|
|0|100|92%|91%|0.91|

## Development

- `.mlmodel` can only be used on macOS version 10.13 or later
- tried docker image `sickcodes/docker-osx`, but does not work

### Virtual ENV
```
python3 -m venv disease-classification
source disease-classification/bin/activate
```

### Install depedencies
```
pip3 install -r requirements.txt
```

### Running the app
```
python3 app.py
```

## Technologies & IDE

<div>
  <img style="float: left" src="https://developer.apple.com/assets/elements/icons/create-ml-framework/create-ml-framework-96x96_2x.png" height="48" alt="create-ml"> &nbsp;
  <img style="float: left" src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" height="48" alt="flask"> &nbsp;
  <img style="float: left" src="https://wtforms.readthedocs.io/en/3.1.x/_static/logo_joined.svg" height="48" alt="wtform"> &nbsp;
  <img style="float: left" src="https://bootstrap-flask.readthedocs.io/en/stable/_static/bootstrap-flask-logo.png" height="48" alt="bootstrap-flask"> &nbsp;
  <img style="float: left" src="https://code.visualstudio.com/assets/updates/1_35/logo-stable.png" height="48" alt="vscode">
</div>