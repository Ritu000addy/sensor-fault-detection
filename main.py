from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os, sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils.main_utils import read_yaml_file
#from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
#def test_exception():
#    try:
#        logging.info("We are dividing 1 by 0")
#        x = 1/0
#    except Exception as e:
#        raise SensorException(e, sys)

#if __name__ == '__main__':
#    try:
#        test_exception()
#    except Exception as e:
#        print(e)
    #mongodb_client = MongoDBClient()
    #print("collection name": mongodb_client.database.list_collection_names())

#if __name__ == "__main__":
#    training_pipeline_config = TrainingPipelineConfig()
#    data_ingestion_config = DataIngestionConfig(training_pipeline_config= training_pipeline_config)
#    print(data_ingestion_config.__dict__)

#def set_env_variable(env_file_path):
#    if os.getenv('MONGO_DB_URL', None) is None:
#    env_config = read_yaml_file(env_file_path)
#    os.environ['MONGO_DB_URL'] = env_config['MONGO_DB_URL']

if __name__ == '__main__':
    try:
#        env_file_path = "D:\project\sfd\sensor-fault-detection\env.yaml"
#        set_env_variable(env_file_path)
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)
