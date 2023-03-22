from highlow.Client import Client as HighLowClient

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("game",
        choices=["callbreak", "highlow"],
        help="choose a game to play")

args = parser.parse_args()

if args.game == 'highlow':
    client = HighLowClient()
    client.run()


