from highlow.HighLow import HighLow
from highlow.schema import call_schema

import os
from flask import Flask, request
import jsonschema

game = HighLow()

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

    @app.route('/new', methods=['GET'])
    def new():
        global game
        try:
            card = game.new()
        except Exception as err:
            app.logger.error("Error creating a new game.")
            app.logger.error(err)
            return {
                "result" : "failure",
                "data" : {
                    "reason" : "server side failure. contact the developers."
                }
            }
        app.logger.info(game.peek_next_card())
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
        if not game or not game.isOn:
            return {
                'result' : 'failure',
                'data' : {
                    'reason' : "game isn't initialized. request a /new game"
                }
            }

        try:
            incoming = request.get_json()
            jsonschema.validate(incoming, call_schema)
        except Exception as E:
            return {
                'result' : 'failure',
                'data' : {
                    'reason' : 'received invalid data format'
                }
            }
        guess = incoming['data']['guess']

        result = game.call(guess)
        card = game.deal()
        app.logger.info(game.peek_next_card())
        
        if result:
            return {
                'result' : 'correct',
                'data' : {
                    'card' : str(card),
                    'score': game.score
                }
            }

        return {
            'result' : 'incorrect',
            'data' : {
                'card' : str(game.peek_next_card()),
                'score': game.score
            }
        }
    
    @app.route('/status', methods=['GET'])
    def status():
        global game
        if not game or not game.isOn:
            return {
                'result' : 'failure',
                'data' : {
                    'reason' : "game isn't initialized. request a /new game"
                }
            }
        app.logger.info(game.peek_next_card())
        return {
            'result' : 'success',
            'data' : {
                'card' : str(game.last_dealt()),
                'score' : game.score
            }
        }
    return app