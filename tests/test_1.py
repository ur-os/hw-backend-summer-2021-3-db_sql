import os
from dataclasses import dataclass
from typing import Optional

import gino
from sqlalchemy.engine.url import URL
import pytest
from sql_querys import TASK_1_QUERY, TASK_2_QUERY, TASK_3_QUERY
import asyncio
import yaml
import datetime


@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    database: str = "demo"
    user: Optional[str] = None
    password: Optional[str] = None


@pytest.fixture
def config() -> DatabaseConfig:
    config_path = os.environ.get("CONFIGPATH")
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)
    return DatabaseConfig(**raw_config["database"])


@pytest.fixture(scope="session")
def loop():
    return asyncio.get_event_loop()


@pytest.fixture(autouse=True)
async def db(loop, config: DatabaseConfig):
    _engine = await gino.create_engine(
        URL(
            drivername="asyncpg",
            host=config.host,
            database=config.database,
            username=config.user,
            password=config.password,
            port=config.port,
        ),
        min_size=1,
        max_size=1,
    )
    db = gino.Gino()
    db.bind = _engine

    yield db

    await db.pop_bind().close()


class TestQuerys:
    @pytest.mark.asyncio
    async def test_query_1(self, db):
        #  flight_no | duration
        # -----------+----------
        #  PG0235    | 00:25:00
        #  PG0234    | 00:25:00
        #  PG0233    | 00:25:00
        #  PG0235    | 00:25:00
        #  PG0234    | 00:25:00
        res = await db.all(db.text(TASK_1_QUERY))
        assert res == [
            ("PG0235", datetime.timedelta(seconds=1500)),
            ("PG0234", datetime.timedelta(seconds=1500)),
            ("PG0233", datetime.timedelta(seconds=1500)),
            ("PG0235", datetime.timedelta(seconds=1500)),
            ("PG0234", datetime.timedelta(seconds=1500)),
        ]

    @pytest.mark.asyncio
    async def test_query_2(self, db):
        #  flight_no | count
        # -----------+-------
        #  PG0260    |    27
        #  PG0371    |    27
        #  PG0310    |    27
        res = await db.all(db.text(TASK_2_QUERY))
        assert res == [("PG0260", 27), ("PG0371", 27), ("PG0310", 27)]

    @pytest.mark.asyncio
    async def test_query_3(self, db):
        #  count
        # --------
        #  16824
        res = await db.scalar(db.text(TASK_3_QUERY))
        assert res == 16824
