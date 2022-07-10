#!/usr/bin/env python -m

import os
from commons.database.db import write_ddl, init_db
from commons.models.people import People
from commons.models.places import Places
import asyncio


def test_write_ddl():
    path_to_ddl = './tests/sql'
    path_places_ddl = f"{path_to_ddl}/{Places.__name__.lower()}.sql"
    path_people_ddl = f"{path_to_ddl}/{People.__name__.lower()}.sql"
    async def run_db_test():
        await init_db()
        await write_ddl(table_names=[Places.__name__.lower(), People.__name__.lower()], write_path=path_to_ddl)
    asyncio.run(run_db_test())
    assert os.path.exists(path_places_ddl) == True
    assert os.path.exists(path_people_ddl) == True


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }

#def test_always_fails():
#    assert False