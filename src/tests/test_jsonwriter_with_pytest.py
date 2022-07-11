import asyncio
import os
import pytest

from jsonwriter.jsonwriter import write_json_from_db
from tests.sql.queries.test_query import TEST_QUERY


def test_jsonwriter_write_valid_json():
    json_path = './tests/data/json_test.json'
    if os.path.exists(json_path):
        os.remove(json_path)
    asyncio.run(write_json_from_db(file_path=json_path, sql_query=TEST_QUERY))
    assert os.path.exists(json_path) == True
