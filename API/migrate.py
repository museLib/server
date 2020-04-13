from db import db
from user import models
from book import models
from sqlalchemy.sql import text


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)

    # Install pgroonga
    q = text('CREATE EXTENSION pgroonga')
    session = db.Session()
    session.execute(q)
