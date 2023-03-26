from callbreak.CallBreak import CallBreak
from commons.Player import Player

import os
from flask import Flask

game = CallBreak()
def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'callbreak.sqlite'),
            )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/status')
    def status():
        global game
        try:
            return game.status()
        except Exception as err:
            app.logger.error(err)
            return { 
                'result' : 'failure', 
                'data' : {
                    'reason' : 'Failure retrieving status'
                }
            }

    @app.route('/new/<name>', methods=['GET'])
    def new(name):
        global game
        try:
            game = CallBreak()
            game.addPlayer(Player(name), game)
            game.addPlayer(Player('1'), game)
            game.addPlayer(Player('2'), game)
            game.addPlayer(Player('3'), game)
            app.logger.info(game.status())

        except Exception as err:
            app.logger.error(err)
            game.respond_failure(err)

        return game.respond_success()
    
    @app.route('/call', methods=['POST'])
    def call():
        global game
        try:
            for player in game.get_players()[1:]:
                player.set_calls(1)
        except Exception as err:
            app.logger.err(err)
            game.respond_failure(err)
        

    return app
