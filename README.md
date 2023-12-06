# disease-classification-automl

## Dataset

[Kaggle | Diabetes, Hypertension and Stroke Prediction](https://www.kaggle.com/datasets/prosperchuks/health-dataset)

## Model Performance

### Diabetes

|class|count|precision|recall|f1-score|
|---|---|---|---|---|
|1|101|69%|94%|0.8|
|0|100|91%|58%|0.71|

### Stroke

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
  <img style="float: left" src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" height="48" alt="flask"> &nbsp;
  <img style="float: left" src="https://developer.apple.com/assets/elements/icons/create-ml-framework/create-ml-framework-96x96_2x.png" height="48" alt="create-ml"> &nbsp;
  <img style="float: left" src="https://code.visualstudio.com/assets/updates/1_35/logo-stable.png" height="48" alt="vscode">
</div>