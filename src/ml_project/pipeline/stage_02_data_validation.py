from ml_project.config.configuration import ConfigurationManger
from ml_project.components.data_validation import DataValiadtion
from ml_project import logger

STAGE_NAME="Data Validation stage"

class DataValidationTraningPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManger()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj=DataValidationTraningPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<\n\n")

    except Exception as e:
        logger.exception(e)
        raise e


