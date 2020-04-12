import db.db as db
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Enum
from sqlalchemy.dialects.postgresql import INTEGER, BOOLEAN
from sqlalchemy.orm import relationship
import enum


Base = db.Base


class Author(Base):
    """
    Author Table

    id : ID
    name : Name
    """
    __tablename__ = 'author'
    id = Column(
        'id',
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )
    name = Column('name', String, nullable=False)


class Publisher(Base):
    """
    Publisher Table

    id : ID
    name : Publisher name
    """
    __tablename__ = 'publisher'
    id = Column(
        'id',
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )
    name = Column('name', String, nullable=False)


class BaseBook(Base):
    """
    Base Book Table

    id : ID
    title : Title
    author : Author
    bio : BIO/まえがき
    pub_date : Date of Publication

    isbn13 : ISBN-13 code
    isbn10 : ISBN-10 code
    issn : ISSN code
    ean : EAN/JAN code
    doi : Digital Object Identifier
    zasshi : Japanese Magazine Code http://jpo.or.jp/magcode/info/outline.html

    publisher : Publisher
    """
    __tablename__ = 'basebook'
    id = Column(
        'id',
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )
    title = Column('title', String, nullable=False)
    author_id = Column(INTEGER, ForeignKey('author.id'),
                       nullable=True)  # null -> unknown author
    author = relationship('Author')
    bio = Column('bio', String)
    pub_date = Column('pub_date', DateTime, nullable=False)

    isbn13 = Column('isbn13', INTEGER, nullable=True)
    isbn10 = Column('isbn10', INTEGER, nullable=True)
    issn = Column('issn', INTEGER, nullable=True)
    ean = Column('ean', INTEGER, nullable=True)
    doi = Column('doi', String, nullable=True)
    zasshi = Column('zasshi', INTEGER, nullable=True)

    publisher_id = Column(INTEGER, ForeignKey(
        'publisher.id'), nullable=True)  # null -> unknown publisher
    publisher = relationship('Publisher')


class UserBookState(enum.Enum):
    UNUSED = 0
    USED_CLEAN = 1
    USED_GOOD = 2
    USED_WITH_WRITING = 3
    USED_BAD = 4


class UserBook(Base):
    """
    Book lent by users

    id : ID
    base_book : Base Book
    pt : Book Point
    description : Description of the state of the book
    """
    __tablename__ = "userbook"
    id = Column(
        'id',
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )
    base_book_id = Column(INTEGER, ForeignKey('basebook.id'), nullable=False)
    base_book = relationship('BaseBook')
    pt = Column('pt', INTEGER, nullable=False)
    state = Column('state', Enum(UserBookState))
    description = Column('description', String, nullable=True)
