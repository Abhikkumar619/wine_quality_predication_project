from ml_project.components.model_trainer import ModelTrainer
from ml_project import logger
from ml_project.config.configuration import ConfigurationManger

STAGE_NAME ="Model Training stage" 

class ModelTrainingPipeline: 
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManger()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try: 
        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<\n\n")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<\n\n")


    except Exception as e: 
        logger.exception(e)
        raise e

