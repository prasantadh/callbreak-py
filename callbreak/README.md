# Rules

## Objective of the Game
Be the player with the highest score at the end of the game.

## Generics
- The game is played with a standard deck of 52 cards.
- A game is played for 5 rounds with 4 players.
- The game proceeds clockwise at all times.
- A call is the estimated number of tricks you will win. You make
this estimate after you have seen your cards and before each round starts.
- Each player gets 13 cards at the start of the game and hence,
a round is a collection of 13 tricks.

```txt
Glossary:
Hand: The cards that a player has.
Trick: A collection of 4 cards played face up from each player.

In Nepali, these would both be called _haat_.
```

## Game Play
- The dealer deals all the cards starting with the person immediately
to her left.
- Eldest Hand (the player who was given the first card) of the round
calls first.  Others call clockwise. Eldest Hand plays first card of 
the first trick in each round.
- In a trick, the trump suit wins all other suits. You can only play
a trump suit card if you are the first to play on a trick or if you
are out of the suit that was the first card played on current trick.
- In absence of trump cards, the first suit in a trick is the
winning suit for that trick.
- If you have a card that is greater than any card played in the
trick so far, you must play that card.
- The player to win the trick, starts the next trick.

## Termination
- Each extra trick won will give you .1 points.
If estimated number of tricks aren't won, you get a negative of the
estimation for that round.
- After 5 rounds, the score is totalled. The player with the highest
score wins.

# API

This document details the API interactions between the game server
and the player.

The response will always be in the format
```json
{
    "result": "success/failure",
    "data" : {"relevant data on success",
                "reason on failure"}
}
```

## Request Endpoints

Name                     | Description
-------------------------|--------------------------------------
`break`  | Only valid at relevant points in the game. Request `data = {'<suit><rank>'}`. This would be equivalent to playing the card. |
`call`   | Only valid at relevant points in the game. Request `data = {'<int-call-value>'}`
`get`     | Get card played in a round by a player at a move. Request `data = {'round' : '1-5', 'player' = '1-4', break = '0-13'}`. Response is in the form `data = {'<suit><rank>'}` which is say the player played that card. To get the hand that a player was dealt at the beginning of the round use `break=0`; only applicable if the requester is also the player being queried
`new`     | Restart a game. In doing so, your last game will no longer exist. `http://127.0.0.1:5000/new`. No `data` returned.
`status` | Return last played `data = {'round' : '1-5', 'player' = '1-4', break = '0-13'}`. The format is the same as is used for sending data to the `get` endpoint. `
`score` | Valid at any point in the game. `data` is ignored for requests. Returns `data = {[ _ , _ , _ , _ ], [....], [....], [....], [....]}`. The scores are ordered by rounds and players. The dealer in the first round is the first player in all reporting. The score is reported imagining a counterclockwise arrangement from the first player.
