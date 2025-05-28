from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_tranier import ModelTrainer
import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # logging.info("Data Ingestion is completed")
        
        data_transformation = DataTransformation()
        train_array, test_array, _ = data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        logging.info("Data Transformation is completed")
        
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_trainer(train_array, test_array)
        logging.info("Model Training is completed")

    except Exception as e:
        raise CustomException(e, sys)