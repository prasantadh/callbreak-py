# callbreak

## Instalation
```
cd
apt update
apt install git pip
pip install --target callbreak git+https://github.com/prasantadh/callbreak.git@highlow
```

## Usage
When you are on the topmost level,

```bash
cd callbreak
# run the server
PYTHONPATH=~/callbreak bin/flask --app highlow --debug run
# start the client and play
python3 play.py highlow
```

## Testing
Testing will require you to download the source fully,
then set up your own environment (WIP: Details on "how").

```bash
python -m unittest discover test
```

Consult the `highlow/api.md` for the api on playing HighLow.

An example on how to interact with the server is provided at `highlow/Client.py`.
This version uses our renderer. You are welcome to bring your own to the game ;)
