import os
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionconfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.Ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method ot component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('read the data set as the data frame')

            os.makedirs(os.path.dirname(self.Ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.Ingestion_config.raw_data_path,index=False,header=True)

            logging.info("train test split initiated")
            train_set,test_set = train_test_split(df,test_size =0.2, random_state= 42)

            train_set.to_csv(self.Ingestion_config.train_data_path,index=False,header=True)

            train_set.to_csv(self.Ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of the data is completed")

            return(

                self.Ingestion_config.train_data_path,
                self.Ingestion_config.test_data_path
            )
        except Exception as e:
            raise customException(e , sys)

if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
