import mock
import pytest
from src.notification_store import createNotificationsDb


@mock.patch('sqlite3.connect')
def test_db_creation(mock_sqlite3Connect):
    createNotificationsDb()
    assert mock_sqlite3Connect.call_count == 1


if __name__ == "__main__":
    pytest.main()