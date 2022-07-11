import csv
from pydantic import ValidationError
from sqlmodel import SQLModel
from typing import Optional

from logger.logs import logger


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
