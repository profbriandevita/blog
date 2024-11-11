
from datetime import datetime
from models import db



# Modelo 
class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    is_favorite = db.Column(db.Boolean, default=False,  nullable=False)


    def __repr__(self):
        return f'<Article {self.title}>'