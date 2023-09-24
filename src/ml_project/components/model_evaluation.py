import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
from ml_project.utils.common import save_json
from ml_project.entity.config_entity import ModelEvaluationConfig
from pathlib import Path



class ModelEvaluation: 
    def __init__(self, config=ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rms=np.sqrt(mean_squared_error(actual, pred))
        mse=mean_absolute_error(actual, pred)
        r2=r2_score(actual, pred)

        return rms, mse, r2
    
    def save_results(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop([self.config.target_column], axis=1)
        test_y=test_data[[self.config.target_column]]

        predict_data=model.predict(test_x)

        (rms, mse, r2)=self.eval_metrics(actual=test_y, pred=predict_data)

        # Saving metrics path as local.

        score={"rms":rms, "mse": mse, "r2":r2}

        save_json(path=Path(self.config.metric_file_name),  data= score)

