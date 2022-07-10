import os

from sqlmodel import SQLModel

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from logger.logs import logger


DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        logger.info("Starting to create database tables")
        await conn.run_sync(SQLModel.metadata.create_all)
        logger.info("Finished creating database tables")


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


async def write_ddl(table_names: str, write_path: str) -> None:
    logger.info(f"writing ddl file for tables {table_names}")
    for table_name in table_names:
        get_ddl = f"SHOW CREATE TABLE {table_name}"
        drop = f"DROP TABLE IF EXISTS {table_name}; \n\n"
        try:
            async with engine.connect() as conn:
                result = await conn.execute(text(get_ddl))
                ddl = result.fetchall()
                write_ddl = drop + str(ddl[0][1]).split('ENGINE')[0] + ";"
                with open(f'{write_path}/{table_name}.sql', 'w') as f:
                    f.write(write_ddl)
                    logger.info(f"table {table_name} was created successfully")
        except Exception as e:
            logger.error(
                f"something failed, could not write the ddl for the table {table_name}, error as follows: {e}")