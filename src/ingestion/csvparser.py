import csv
from pydantic import ValidationError
from sqlmodel import SQLModel
from typing import Optional, Type

from commons.database.controller import add_record_to_db
from logger.logs_ingestion import logger


def validate_row(csv_row, csv_pydantic_schema) -> Optional[SQLModel]:
    """
    This function receives a csv row and validates it against a
    pydantic schema to make sure all fields and types are good
    according to the validation requirements of the model.
    :returns True if validation was good and False if not
    """
    try:
        object = csv_pydantic_schema(
            **csv_row
        )
        return object
    except ValidationError as e:
        logger.warning(f'validation error found, record wont be inserted into db, error as follows: {e}'
                  f'\n{{"errored_row":{csv_row}}}')
        return None


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
            valid_object = validate_row(csv_row=row, csv_pydantic_schema=csv_pydantic_schema)
            if valid_object:
                await add_record_to_db(valid_object.dict(), ModelORM=ModelORM)
    logger.info(f"finished ingesting {input_path}/{file_name}")