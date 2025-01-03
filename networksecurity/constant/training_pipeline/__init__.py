import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phishingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")

SAVED_MODEL_DIR = os.path.join("final_model")
MODEL_FILE_NAME = "model.pkl"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "MAYANKAI"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation related constant start with Data_Transformation VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
PREPROCESSOR_OBJECT_FILE_name: str = "preprocessor_object"
## knn imputer to replace nan values
DATA_TRANSFFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}

"""
Model Trainer related constant start with MODEL TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:  str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE_FILE: str = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD: str = 0.05

TRAINING_BUCKET_NAME = "networksecurity112"

