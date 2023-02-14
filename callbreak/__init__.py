import os
from flask import Flask


# from CallBreak import CallBreak       # This imports the "player's" CallBreadk class instead.
from callbreak.CallBreak import CallBreak
from callbreak.commons.Player import Player


# print(CallBreak)



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
            app.logger.error("Error retrieving status.")
            app.logger.error(err)
            return { 'result' : 'failure' }
            
        return

    @app.route('/new/<name>', methods=['GET'])
    def new(name):
        global game
        try:
            game = CallBreak()
            game.addPlayer(Player(name))
            game.play()

            app.logger.info(game.status())
            return {
                    'result' : 'success'
                    }
        except Exception as err:
            app.logger.error("Error creating a new game.")
            app.logger.error(err)
            print(err)

        return

    return app
