from flask import jsonify, session
from models.article import Article
from models import db 



def update_article(id, data):
    article = Article.query.get_or_404(id)
    article.title = data['title']
    article.content = data['content']
    db.session.commit()

    return jsonify({
    'id': article.id, 
    'title': article.title,
    'content': article.content
    })

def delete_article(id):
    if 'user_id' not in session:
        return jsonify({'message': 'No autorizado'}), 401
    
    article = Article.query.get_or_404(id)

    if article.user_id != session['user_id']:
        return jsonify({'message': 'No autorizado para eliminar este articulo'}), 403
    
    try:
        db.session.delete(article)
        db.session.commit()
        return jsonify({'message':f'Articulo eliminado con exito. Selimino {article.title}'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message':'Error al eliminar el articulo', 'error': str(e)}), 500

def get_article(article_id):
    article = Article.query.get_or_404(article_id)
    return jsonify({
    'id': article.id, 
    'title': article.title,
    'content': article.content
    })

def create_article(data, user_id):
    if not user_id:
        return jsonify({'error': 'El usuario no está autenticado o el ID de usuario no está en la sesión'}), 401
    new_article = Article(
       title=data['title'], 
       content=data['content'],
       image_url=data['image_url'],
       user_id = user_id
       )
    db.session.add(new_article)
    db.session.commit()
   
    return jsonify({
    'id': new_article.id, 
    'title': new_article.title,
    'content': new_article.content,
    'image_url': new_article.image_url,
    'author': new_article.author.username

   }), 201

def get_all_articles():
    articles = Article.query.all()
    return jsonify([{
        'id': article.id,
        'title': article.title,
        'content': article.content,
        'image_url': article.image_url,
        'author': article.author.username,
        'created_at': article.created_at.strftime('%d-%m-%Y'),
        'user_id': article.user_id
    } for article in articles])

def toggle_favorite(data, article_id):
    is_favorite = data.get('isFavorite')
   
    article = Article.query.get_or_404(article_id)
    article.is_favorite = is_favorite

    db.session.commit()

    return jsonify({'message': 'Estado de favorito Actualizado'}), 201


def get_favorites(user_id):
    if not user_id:
        return jsonify({'error': 'El usuario no está autenticado o el ID de usuario no está en la sesión'}), 401
    

    favorites_articles = Article.query.filter_by(user_id=user_id, is_favorite=True).all()
    articles_list = [
        {
            'id': article.id,
            'title': article.title,
            'content':article.content,
            'image_url': article.image_url,
            'created_at': article.created_at,
            'is_favorite': article.is_favorite

        } for article in favorites_articles

    ]

    return jsonify(articles_list), 200