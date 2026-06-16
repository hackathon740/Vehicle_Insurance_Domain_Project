import os
import dill
from src.exception import MyException
from src.entity.estimator import MyModel
import sys
from pandas import DataFrame


class Proj1Estimator:
    """
    This class is used to save and retrieve our model from s3 bucket and to do prediction
    """

    def __init__(self,bucket_name,model_path,):
        """
        :param bucket_name: Name of your model bucket
        :param model_path: Location of your model in bucket
        """
        self.bucket_name = bucket_name
        self.model_path = model_path
        self.loaded_model:MyModel=None


    def is_model_present(self,model_path):
        return os.path.exists(model_path)

    def load_model(self,)->MyModel:
        """
        Load the model from the model_path
        :return:
        """
        try:
            model_path = os.path.join(
                "artifact",
                "03_07_2026_23_21_33",
                "model_trainer",
                "trained_model",
                "model.pkl"
            )

            with open(model_path, "rb") as file:
                model = dill.load(file)

            return model

        except Exception as e:
            raise MyException(e, sys)

        ## return self.s3.load_model(self.model_path,bucket_name=self.bucket_name)

    def save_model(self,from_file,remove:bool=False)->None:
        """
        Save the model to the model_path
        :param from_file: Your local system model path
        :param remove: By default it is false that mean you will have your model locally available in your system folder
        :return:
        """
        pass


    def predict(self,dataframe:DataFrame):
        """
        :param dataframe:
        :return:
        """
        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            return self.loaded_model.predict(dataframe=dataframe)
        except Exception as e:
            raise MyException(e, sys)