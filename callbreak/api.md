# API

This document details the API interactions between the game server
and the player.

## Request Endpoints

Name                     | Description
-------------------------|--------------------------------------
new     | Restart a game. In doing so, your last game will no longer exist.  `http://127.0.0.1:5000/new`
status  | Get the status of your current game. `http://127.0.0.1:5000/status`
play    | Play a card from your hand onto the table. Include the suit and rank you want to play `http://127.0.0.1/play?suit=Hearts&rank=A`


## Response Values

Name        |  Description
------------|-----------------------------------------------------
status      | Specifies if the request was successfully executed. Returns `success` or `fail`. If it fails, `data` returns an explanation.
data        | Contains response data with includes `hand` : the cards that the current player has at hand
