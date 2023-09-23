from ml_project.components.data_transformation import DataTransformation
from ml_project import logger
from ml_project.config.configuration import ConfigurationManger
# from pathlib import Path

STAGE_NAME="Data Transformation stage"

class DataTransformationTraningPipeline: 
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManger()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<\n\n")
        obj=DataTransformationTraningPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<\n\n")

    except Exception as e:
        logger.exception(e)
        raise e