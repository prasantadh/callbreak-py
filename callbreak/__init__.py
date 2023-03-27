from callbreak.CallBreak import CallBreak
from commons.Player import Player

from commons.exceptions.CallbreakExceptions import GameIsNotOnError

import os
from flask import Flask

game = CallBreak()

def respond_failure(err):
    return {
        'result' : 'failure',
        'data' : {
            'reason' : str(err)
        }
    }

def respond_success():
    return {
        'result' : 'success',
        'data' : {
            'players' : game.player_names,
            'calls' : game.calls,
            'scores' : game.scores
        }
    }

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
        if not game.isOn:
            return game.respond_failure('No running game! Request a /new game.')
        
        return game.respond_success()


    @app.route('/new/<name>', methods=['GET'])
    def new(name):
        global game
        try:
            game.new()
            game.addPlayer(Player(name, game))
            game.addPlayer(Player('1', game))
            game.addPlayer(Player('2', game))
            game.addPlayer(Player('3', game))

        except Exception as err:
            app.logger.error(err)
            return respond_failure(err)

        return respond_success()
    
    @app.route('/call', methods=['POST'])
    def call():
        global game
        try:
            if not game or not game.isOn:
                raise GameIsNotOnError
            for player in game.players:
                player.call(1)
        except Exception as err:
            app.logger.error(err)
            respond_failure(err)
        
        return respond_success()
        

    return app
