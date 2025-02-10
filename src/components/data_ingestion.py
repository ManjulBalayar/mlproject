import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

# You will be able to directly define your class variables
@dataclass
class DataIngestionConfig:
    # My data ingestion will save my training data/output in this specific path
    train_data_path: str=os.path.join('artifact', 'train.csv')
    test_data_path: str=os.path.join('artifact', 'test.csv')
    raw_data_path: str=os.path.join('artifact', 'data.csv')

class DataIngestion:
    def __init__(self):
        # This ingestion_config will consist of the 3 values from our config class. Meaning all 3 will get saved in the following variable.
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        # If data is stored in some databases, this code will read from the database.
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            # Makes the artifacts directory/folder from the ingestion, if it doesn't exist already
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # First save our raw dataset
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train-test-split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Second, save our training and testing dataset after the split
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of the data is completed')

            return (
                # Will be needing these for my data transformation so that it can just grab this information
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ =  data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
