#!/usr/bin/env python
import asyncio
import time

from commons.database.db import init_db, write_ddl
from commons.database.controller import run_query_in_db
from commons.models.people import PeopleRaw, PeopleFinal, PeopleRawBase
from commons.models.places import Places, PlacesBase
from ingestion.utils import ingest_csv_file
from ingestion.utils import flag_finished_ingestion
from logger.logs import logger
from sql.queries.queries import INSERT_PEOPLE_FINAL


async def main():
    await init_db()
    await write_ddl(
        table_names=[Places.__name__.lower(), PeopleRaw.__name__.lower(), PeopleFinal.__name__.lower()],
        write_path='./sql/schemas'
    )
    await ingest_csv_file(
        input_path='/app/data', file_name='places.csv',delimiter=',',
        csv_pydantic_schema=PlacesBase,
        ModelORM=Places)
    await ingest_csv_file(
        input_path='/app/data', file_name='people_col.csv',delimiter=',',
        csv_pydantic_schema=PeopleRawBase,
        ModelORM=PeopleRaw)
    await run_query_in_db(query=INSERT_PEOPLE_FINAL, mode="post")


if __name__ == '__main__':
    asyncio.run(main())  # here is where our ingestion process run
    logger.info("Finished ingestion process, writing healthcheck file for docker to start jsonwriter")
    flag_finished_ingestion(path="./finished_ingestion", file_name="/finished_ingestion.txt")
    time.sleep(20)  # to make sure our healthcheck can pick up the file we have written above