#!/usr/bin/env python
import asyncio
import time
import os

from commons.database.db import init_db, write_ddl
from commons.database.controller import run_query_in_db
from commons.models.people import PeopleRaw, PeopleFinal, PeopleRawBase
from commons.models.places import Places, PlacesBase
from logger.logs_ingestion import logger
from ingestion.csvparser import ingest_csv_file
from sql.queries.queries import INSERT_PEOPLE_FINAL




async def main():
    await init_db()
    await write_ddl(
        table_names=[Places.__name__.lower(), PeopleRaw.__name__.lower(), PeopleFinal.__name__.lower()],
        write_path='./sql/schemas'
    )
    await ingest_csv_file(
        input_path='/app/data',
        file_name='places.csv',
        delimiter=',',
        csv_pydantic_schema=PlacesBase,
        ModelORM=Places)
    await ingest_csv_file(
        input_path='/app/data',
        file_name='people.csv',
        delimiter=',',
        csv_pydantic_schema=PeopleRawBase,
        ModelORM=PeopleRaw)
    logger.info("Preparing to insert data in peoplefinal")
    await run_query_in_db(query=INSERT_PEOPLE_FINAL, mode="post")
    logger.info("Finished inserting data in peoplefinal")

def finished_ingestion(path: str, file_name: str) -> None:
    os.mkdir(path)
    with open(f"{path}{file_name}", "w") as file1:
        # Writing data to a file
        file1.write("Ingestion was finished successfully")

if __name__ == '__main__':
    asyncio.run(main())
    finished_ingestion(path = "./finished_ingestion", file_name="/finished_ingestion.txt")
    time.sleep(30)
