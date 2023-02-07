from rich import print
from rich.layout import Layout
from rich.align import Align
from rich.padding import Padding
from rich.live import Live
# from rich.console import Console
from utilities import render_empty_card
import random
from pynput import keyboard

# In the future, could potentially use the same class for, say a HTML5/JS
# version that uses the same backend.

# console = Console()


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
        self.highlighted_card = -1  # Which card is highlighted (to indicate the card that would be played next).
        self.number_of_cards_per_player = 13

        self.which_players_turn = 0

        # List where the jth element holds card player j played
        # in current hand.
        self.card_index_played_on_current_hand = None

        self.quit_render = False

    def on_press(self, key):
        """
        on_press Respond to key presses.

        _extended_summary_

        Arguments:
            key -- _description_
        """
        # Move the card highlight to left.
        if key == keyboard.Key.left:
            self.highlighted_card = max((self.highlighted_card - 1)
                                        % (self.players[0])
                                        .getNumberOfRemainingCards(), 0)
        # Move the card highlight to right.
        elif key == keyboard.Key.right:
            self.highlighted_card = min((self.highlighted_card + 1)
                                        % self.players[0]
                                        .getNumberOfRemainingCards(),
                                        self.players[0]
                                        .getNumberOfRemainingCards())
        # Play the current card.
        elif key == keyboard.Key.enter:
            if self.highlighted_card > -1:
                self.card_index_played_on_current_hand[0] \
                    = self.highlighted_card

        self.live.update(self.render_call_break())

    def update_players(self, players):
        """
        update_players _summary_

        _extended_summary_

        Arguments:
            players -- _description_
        """
        self.players = players
        self.card_index_played_on_current_hand = \
            [-1 for i in range(len(self.players))]

    # def play_other_players_turn(self):
    #     if self.which_players_turn != 0:
    #         card_to_play = random.sample(self.players[self.which_players_turn].getCards())
    #         self.card_index_played_on_current_hand[self.which_players_turn] = self.players[self.which_players_turn].index(card_to_play)
    #         # console.log("Playing another player's turn.")

    #         # console.log(self.card_index_played_on_current_hand)

    #         exit(-1)

    def get_card_played_on_current_hand(self, player_id: int):
        """
        get_card_played_on_current_hand Return card that's been played on
        current hand.

        While it's still a player's turn (as indicated by not having
        selected the card and then pressed Enter), this is used
        to mark which card appears as selected card.

        _extended_summary_

        Arguments:
            player_id -- player index

        Returns:
            _description_
        """
        # The placeholder below is a single-space-string instead of something
        # like None because if you make it None,
        # rich shows dimensions of the grid instead.

        card_id = self.card_index_played_on_current_hand[player_id]
        if card_id < 0:
            return " "
        return self.players[player_id].getCards()[card_id].rich_render()

    def should_render_card(self, player_index: int, card_index: int) -> bool:
        """
        should_render_card Decides whether or not the current card
        needs to be rendered. This basically is a safety check to 
        not cause an overflow.

        _extended_summary_

        Arguments:
            player_index -- _description_
            card_index -- _description_

        Returns:
            _description_
        """
        return card_index < \
            self.players[player_index].getNumberOfRemainingCards()

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
        self.players[0].sortCards(ascending=False)

        # Use rich.Layout objects to write the player 0's name.
        player_name = Layout()
        player_name.split_column(
            Layout(self.players[0].name, name="player_name"),
        )

        # Populate all players' cards.
        # For player 0, get cards from Player() and render that
        # while for the rest, just print generic flipped cards.
        all_players_cards = [[], [], [], []]

        for i in range(self.number_of_cards_per_player):
            
            if self.should_render_card(0, i):
                # Checking if we should highlight the current card
                # as the card that would be played next.
                highlight_card = (self.highlighted_card >= 0) and \
                    (self.highlighted_card < self.number_of_cards_per_player) \
                    and (i == self.highlighted_card)

                # Decide whether to render an empty placeholder
                # for where the highlighted card would have been
                # or a regular card.
                if self.card_index_played_on_current_hand[0] != i:
                    current_player_current_card = \
                        self.players[0].getCards()[i].rich_render(highlight_card)
                else:
                    current_player_current_card = \
                        render_empty_card(for_across_a_row=True, 
                                          width=8,
                                          height=6,
                                          color="#333333"
                                          )

                all_players_cards[0].append(current_player_current_card)

            # Generic pictures for the back of the cards.
            if self.should_render_card(1, i):
                all_players_cards[1].append(render_empty_card(
                                                for_across_a_row=False,
                                                color="white",
                                                text=":dragon::dragon:"
                                                ))
            if self.should_render_card(2, i):
                all_players_cards[2].append(render_empty_card(
                                                for_across_a_row=True,
                                                color="white",
                                                text=":dragon::dragon:"
                                                ))
            if self.should_render_card(3, i):
                all_players_cards[3].append(render_empty_card(
                                                for_across_a_row=False,
                                                color="white",
                                                text=":dragon::dragon:"
                                                ))

        # Layout the screen into rows and columns.
        # Write the player 0's name on the lowest panel.
        layout = Layout()
        layout.split_column(
            Layout(name="top_padding"),
            Layout(name="upper"),
            Layout(name="middle"),
            Layout(name="lower"),
            Layout(Align.center(self.players[0].name), name="lower_padding")
        )

        # Write the round number on the top-left.
        layout["top_padding"].split_row(Layout(Align.left("Turn: " + str(self.players[self.which_players_turn].name), vertical="bottom"), name="top_left_padding"),
                Layout(Align.center(self.players[2].name, vertical="bottom"), name="top_middle_padding"),
                Layout(" ", name="top_right_padding"),
        )

        # Top row into three columns- middle for player 2's cards.
        layout["upper"].split_row(
            Layout(" ", name="upper_left"),
            Layout(" ", name="upper_middle"),
            Layout(" ", name="upper_right"),
        )

        # Middle row also into three column- player 3's cards, the central 
        # part, and player 1's cards.

        layout["middle"].split_row(
            Layout(name="middle_left"),
            Layout(name="middle_middle"),
            Layout(name="middle_right"),
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

        layout["middle_middle"].split_column(
            Layout(" ", name="middle_middle_0"),
            Layout(" ", name="middle_middle_1"),
            Layout(" ", name="middle_middle_2")
        )

        layout["middle_middle_0"].split_row(
            Layout(" ", name="middle_middle_1_0"),
            Layout(" ", name="middle_middle_1_1"),
            Layout(" ", name="middle_middle_1_2"),
        )

        layout["middle_middle_1"].split_row(
            Layout(" ", name="middle_middle_2_0"),
            Layout(" ", name="middle_middle_2_1"),
            Layout(" ", name="middle_middle_2_2"),
        )

        layout["middle_middle_2"].split_row(
            Layout(" ", name="middle_middle_3_0"),
            # Layout(Align.center(all_players_cards[0][0], vertical="top"), name="middle_middle_3_1"),
            Layout(Align.center(self.get_card_played_on_current_hand(0), vertical="top"), name="middle_middle_3_1"),
            Layout(" ", name="middle_middle_3_2"),
        )

        # Write all the players' cards.
        layout["middle_right"].split_row(
            Layout(" ", name="middle_right_cards"),
            Layout(Align.center(self.players[3].name, vertical="middle"), name="middle_right_player_name")
        )
        layout["middle_right_cards"].split_column(*all_players_cards[1])
        layout["upper_middle"].split_row(*all_players_cards[2])
        layout["middle_left"].split_row(
            Layout(Align.center(self.players[1].name, vertical="middle"), name="middle_left_player_name"),
            Layout(" ", name="middle_left_cards"),
        )

        layout["middle_left_cards"].split_column(*all_players_cards[3])

        # Define size ratios for the layouts.
        layout["top_padding"].ratio = 1
        layout["upper"].ratio = 1
        layout["middle"].ratio = 8
        layout["lower"].ratio = 2

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

    def render_live(self):
        """
        render_live Render the board where we update it
        whenever something changes (like a card being
        played for example).

        _extended_summary_
        """

        # Listener to listen for keyboard presses.
        listener = keyboard.Listener(
            on_press=self.on_press
        )
        listener.start()

        with Live(self.render_call_break(), screen=True, auto_refresh=False) as self.live:
            while not self.quit_render:
                self.render_call_break()

                # if self.quit_render:
                #     self.live.stop()


if __name__ == '__main__':
    pass
