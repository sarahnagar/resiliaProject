from datetime import datetime
import sqlite3


def createNotificationsDb():
    """ Creates the notifications database
        Each entry contains a division, notification and timestamp
    """
    currentFirstVaccineNotification = "19.9% of the American population have received at least one dose of the vaccine"
    currentSecondVaccineNotification = '10.3% of the American population are fully vaccinated'
    previousFirstVaccineNotification = "11.7% of the American population have received at least one dose of the vaccine"
    previousSecondVaccineNotification = '5.6% of the American population are fully vaccinated'

    # creating the sqLite notification database
    print("Create a notifications database...")

    try:
        conn = sqlite3.connect('notifications.db')  # creates notifications store
        conn.execute(
            "CREATE TABLE notifications (division char(50), notification char(1000), timestamp int(50), id INTEGER "
            "PRIMARY KEY )")
        # current vaccine notification #1
        conn.execute("INSERT INTO notifications (division, notification, timestamp) VALUES ('Global Health Division', "
                     "'{vaccineNotification}', '{timestamp}')".format(
            vaccineNotification=currentFirstVaccineNotification,
            timestamp=datetime.now()))
        # current vaccine notification #2
        conn.execute("INSERT INTO notifications (division, notification, timestamp) VALUES ('Global Health Division', "
                     "'{vaccineNotification}', '{timestamp}')".format(
            vaccineNotification=currentSecondVaccineNotification,
            timestamp=datetime.now()))
        # previous vaccination notification
        conn.execute("INSERT INTO notifications (division, notification, timestamp) VALUES ('Global Health Division', "
                     "'{vaccineNotification}', '{timestamp}')".format(
            vaccineNotification=previousFirstVaccineNotification,
            timestamp=datetime(2021, 2, 6, 12, 49, 9, 700689)))
        conn.execute("INSERT INTO notifications (division, notification, timestamp) VALUES ('Global Health Division', "
                     "'{vaccineNotification}', '{timestamp}')".format(
            vaccineNotification=previousSecondVaccineNotification,
            timestamp=datetime(2021, 2, 6, 12, 49, 9, 700689)))

        conn.execute("INSERT INTO notifications (division, notification, timestamp) VALUES ('Global Health Division', "
                     "'First vaccine was distributed in America', '{timestamp}')".format(
            timestamp=datetime(2020, 12, 14, 3, 59, 33, 700689)))
        conn.execute("INSERT INTO notifications (division, notification, timestamp) VALUES ('Global Health Division', "
                     "'Pfizer vaccine was approved by FDA', '{timestamp}')".format(
            timestamp=datetime(2020, 9, 3, 10, 19, 7, 700689)))
        conn.execute("INSERT INTO notifications (division, notification, timestamp) VALUES ('Global Health Division', "
                     "'Moderna vaccine was approved by FDA', '{timestamp}')".format(
            timestamp=datetime(2020, 7, 26, 15, 13, 0, 700689)))

        conn.commit()

        print("Database notifications.db created")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    createNotificationsDb()