# -*- coding:utf-8 -*-
from flask import Flask
from apis.user import app_user
from apis.product import app_product
from apis.clicks import app_clicks
from flask_cors import CORS  # 跨域问题
from flask_cors import *
from apis.application import app_application
from apis.markdown import app_markdown
from apis.neo4joperation import app_neo4j
from apis.askquestion import app_askquestion
app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(app_user)
app.register_blueprint(app_product)
app.register_blueprint(app_application)
app.register_blueprint(app_markdown)
app.register_blueprint(app_neo4j)
app.register_blueprint(app_clicks)
app.register_blueprint(app_askquestion)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3001)
