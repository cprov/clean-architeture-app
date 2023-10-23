from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ca_app import (
    config,
    models,
)

engine = create_engine(
    config.settings.database_uri,
    connect_args={"check_same_thread": False}
)

models.Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
