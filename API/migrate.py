from db import db
from user import models
from book import models


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
