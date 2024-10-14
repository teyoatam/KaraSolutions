
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Update this URL with your PostgreSQL database credentials
DATABASE_URL = "postgresql://postgres:postgres@localhost/telegram"  # Adjust this line

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()