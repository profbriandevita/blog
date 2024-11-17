from flask import Blueprint, request, jsonify, session
from services.article_service import get_article,  delete_article,update_article, create_article,get_all_articles, get_favorites, toggle_favorite

bp = Blueprint('articles',__name__)



# Actualizamos un articulo
@bp.route('/articles/<int:id>', methods=['PUT'])
def update_article_route(id):
    data = request.get_json()
    return update_article(id, data)


# Eliminamos un articulo
@bp.route('/articles/<int:id>', methods=['DELETE'])
def delete_article_route(id):
    return delete_article(id)



# Obtenemos un Articulo
@bp.route('/article/<int:article_id>', methods=['GET'])
def view_article_route(article_id):
    return get_article(article_id)


# Creamos un articulo
@bp.route('/articles', methods=['POST'])
def create_article_route():
   data = request.get_json()
   user_id = session.get('user_id')
   return create_article(data, user_id)



# Obtenemos todos los articulos
@bp.route('/articles', methods=['GET'])
def get_articles_route():
   return get_all_articles()





@bp.route('/favorites/<int:article_id>', methods=['POST'])
def toggle_favorite_route(article_id):
   
    data = request.get_json()
 
    return toggle_favorite(data, article_id)


@bp.route('/favorites', methods=['GET'])
def get_favorites_route():
    user_id = session.get('user_id')
    
    return get_favorites(user_id)

