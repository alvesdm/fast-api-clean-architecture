# fastapi-clean-architecture
A clean-architecture like rest api in python with FastAPI and Mongo

Warning: This is part of my python studies so keep in mind that better ways of implementing stuff you'll find here, might be possible.


## How to setup
- Make sure you have at least python 3.10.x installed;
- Create your virtual environment;
- Setup you mongodb
- Set your .env file (save it into the same folder level as the main.py file)
- > pip install -r requirements.txt
- > uvicorn app.presentation.main:app --reload
- if you want to prevent the __PyCache__ file to be created, run
- > export PYTHONDONTWRITEBYTECODE=1
