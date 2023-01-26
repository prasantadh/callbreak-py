import os
from flask import Flask

from .CallBreak import CallBreak
from .commons.Player import Player

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'callbreak.sqlite'),
            )

    if test_config is None:
        app.config.from_pyfile('./config.py', silent=False)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    game = None
    @app.route('/status')
    def status():
        global game
        try:
            return game.status()
        except Exception as err:
            return { 'result' : 'failure' }

    @app.route('/new/<name>', methods=['GET'])
    def new(name):
        global game
        try:
            game = CallBreak()
            game.addPlayer(name)
            game.play()
            return {
                    'result' : 'success'
                    }
        except Exception as err:
            print(err)

        return

    return app
