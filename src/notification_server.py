import sqlite3
import json
import logging
import bottle
from bottle import Bottle, run

notificationApp = Bottle()  # let's create our own instance of the app


def getHeaders():
    """ These headers are used so that we don't get CORS errors
        due to the web app location and the server location being different
    """
    return {'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'}


@notificationApp.route('/')
def root():
    """ Checks that the app is alive and healthy """
    return "Notification Server Is Up and Running!"


@notificationApp.route('/notifications')
def getNotifications():
    """ Returns the notifications from the database"""
    # gets the data from the notifications db
    try:
        conn = sqlite3.connect('notifications.db')
        c = conn.cursor()

        # get all the data from the db except id (ie. timestamp, message, division)
        c.execute("SELECT division, timestamp, notification FROM notifications")
        result = c.fetchall()
        logging.debug("The database returned {} rows".format((len(result))))
        c.close()
    except sqlite3.OperationalError as e:
        errorMessage = json.dumps({"error": str(e)})
        return bottle.HTTPResponse(body=errorMessage, status=400, headers=getHeaders())
    except Exception as e:
        errorMessage = json.dumps({"error": str(e)})
        return bottle.HTTPResponse(body=errorMessage, status=400,
                                   headers=getHeaders())

    # format the data so the front end can consume it easily
    # we know the order of the data because it's the same order we passed into the select statement
    resultDict = [{'division': notification[0], 'timestamp': notification[1], 'notification': notification[2]} for
                  notification in result]
    return bottle.HTTPResponse(body=json.dumps(resultDict), status=200, headers=getHeaders())


if __name__ == "__main__":
    run(notificationApp)
