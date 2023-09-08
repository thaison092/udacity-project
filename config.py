import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'DefaultEndpointsProtocol=https;AccountName=udacitystoragev1;AccountKey=xezS8OtKdEN14+llMIDni3YuSpoDkU4Y1EbjM5svkQ47TU1qHRQuV7z4h5QCwf9GuEpTkOM3ZzsK+ASt62JbjQ==;EndpointSuffix=core.windows.net'
    # BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ENTER_BLOB_ACCOUNT_NAME'
    # BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ENTER_IMAGES_CONTAINER_NAME'

    # SQL_SERVER = os.environ.get('SQL_SERVER') or 'ENTER_SQL_SERVER_NAME.database.windows.net'
    # SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ENTER_SQL_DB_NAME'
    # SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ENTER_SQL_SERVER_USERNAME'
    # SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'ENTER_SQL_SERVER_PASSWORD'
    
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'xezS8OtKdEN14+llMIDni3YuSpoDkU4Y1EbjM5svkQ47TU1qHRQuV7z4h5QCwf9GuEpTkOM3ZzsK+ASt62JbjQ=='
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacitystoragev1'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'sonpt@0902'

    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+18+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "RmZ8Q~fbH9d4ZVdaCwA-E-h_ZZ9O1fCpdGpo0cBj"


    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "df980e78-579e-442e-b134-4729c74848a0"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session