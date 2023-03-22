# callbreak

When you are on the topmost level, to run the server

```bash
# run the server
flask --app highlow --debug run
# start the client and play
python3 play.py highlow

## run a test
python -m unittest test.commons.test_card
```

Consult the `highlow/api.md` for the api on playing callbreak.
An example on how to interact with the server is provided at `highlow/Client.py`.
This version uses our renderer. You are welcome to bring your own to the game ;)
