import pytest
from boilerplate.database.bootstrap import create_tables, drop_tables


@pytest.fixture(scope="session", autouse=True)
def initialize_db(request: pytest.FixtureRequest):
    drop_tables()
    create_tables()
