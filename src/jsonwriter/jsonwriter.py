import asyncio
import json

from commons.database.controller import run_query_in_db
from logger.logs import logger
from sql.queries.queries import VIEW_PEOPLE_BY_COUNTRY


async def write_json_from_db(file_path: str, sql_query: str) -> None:
    logger.info(f"Preparing to write json data in {file_path}")
    with open(file_path, 'w') as json_file:
        results = await run_query_in_db(sql_query, mode="get")
        json.dump(dict(results), json_file)
    logger.info(f"Finished to write json data in {file_path}")


if __name__ == '__main__':
    asyncio.run(write_json_from_db(file_path='./data/summary_output.json', sql_query=VIEW_PEOPLE_BY_COUNTRY))
