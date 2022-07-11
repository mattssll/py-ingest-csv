#!/usr/bin/env python -m

import os
from commons.database.db import write_ddl, init_db
from commons.models.people import PeopleRaw, PeopleFinal, PeopleRawBase
from commons.models.places import Places, PlacesBase
from ingestion.csvparser import validate_row
import asyncio
import json


def test_write_ddl():
    path_to_ddl = './tests/sql/schemas'
    path_places_ddl = f"{path_to_ddl}/{Places.__name__.lower()}.sql"
    path_people_raw_ddl = f"{path_to_ddl}/{PeopleRaw.__name__.lower()}.sql"
    path_people_final_ddl = f"{path_to_ddl}/{PeopleFinal.__name__.lower()}.sql"

    async def run_db_test():
        await init_db()
        await write_ddl(
            table_names=[Places.__name__.lower(), PeopleRaw.__name__.lower(), PeopleFinal.__name__.lower()],
                        write_path=path_to_ddl
        )
    asyncio.run(run_db_test())
    assert os.path.exists(path_places_ddl) == True
    assert os.path.exists(path_people_raw_ddl) == True
    assert os.path.exists(path_people_final_ddl) == True


def test_parser_valid_record():
    place_record = json.dumps({
        "city": "Amsterdam",
        "county": "Noord Holland",
        "country": "Netherlands"
    })
    people_record = json.dumps({
        "given_name": "John",
        "family_name": "Wild",
        "date_of_birth": "1944-06-23",
        "place_of_birth": "Amsterdam",
    })
    validator_response_place = validate_row(
        csv_row=json.loads(place_record),
        csv_pydantic_schema=PlacesBase
    )
    validator_response_people = validate_row(
        csv_row=json.loads(people_record),
        csv_pydantic_schema=PeopleRawBase
    )
    assert isinstance(validator_response_place, PlacesBase)
    assert isinstance(validator_response_people, PeopleRawBase)


def test_parser_invalid_record():
    place_parser_response = validate_row(
        csv_row ={"dummie_field": "this field is non-existent"},
        csv_pydantic_schema=PlacesBase
    )
    people_parser_response = validate_row(
        csv_row={"dummie_field": "this field is non-existent"},
        csv_pydantic_schema=PeopleRawBase
    )
    assert place_parser_response is None
    assert people_parser_response is None
