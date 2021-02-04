from flask import Blueprint, render_template, request, jsonify
import os
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)

from .extensions import mongo

main = Blueprint('main', __name__)

secret_key = os.environ.get("SECRET_KEY")


@main.route('/')
def index():
    # user_collection = mongo.db.users
    # user_collection.insert({'name': 'Fenil'})
    return render_template('index.html')


@main.route('/auth', methods=['POST'])
def auth():
    user_collection = mongo.db.users
    dict1 = dict(request.form)
    is_user_exist = user_collection.find_one({"email": dict1['email']})
    if not is_user_exist:
        try:
            user_id = user_collection.insert(dict1)
            ret = {
                'access_token': create_access_token(identity=str(user_id)),
                'refresh_token': create_refresh_token(identity=str(user_id))
            }
            return jsonify(ret), 200
        except Exception as e:
            print(e)
            return {"msg": "Please try again."}

    else:
        try:
            ret = {
                'access_token': create_access_token(identity=str(is_user_exist["_id"])),
                'refresh_token': create_refresh_token(identity=str(is_user_exist["_id"]))
            }
            return jsonify(ret), 200
        except Exception as e:
            print(e)
            return {"msg": "Please try again."}

@main.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200

@main.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # username = get_jwt_identity()
    return render_template('private.html')


