from eadmundo import app
from flask import current_app
from flask.ext.script import Manager
from flask.ext.frozen import Freezer

manager = Manager(app)


@manager.command
def freeze():
    freezer = Freezer(current_app)
    freezer.freeze()


@manager.command
def serve_frozen():
    freezer = Freezer(current_app)
    freezer.serve(host='0.0.0.0')

if __name__ == "__main__":
    manager.run()
