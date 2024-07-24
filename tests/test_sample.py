from boilerplate.database.sample import add_test_entry
import uuid
import pytest


@pytest.mark.functional
def test_add_db_entry():
    add_test_entry("1", str(uuid.uuid4()))
    add_test_entry("2", "my_test_val")
