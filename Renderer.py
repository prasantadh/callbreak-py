from rich import print
from rich.layout import Layout
from rich.align import Align
from rich.padding import Padding

from utilities import render_empty_card

# In the future, could potentially use the same class for, say a HTML5/JS
# version that uses the same backend.


class Renderer():
    # TODO: Use a better name for platform.
    def __init__(self, platform: str = "terminal"):
        """
        __init__ _summary_

        _extended_summary_

        Keyword Arguments:
            platform -- _description_ (default: {"terminal"})
        """
        self.players = []
        self.platform = platform

    def update_players(self, players):
        """
        update_players _summary_

        _extended_summary_

        Arguments:
            players -- _description_
        """
        self.players = players

    def render_call_break(self):
        """
        render_call_break
        Renders a call break game. The renderer fits whatever the size
        the terminal is unless the terminal window is very small.

        TODO: Auto adjust dimensions on terminal window resize.

        _extended_summary_
        """

        # Sort the player 0's cards so that they appear nice and
        # organized on the deck.
        self.players[0].sortCards(ascending=True)

        # Use rich.Layout objects to write the player 0's name.
        player_name = Layout()
        player_name.split_column(
            Layout(self.players[0].name, name="player_name"),
        )

        # Populate all players' cards.
        # For player 0, get cards from Player() and render that
        # while for the rest, just print generic flipped cards.
        all_players_cards = [[], [], [], []]

        for i in range(13):
            all_players_cards[0].append(self.players[0].getCards()[i].rich_render())

            # Generic pictures for the back of the cards.
            all_players_cards[1].append(render_empty_card(for_across_a_row=False, color="red", text=":mahjong_red_dragon::mahjong_red_dragon:"))
            all_players_cards[2].append(render_empty_card(for_across_a_row=True, color="green", text=":dragon::dragon:"))
            all_players_cards[3].append(render_empty_card(for_across_a_row=False, color="blue", text=":comet::comet:"))

        # Layout the screen into rows and columns.
        # Write the player 0's name on the lowest panel.
        layout = Layout()
        layout.split_column(
            Layout(name="top_padding"),
            Layout(" ", name="upper"),
            Layout(" ", name="middle"),
            Layout(" ", name="lower"),
            Layout(Align.center(self.players[0].name), name="lower_padding")
        )

        # Write the round number on the top-left.
        layout["top_padding"].split_row(
                Layout(Align.left("Round 1 / 5", vertical="bottom"), name="top_left_padding"),
                Layout(Align.center(self.players[2].name, vertical="bottom"), name="top_middle_padding"),
                Layout(" ", name="top_right_padding"),
        )

        # Top row into three columns- middle for player 2's cards.
        layout["upper"].split_row(
            Layout(" ", name="upper_left"),
            Layout(" ", name="upper_middle"),
            Layout(" ", name="upper_right"),
        )

        # Middle row also into three column- player 3's cards, the central part,
        # and player 1's cards.

        layout["middle"].split_row(
            Layout(" ", name="middle_left"),
            Layout(" ", name="middle_middle"),
            Layout(" ", name="middle_right"),
        )

        # Same as for top row but for player 0.

        layout["lower"].split_row(
            Layout(" ", name="lower_left"),
            Layout(" ", name="lower_middle"),
            Layout(" ", name="lower_right"),
        )

        # Populate the lower middle part with player 0's cards.
        # The cards are rendered by Card's method rich_render().
        # For generic cards, we use a utility function from
        # utilities.py.
        layout["lower_middle"].split_row(*all_players_cards[0])

        # Write all the players' cards.
        layout["middle_right"].split_row(
            Layout(" ", name="middle_right_cards"),
            Layout(Align.center(self.players[1].name, vertical="middle"), name="middle_right_player_name")
        )
        layout["middle_right_cards"].split_column(*all_players_cards[1])
        layout["upper_middle"].split_row(*all_players_cards[2])
        layout["middle_left"].split_row(
            Layout(Align.center(self.players[3].name, vertical="middle"), name="middle_left_player_name"),
            Layout(" ", name="middle_left_cards"),
        )

        layout["middle_left_cards"].split_column(*all_players_cards[3])

        # Define size ratios for the layouts.
        layout["top_padding"].ratio = 1
        layout["upper"].ratio = 1
        layout["middle"].ratio = 4
        layout["lower"].ratio = 1

        layout["upper_left"].ratio = 1
        layout["upper_middle"].ratio = 5
        layout["upper_right"].ratio = 1

        layout["middle_left"].ratio = 1
        layout["middle_middle"].ratio = 10
        layout["middle_right"].ratio = 1

        layout["lower_left"].ratio = 1
        layout["lower_middle"].ratio = 5
        layout["lower_right"].ratio = 1

        # print the overall layout.
        print(Padding(layout, (1, 2)))


if __name__ == '__main__':
    pass
