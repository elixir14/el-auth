# el-auth
Authentication library for flask using multiple social media platform

### Setup

Install all dependencies using

`pip install -r requirments.txt`

Create `.env` file and add `MONGO_URI` (MongoDb connection string) and `SECRET_KEY` (for JWT).

Create `.flaskenv` and add `FLASK_APP` and `FLASK_ENV` (development or production).

### Start app

`flask run`

or

`flask run --host 0.0.0.0 --port 5000`
