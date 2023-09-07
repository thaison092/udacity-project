import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'ENTER_STORAGE_CONNECTION_STRING'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'QOGw6ISSMk0mMX6P6z7ABDGabEsXco8mizaWN9bs9FJshVuea7Qs4+K0DRBStjXJE3P08S1ZS03b+AStsY7Elw=='
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacitystorage'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'sonpt@0902'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = "YvB8Q~p~grh81DW.xcbrAAzSmOKCX~bqLhkj8asH"

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "bd96d3ee-20f9-4701-833d-4e8c4ace8855"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session