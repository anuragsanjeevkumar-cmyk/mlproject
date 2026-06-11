import os
import sys
import numpy as np
import pandas as pd
import dill

from sklearn.metrics import r2_score
from src.exception import CustomException



from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)


from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def evaluate_model(X_train, y_train, X_test, y_test,
                   models, param):

    try:

        report = {}

        for model_name, model in models.items():

            para = param[model_name]

            # Hyperparameter Tuning
            gs = GridSearchCV(
                model,
                para,
                cv=3
            )

            gs.fit(X_train, y_train)

            # Set best parameters
            model.set_params(**gs.best_params_)

            # Train model with best parameters
            model.fit(X_train, y_train)

            # Prediction
            y_pred = model.predict(X_test)

            # R2 Score
            score = r2_score(y_test, y_pred)

            # Save score
            report[model_name] = score

        return report

    except Exception as e:
        raise CustomException(e, sys)