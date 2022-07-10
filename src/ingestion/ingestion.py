#!/usr/bin/env python

from commons.database.db import init_db, write_ddl
from commons.models.people import People
from commons.models.places import Places
import asyncio
"""
# connect to the database
engine = sqlalchemy.create_engine(
    "mysql://temper_code_test:good_luck@database/temper_code_test")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the table
Example = sqlalchemy.schema.Table(
    'examples', metadata, autoload=True, autoload_with=engine)

# read the CSV data file into the table
print("writing data to db")
with open('/data/example.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        connection.execute(Example.insert().values(name=row[0]))

# output the table to a JSON file
print("writing output file")
with open('/data/example_python.json', 'w') as json_file:
    rows = connection.execute(sqlalchemy.sql.select([Example])).fetchall()
    rows = [{'id': row[0], 'name': row[1]} for row in rows]
    json.dump(rows, json_file, separators=(',', ':'))


"""

async def start_db():
    await init_db()
    await write_ddl(table_names=[Places.__name__.lower(), People.__name__.lower()], write_path='./sql')

if __name__ == '__main__':
    asyncio.run(start_db())

