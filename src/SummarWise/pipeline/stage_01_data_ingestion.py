from SummarWise.constants import *
from SummarWise.utils.common import read_yaml, create_directories

from SummarWise.config.configuration import ConfigurationManager
from SummarWise.conponents.data_ingestion import DataIngestion

from SummarWise.entity import(DataIngestionConfig)

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()