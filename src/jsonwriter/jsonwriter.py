import asyncio
import json

from commons.database.controller import run_query_in_db
from logger.logs_jsonwriter import logger
from sql.queries.queries import VIEW_PEOPLE_BY_COUNTRY


async def write_json_from_db(file_path: str) -> None:
    logger.info("Starting to write json output results with number of people per country")
    with open(file_path, 'w') as json_file:
        results = await run_query_in_db(VIEW_PEOPLE_BY_COUNTRY, mode="get")
        json.dump(dict(results), json_file)
    logger.info(f"Finished to write json output results with number of people per country, "
                f"see it in {file_path}")


if __name__ == '__main__':
    asyncio.run(write_json_from_db(file_path='./data/summary_output.json'))
