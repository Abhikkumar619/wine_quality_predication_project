from ml_project import logger
from ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipeline.stage_02_data_validation import DataValidationTraningPipeline
from ml_project.pipeline.stage_03_data_transformation import DataTransformationTraningPipeline
from ml_project.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from ml_project.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Validation stage"

try:
    logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<")
    obj=DataValidationTraningPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation stage"

try:
    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<\n\n")
    obj=DataTransformationTraningPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<\n\n")
        
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME ="Model Training stage" 

try: 
    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<\n\n")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<\n\n")


except Exception as e: 
    logger.exception(e)
    raise e
 


STAGE_NAME= "Model Evaluation Stage"
try: 

    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<\n\n")
    obj=ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<\n\n")

except Exception as e: 
    logger.exception(e)
    raise e