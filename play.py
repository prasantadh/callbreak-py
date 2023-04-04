from highlow.Client import Client as HighLowClient
from callbreak.BasicClient import Client as CallBreakClient
import validators

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('game',
        choices=['callbreak', 'highlow'],
        default='callbreak',
        help="choose a game to play. default is callbreak")
parser.add_argument("--url", 
        required=False,
        default='http://127.0.0.1:5000/',
        help=('server url at which the game is available. '
                'ex. http://127.0.0.1:5000/. full url is expected')
        )

args = parser.parse_args()

if not validators.url(args.url):
    print('Invalid URL! Remember to include http:// or https://')
    exit()

if args.game == 'highlow':
    client = HighLowClient(args.url)
    client.run()

elif args.game == 'callbreak':
    client = CallBreakClient(args.url)
    client.run()