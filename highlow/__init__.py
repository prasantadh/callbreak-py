from highlow.HighLow import HighLow

import os
from flask import Flask, request

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'highlow.sqlite'),
            )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    game = HighLow()

    @app.route('/new', methods=['GET'])
    def new():
        global game
        try:
            game = HighLow()
            card = game.new()
            print("game initialization")
        except Exception as err:
            app.logger.error("Error creating a new game.")
            app.logger.error(err)
            return {
                "result" : "failure",
                "data" : {
                    "reason" : "server side failure. contact the developers."
                }
            }
        return {
            "result" : "success",
            "data" : {
                "card" : str(card),
                "score" : 0
            }
        }

    @app.route('/call', methods=['POST'])
    def call():
        global game
        # TODO: insert exception check here
        data = request.get_json()['data']['guess']
        print(data)

        # TODO: check if there is a running game
        # if there is then...
        if data != 'high' and data != 'low':
            return {
                'result' : 'failure',
                'data' : {
                    'reason' : 'invalid call value (allowed: high/low)'
                }
            }
        result = game.call(data)
        if result:
            return {
                'result' : 'success',
                'data' : {
                    'card' : str(game.deal()),
                    'score': game.score
                }
            }
        else:
            return {
                'result' : 'failure',
                'data' : {
                    'reason' : 'failed!'
                }
            }
    return app