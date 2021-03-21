ResiliaProject is a Bottle/JavaScript web app and REST API to view dummy data notifications that the Gates Foundation would receive.

In order to have everything working locally, you need the following processes:

1. Create virtualenv -> python -m venv virtualenv
2. Virtualenv -> source virtualenv/bin/activate
3. Install python requirements -> pip install -r requirements.txt
4. Create database table -> python src/notification_store.py
5. Bottle server -> python src/notification_server.py
6. HTML server - > open src/frontend/html/index.html

