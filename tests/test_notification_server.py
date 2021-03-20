import mock
import pytest
import sqlite3
from src.notification_server import notificationApp
from webtest import TestApp

app = TestApp(notificationApp)


def test_root():
    response = app.get("/")
    assert response.status_code == 200
    assert response.body == b'Notification Server Is Up and Running!'


@mock.patch('sqlite3.connect')
def test_getNotifications(mock_sqlite3Connect):
    mock_sqlite3Connect().cursor().fetchall.return_value = [('Vaccination Distribution', 123456, 'test')]

    expectedResult = b'[{"division": "Vaccination Distribution", "timestamp": 123456, "notification": "test"}]'
    response = app.get("/notifications")
    assert response.status_code == 200
    assert response.body == expectedResult


@mock.patch('sqlite3.connect', return_value=sqlite3.connect("nonexistent.db"))
def test_getNotifications_operational_error(mock_sqlite3Connect):
    ## FIX THIS BROKEN TEST ##
    mock_sqlite3Connect.return_value = sqlite3.connect("nonexistent.db")
    response = app.get("/notifications")
    assert response.status_code == 400
    assert response.body == b'{"error": "no such table: notifications"}'


def test_getNotifications_db_error():
    with pytest.raises(Exception):
        response = app.get("/notifications")
        assert response.status_code == 400
        assert response.body == b'{"error": "Failed to get data from notifications.db"}'


if __name__ == "__main__":
    pytest.main()
