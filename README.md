ResiliaProject is a Bottle/JavaScript web app and REST API to view dummy data notifications that the Gates Foundation would receive.

In order to have everything working locally, you need the following processes: Install python requirements with pip install -r requirements.txt 

1. Virtualenv -> source <virtualenv>/bin/activate
   
2. Create database table -> python src/notification_store.py
   
3. Bottle server -> python src/notification_server.py
   
4. HTML server - > open src/frontend/html/index.html

