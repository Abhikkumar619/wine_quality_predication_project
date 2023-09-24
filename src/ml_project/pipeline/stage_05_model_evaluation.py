from ml_project.components.model_evaluation import ModelEvaluation
from ml_project import logger
from ml_project.config.configuration import ConfigurationManger

STAGE_NAME= "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManger()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evalutaion=ModelEvaluation(model_evaluation_config)
        model_evalutaion.save_results()


if __name__ == '__main__':
    try: 

        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<\n\n")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<\n\n")

    except Exception as e: 
        logger.exception(e)
        raise e
