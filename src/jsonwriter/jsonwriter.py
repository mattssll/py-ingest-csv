import asyncio
import json

from commons.database.controller import run_query_in_db
from logger.logs_jsonwriter import logger
from sql.queries.queries import VIEW_PEOPLE_BY_COUNTRY


async def main():
    logger.info("Starting to write json output results with number of people per country")
    with open('./data/agg_ppl_by_country.json', 'w') as json_file:
        results = await run_query_in_db(VIEW_PEOPLE_BY_COUNTRY, mode="get")
        print(dict(results))
        json.dump(dict(results), json_file)
    logger.info("Finished to write json output results with number of people per country, "
                "see it in ./data/agg_ppl_by_country.json")


if __name__ == '__main__':
    asyncio.run(main())
