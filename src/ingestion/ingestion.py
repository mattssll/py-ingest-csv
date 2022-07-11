#!/usr/bin/env python

from commons.database.db import init_db, write_ddl
from commons.database.controller import run_query_in_db
from commons.models.people import PeopleRaw, PeopleFinal, PeopleRawBase
from commons.models.places import Places, PlacesBase
from ingestion.csvparser import ingest_csv_file
from sql.queries.queries import INSERT_PEOPLE_FINAL
import asyncio
"""
# read the CSV data file into the table


# output the table to a JSON file
print("writing output file")
with open('/data/example_python.json', 'w') as json_file:
    rows = connection.execute(sqlalchemy.sql.select([Example])).fetchall()
    rows = [{'id': row[0], 'name': row[1]} for row in rows]
    json.dump(rows, json_file, separators=(',', ':'))
"""

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
    await run_query_in_db(INSERT_PEOPLE_FINAL)

if __name__ == '__main__':
    asyncio.run(main())


