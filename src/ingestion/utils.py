import csv
import os
from sqlmodel import SQLModel
from typing import Type

from commons.database.controller import add_record_to_db
from ingestion.csvparser import validate_row
from logger.logs import logger


async def ingest_csv_file(input_path: str,
                              file_name: str,
                              delimiter: str,
                              csv_pydantic_schema: SQLModel,
                              ModelORM: Type[SQLModel]):
    """
    This method opens a csv file and iterates over it,
    it calls "validate_row()" that validates each row against the pre-defined schema,
    if validation is passed it inserts the record to the database,
    if not, then the errored records are sent to the logs of the app (allows for recovery)
    """
    logger.info(f"starting to ingest csv {input_path}/{file_name}")
    with open(f'{input_path}/{file_name}', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in reader:
            logger.info(f"row:  {row}")
            valid_object = validate_row(csv_row=row, csv_pydantic_schema=csv_pydantic_schema)
            if valid_object:
                await add_record_to_db(valid_object.dict(), ModelORM=ModelORM)
    logger.info(f"finished ingesting {input_path}/{file_name}")


def clean_logger():
    path = './logger/logs.log'
    if os.path.exists(path):
        os.remove(path)


def flag_finished_ingestion(path: str, file_name: str) -> None:
    try:
        os.mkdir(path)
        with open(f"{path}{file_name}", "w") as file1:
            file1.write("Ingestion was finished successfully")
    except FileExistsError as e:
        logger.error(f"problem writing confirmation file, error as follows: {str(e)}")
