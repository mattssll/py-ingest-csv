from typing import Type
from sqlalchemy import text
from sqlmodel import SQLModel
from commons.database.db import get_session, engine
from logger.logs import logger


async def add_record_to_db(record: SQLModel, ModelORM: Type[SQLModel]) -> None:
    """
    This function receives a record from a SQLModel Schema,
    and then inserts this record into the database
    :param record: SQLModel Record, Base Schema
    :param ModelORM: The ORM Class that points to a table where we will insert the data
    :return: a confirmation with the id of the inserted record
    """
    async_session = await get_session()
    async with async_session() as session:
        try:
            orm_object = ModelORM(
                **record
            )
            session.add(orm_object)
            await session.commit()
            return orm_object.id
        except Exception as e:  # in case PK already exists for example, simply discard it
            print("failed on insertion of record to db, error: ", e)


async def run_query_in_db(query: str) -> None:
    """
    Runs a query from a .sql file in the mysql database
    :param query: .sql query picked up from a python variable in src/sql/queries/queries.py
    :return: None
    """
    try:
        logger.info("Started to run a .sql query in the database")
        async with engine.connect() as conn:
            await conn.execute(text(query))
            await conn.commit()
        logger.info("Finished running a .sql query in the database")
    except Exception as e:
        logger.error(f"an error happened when running your query, error as follows: {e}")
