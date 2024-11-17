from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .article import Article

__all__ = ['User', 'Article']
