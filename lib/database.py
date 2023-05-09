"""providing db configuration"""
from os import environ
from decouple import config
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()


# DB_URL = oenviron["DB_URL"]
# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"


db_url_object = URL.create(
    drivername=config('DB_DRIVER'),
    username=config('DB_USERNAME'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST'),
    database=config('DB_NAME'),
)


# # Engine which will be used everywhere
engine = create_engine(
    url=db_url_object,
    connect_args={
        'ssl': {
            'ssl-mode': environ.get('SSL_MODE', 'false')
        }
    }
)
# engine = create_engine("mysql+pymysql://root:agile123@localhost/main-db")
# engine = "mysql+pymysql://root:agile123@localhost/test"


def get_session():
    """Get Session - used in fast API"""
    with Session(engine) as session:
        yield session


def create_db_tables():
    """create all tables"""
    SQLModel.metadata.create_all(engine)


create_db_tables()
