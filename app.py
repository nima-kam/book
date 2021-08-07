from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)


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

