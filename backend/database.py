from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config: ConfigParser = ConfigParser()
config.read('config/config.ini')

engine = create_engine(f'postgresql+psycopg2://{config["database"]["username"]}:{config["database"]["password"]}@{config["database"]["host"]}/{config["database"]["database"]}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
