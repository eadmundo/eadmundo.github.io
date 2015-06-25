from flask import Flask
from flask.ext.blog import FlaskBlog
from flask.ext.webpack import Webpack

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'
app.config['BLOG_FILE_POSTS_FOLDER'] = 'posts'
app.config['WEBPACK_MANIFEST_PATH'] = './build/manifest.json'

blog = FlaskBlog()
blog.init_app(app)

webpack = Webpack()
webpack.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
