from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from Models.db import db
import database_Url as dbu


app = Flask(__name__)
# 'mysql://{0}:{1}@{2}:{3}/{4}'.format(user, pass, host, port, db)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(dbu.user, dbu.password, dbu.host, dbu.port, dbu.DB_NAME)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

# api.add_resource(Store, "/store/<string:name>")
# api.add_resource(StoreList, "/stores")
api.add_resource(Book, "/book/<string:name>")
api.add_resource(BookList, "/books")
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")

if __name__ == '__main__':
    app.run(debug=1)
