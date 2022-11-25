# from flask import Flask
# from src.database.database import init_app
#
# # import the controllers
#
# app = Flask(__name__)
#
# # setup config
# app.config.from_object('config.DevelopmentConfig')
#
# # initialize the database
# init_app(app)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

from src import init_app

app = init_app()


if __name__ == '__main__':
    app.run(debug=True)
