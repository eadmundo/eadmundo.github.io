from flask.ext.kitchensink import app
from flask.ext.blog import FlaskBlog

blog = FlaskBlog()

app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False

blog.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
