import db.db as db
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import INTEGER, BOOLEAN
from sqlalchemy.orm import relationship


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


class Book(Base):
    """
    Book Table

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
    __tablename__ = 'book'
    id = Column(
        'id',
        INTEGER,
        primary_key=True,
        autoincrement=True,
    )
    title = Column('title', String, nullable=False)
    author_id = Column(INTEGER, ForeignKey('author.id'), nullable=True)  # null -> unknown author
    author = relationship('Author')
    bio = Column('bio', String)
    pub_date = Column('pub_date', DateTime, nullable=False)
    
    isbn13 = Column('isbn13', INTEGER, nullable=True)
    isbn10 = Column('isbn10', INTEGER, nullable=True)
    issn = Column('issn', INTEGER, nullable=True)
    ean = Column('ean', INTEGER, nullable=True)
    doi = Column('doi', String, nullable=True)
    zasshi = Column('zasshi', INTEGER, nullable=True)
    
    publisher_id = Column(INTEGER, ForeignKey('publisher.id'), nullable=True)  # null -> unknown publisher
    publisher = relationship('Publisher')
