#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/rhrmx/3282012_challenge_32_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/032e.py

| **Challenge name:** Roulette (reddit_, source_)
| **Challenge number:** 32
| **Difficulty:** Easy
| **Submission date:** 2012-03-28
| **Status:** Complete

Description
-----------

Let's simulate a roulette wheel!

A program that takes as input your bet, and gives as output how much you won, with the
appropriate probability.

Write a program that will take a players bet and output the resulting spin and payout.
Try using an american roulette wheel (which has the 00 slot) to add a slight twist, and
try to incorporate as many complex bets as you can. A comprehensive list can be found
`here <http://en.wikipedia.org/wiki/Roulette#Bet_odds_table>`_.

Thanks to SleepyTurtle for the challenge at `/r/dailyprogrammer_ideas <http://www.reddit.com/r/dailyprogrammer_ideas>`_

Example run
-----------

::

    $ python3 dailyprogrammer.py 032e
    Amount of players: 1
    Enter information for player 1:
    New player name: John
    Starting credits for John: 2000
    Goal for John: 2100

            ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
            │top│d1 │d2 │d3 │d4 │d5 │d6 │d7 │d8 │d9 │d10│d11│
          ┌─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┐
          │row│s1 │s2 │s3 │s4 │s5 │s6 │s7 │s8 │s9 │s10│s11│s12│
          └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
    ┌───┐ ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ┌───┐
    │ba3│ │00 │r3 │b6 │r9 │r12│b15│r18│r21│b24│r27│r30│b33│r36│ │c3 │
    ├───┤ │   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ├───┤
    │ba2│ ├───┤b2 │r5 │b8 │b11│r14│b17│b20│r23│b26│b29│r32│b35│ │c2 │
    ├───┤ │   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ├───┤
    │ba1│ │0  │r1 │b4 │r7 │b10│b13│r16│r19│b22│r25│b28│b31│r34│ │c1 │
    └───┘ └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ └───┘
              ┌───────────────┬───────────────┬───────────────┐
              │     1st12     │     2nd12     │     3rd12     │
              ├───────┬───────┼───────┬───────┼───────┬───────┤
              │ 1-18  │  even │  red  │ black │  odd  │ 19-36 │
              └───────┴───────┴───────┴───────┴───────┴───────┘
    split/corner: provide numbers (in order) joined with '+' (e.g. 'r1+b2')
    bet: join value and position with ',' (e.g. '1,r1+b2')
    multiple bets: join bets with ';' (e.g. '1,r1+b2;1,c1;1,even')

    John, it's your turn! You have 2000 credits, your goal is 2100 credits.
    Place your bet(s): 2000,r1+b2+r7+b8
    Invalid bet position: 'r1+b2+r7+b8'
    Try again: 1000,r1+b2+b4+r5;1000,red
    This is the interpretation of your bet(s):
    - Bet of 1000 credits in position 'r1+b2+b4+r5':
        Pays out 8000 credits if won.
        Odds for winning this bet are 4 against 34.
    - Bet of 1000 credits in position 'red':
        Pays out 1000 credits if won.
        Odds for winning this bet are 18 against 20.

    <DRAWING OF ROULETTE TABLE>

    All players have placed their bets!
    Press [ENTER] to spin the wheel!
    The winning number is: 'r21'

    John, let's see how you did...
    Your bet of 1000 credits in position 'r1+b2+b4+r5' is lost... You lose 1000 credits.
    Your bet of 1000 credits in position 'red' is won! You gain 1000 credits.
    John, that was it for you. You now have 2000 credits.

    All bets have been evaluated!

    <DRAWING OF ROULETTE TABLE>

    John, it's your turn! You have 2000 credits, your goal is 2100 credits.
    Place your bet(s): 2000,red
    This is the interpretation of your bet(s):
    - Bet of 2000 credits in position 'red':
        Pays out 2000 credits if won.
        Odds for winning this bet are 18 against 20.

    <DRAWING OF ROULETTE TABLE>

    All players have placed their bets!
    Press [ENTER] to spin the wheel!
    The winning number is: 'r27'

    John, let's see how you did...
    Your bet of 2000 credits in position 'red' is won! You gain 2000 credits.
    John, that was it for you. You now have 4000 credits.

    All bets have been evaluated!
    Congratulations John, you have reached your goal!

Module contents
---------------

| *var* challenges.032e.\ **rnrs** *(list(str, ...))*
|     list containing all numbers of an American roulette wheel

| *var* challenges.032e.\ **p2w** *(dict(str: list(str, ...), ...))*
|     dictionary mapping positions on an American roulette table to the associated winning numbers
"""

import random

# Numbers on an American roulette wheel.
rnrs = '0 00 r1 b2 r3 b4 r5 b6 r7 b8 r9 b10 b11 r12 b13 r14 b15 r16 b17 r18 r19 b20 '
rnrs += 'r21 b22 r23 b24 r25 b26 r27 b28 b29 r30 b31 r32 b33 r34 b35 r36'
rnrs = rnrs.split()

# Map all possible bet positions to the related winning numbers.
p2w = {nr: [nr] for nr in rnrs}  ## Individual numbers.
p2w.update({  ## Some of the out-of-board positions.
    '1st12': rnrs[2:14],
    '2nd12': rnrs[14:26],
    '3rd12': rnrs[26:],
    '1-18': rnrs[2:20],
    '19-36': rnrs[20:],
    'row': rnrs[:2],
    'top': rnrs[:5],
    'even': [nr for nr in rnrs[2:] if int(nr[1:])%2 == 0],
    'odd': [nr for nr in rnrs[2:] if int(nr[1:])%2 == 1],
    'red': [nr for nr in rnrs if 'r' in nr],
    'black': [nr for nr in rnrs if 'b' in nr],
    'c1': [nr for nr in rnrs[2:] if int(nr[1:])%3 == 1],
    'c2': [nr for nr in rnrs[2:] if int(nr[1:])%3 == 2],
    'c3': [nr for nr in rnrs[2:] if int(nr[1:])%3 == 0],
    'ba1': ['0', 'r1', 'b2'],
    'ba2': ['0', '00', 'b2'],
    'ba3': ['00', 'b2', 'r3'],
})
for ii in range(12):  ## Streets and vertical splits.
    p2w['s{}'.format(ii+1)] = rnrs[2+ii*3:5+ii*3]  ## Street.
    split1 = rnrs[2+ii*3:4+ii*3]  ## First vertical split.
    p2w['+'.join(split1)] = split1
    split2 = rnrs[3+ii*3:5+ii*3]  ## Second vertical split.
    p2w['+'.join(split2)] = split2
for ii in range(11):  ## Double streets, horizontal splits and corners.
    p2w['d{}'.format(ii+1)] = rnrs[2+ii*3:8+ii*3]  ## Double street.
    split1 = [rnrs[jj+ii*3] for jj in [2, 5]]  ## First horizontal split.
    p2w['+'.join(split1)] = split1
    split2 = [rnrs[jj+ii*3] for jj in [3, 6]]  ## Second horizontal split.
    p2w['+'.join(split2)] = split2
    split3 = [rnrs[jj+ii*3] for jj in [4, 7]]  ## Third horizontal split.
    p2w['+'.join(split3)] = split3
    corner1 = [rnrs[jj+ii*3] for jj in [2, 3, 5, 6]]  ## First corner.
    p2w['+'.join(corner1)] = corner1
    corner2 = [rnrs[jj+ii*3] for jj in [3, 4, 6, 7]]  ## Second corner.
    p2w['+'.join(corner2)] = corner2


class RouletteBet(object):
    """A class representing a bet in a game of roulette.

    A roulette bet is characterized by the value of the bet, and the position of the bet on the
    roulette table. A roulette bet is initialized by providing a string with both parts joined
    with a comma character (see example). The value must be a positive integer and the position
    must be valid on the table. Initializing an invalid bet is possible, but in that case almost
    all methods will simply return None instead of the expected value.

    :param str raw: raw representation of the bet, i.e. the value and position joined with a comma

    Example::

        >>> print(RouletteBet('2red'))
        Invalid bet: 2red
        >>> print(RouletteBet('notaninteger,red'))
        Invalid bet: notaninteger,red
        >>> print(RouletteBet('-2,red'))
        Invalid bet: -2,red
        >>> print(RouletteBet('2,invalidposition'))
        Invalid bet: 2,invalidposition
        >>> print(RouletteBet('2,red'))
        - Bet of 2 credits in position 'red':
            Pays out 2 credits if won.
            Odds for winning this bet are 18 against 20.
    """


    def __init__(self, raw):
        """Create a new roulette bet."""
        self.raw = raw


    def __str__(self):
        """Format the roulette bet as a string."""
        if not self.is_valid():
            return "Invalid bet: {}".format(self.raw)
        str_ = "- Bet of {} credits in position '{}':\n".format(self.value(), self.position())
        str_ += "    Pays out {} credits if won.\n".format(self.payout())
        str_ += "    Odds for winning this bet are {}.".format(self.odds_for())
        return str_


    def process(self, verbose=False):
        """Process the raw roulette bet by attempting to determine value and position.

        If wanted, the method can be made verbose so extra information concerning why a roulette bet is
        invalid is printed.

        :param bool verbose: set to True to print more information concerning invalidity (default False)
        :return: tuple consisting of bet value and position or None if bet is invalid
        :rtype: (int, str) or None

        Example::

            >>> RouletteBet('invalidbet').process(verbose=True)
            Invalid raw bet input: 'invalidbet'
            >>> RouletteBet('-2,red').process(verbose=True)
            Bet value must be higher than zero, got: -2
            >>> RouletteBet('2,red').process()
            (2, 'red')
        """
        # Split value of bet from its position on the table.
        try:
            value, position = self.raw.split(',')
        except:
            if verbose:
                print("Invalid raw bet input: '{}'".format(self.raw))
            return
        # Evaluate value.
        try:
            value = int(value)
        except:
            if verbose:
                print("Invalid bet value: '{}'".format(value))
            return
        if value <= 0:
            if verbose:
                print("Bet value must be higher than zero, got: {}".format(value))
            return
        # Evaluate position.
        if position not in p2w:
            if verbose:
                print("Invalid bet position: '{}'".format(position))
            return
        return value, position


    def is_valid(self, verbose=False):
        """Return a boolean indicating whether or not the roulette bet is valid.

        If wanted, the method can be made verbose so extra information concerning why a roulette bet is
        invalid is printed.

        :param bool verbose: set to True to print more information concerning invalidity (default False)
        :return: True if the roulette bet is valid, False otherwise
        :rtype: bool

        Example::

            >>> RouletteBet('invalidbet').is_valid()
            False
            >>> RouletteBet('2,red').is_valid()
            True
        """
        return not (self.process(verbose=verbose) is None)


    def value(self):
        """Get the value of the roulette bet.

        :return: the value of the bet or None if the bet is invalid
        :rtype: int or None

        Example::

            >>> RouletteBet('2,red').value()
            2
        """
        if not self.is_valid():
            return
        return self.process()[0]


    def position(self):
        """Get the position of the roulette bet.

        :return: the position of the bet or None if the bet is invalid
        :rtype: str or None

        Example::

            >>> RouletteBet('2,red').value()
            'red'
        """
        if not self.is_valid():
            return
        return self.process()[1]


    def winning_numbers(self):
        """Get the winning numbers associated with the position of the roulette bet.

        :return: the list of winning roulette wheel numbers associated with the table position of
                 the bet or None if the bet is invalid
        :rtype: list(str, ...) or None

        Example::

            >>> RouletteBet('2,r1+b2+b4+r5').winning_numbers()
            ['r1', 'b2', 'b4', 'r5']s
            >>> RouletteBet('2,c1').winning_numbers()
            ['r1', 'b4', 'r7', 'b10', 'b13', 'r16', 'r19', 'b22', 'r25', 'b28', 'b31', 'r34']
        """
        if not self.is_valid():
            return
        return p2w[self.position()]


    def payout(self):
        """Get the amount of credits that would be paid out if the bet is won.

        :return: the payout if the bet is won or None if the bet is invalid
        :rtype: int or None

        Example::

            >>> RouletteBet('2,r1+b2+b4+r5').payout()
            16
        """
        if not self.is_valid():
            return
        return self.value()*(36//len(self.winning_numbers())-1)


    def odds_for(self):
        """Determine the odds for winning the bet.

        :return: the odds for winning the bet or None if the bet is invalid
        :rtype: str or None

        Example::

            >>> RouletteBet('2,r1+b2+b4+r5').odds_for()
            '4 against 34'
        """
        if not self.is_valid():
            return
        nf = len(self.winning_numbers())
        na = len(rnrs) - nf
        return '{} against {}'.format(nf, na)


    def odds_against(self):
        """Determine the odds against winning the bet.

        :return: the odds against winning the bet or None if the bet is invalid
        :rtype: str or None

        Example::

            >>> RouletteBet('2,r1+b2+b4+r5').odds_against()
            '34 against 4'
        """
        if not self.is_valid():
            return
        nf = len(self.winning_numbers())
        na = len(rnrs) - nf
        return '{} against {}'.format(na, nf)


def validate_bets(bets_raw, player):
    """Interpret raw bet input and return a list of bets.

    Helper function for method :meth:`challenges.032e.RoulettePlayer.place_bets`. Validates the
    string of bets (can be more than one) coming from the raw input provided by the player. If
    all bets are valid and the total sum of all bet values is not more than the credits available
    to the player, the list of roulette bets is returned. Otherwise, None is returned. The
    validation of the roulette bets is made verbose, so if one or more bets are invalid information
    will be printed concerning the reason of invalidity.

    :param str bets_raw: string of raw bets
    :param RoulettePlayer player: the player for whom the raw bets are validated
    :return: list of roulette bets (if all are valid and sum of values ok) or None
    :rtype: list(RouletteBet, ...) or None

    Example::

        >>> player = RoulettePlayer('player', 2000, 2100)
        >>> bets = validate_bets('1000,c1;2000,red', player)
        Insufficient credits, maximum allowed: 2000
        >>> print(bets)
        None
        >>> bets = validate_bets('1000,c1;1000,red', player)
        >>> for bet in bets:
        ...     print(bet)
        ...
        - Bet of 1000 credits in position 'c1':
            Pays out 2000 credits if won.
            Odds for winning this bet are 12 against 26.
        - Bet of 1000 credits in position 'red':
            Pays out 1000 credits if won.
            Odds for winning this bet are 18 against 20.
    """
    bets = [RouletteBet(bet_raw) for bet_raw in bets_raw.split(';')]
    if not all([bet.is_valid(verbose=True) for bet in bets]):
        return
    if sum([bet.value() for bet in bets]) > player.credits:
        print("Insufficient credits, maximum allowed: {}".format(player.credits))
        return
    return bets


class RoulettePlayer(object):
    """A class representing a roulette player.

    A roulette player is characterized by a name, an amount of credits availabe, and a goal
    (i.e. the desired amount of credits).

    :param str name: the name of the roulette player
    :param int credits: amount of credits available to the player
    :param int goal: desired amount of credits, the goal towards which the player is working

    Example::

        >>> player = RoulettePlayer('John', 100, 2000)
        >>> print(player)
        John (100 credits)
        >>> player.goal
        2000
    """


    def __init__(self, name, credits, goal):
        """Create a new roulette player."""
        self.name = name
        self.credits = credits
        self.goal = goal
        self.bets = []


    def __str__(self):
        """Format the roulette player as a string."""
        return "{} ({} credits)".format(self.name, self.credits)


    @classmethod
    def new(cls):
        """Ask input for a new roulette player and create that player.

        The user is asked to provide a name, starting amount of credits and goal for the player.
        A new roulette player is instantiated and returned.

        :return: a new roulette player with the given name, credits and goal
        :rtype: RoulettePlayer

        Example::

            >>> player = RoulettePlayer.new()
            New player name: John
            Starting credits for John: 100
            Goal for John: 2000
            >>> print(player, player.goal)
            John (100 credits) 2000
        """
        name = input("New player name: ")
        credits = int(input("Starting credits for {}: ".format(name)))
        goal = int(input("Goal for {}: ".format(name)))
        return cls(name, credits, goal)


    def place_bets(self):
        """Place bets for a turn of roulette.

        The user is continually asked to provide raw bet input until a valid string is given. It
        is possible to provide more than one bet. To do this, the bets should be joined with a
        semicolon character (see the example). The resulting list of bets is set as an attribute
        for the roulette player.

        Example::

            >>> player = RoulettePlayer('John', 100, 2000)
            >>> player.bets
            []
            >>> player.place_bets()
            100,red;200,odd
            Insufficient credits, maximum allowed: 100
            Try again: 50,red;50,odd
            >>> for bet in player.bets:
            ...     print(bet)
            ...
            - Bet of 50 credits in position 'red':
                Pays out 50 credits if won.
                Odds for winning this bet are 18 against 20.
            - Bet of 50 credits in position 'odd':
                Pays out 50 credits if won.
                Odds for winning this bet are 18 against 20.
        """
        self.bets = validate_bets(input(), self)
        while self.bets is None:
            self.bets = validate_bets(input("Try again: "), self)


class Roulette(object):
    """A class representing a game of roulette.

    A game of roulette is characterized by a table (for now purely the graphical representation
    of the table), the players (who can each place bets) and the current winning number.

    :param players: list containing the players that are participating in the game of roulette
    :type players: list(RoulettePlayer, ...)
    :param str table: path to a text file containing ASCII art for the roulette table

    Example::

        >>> p1 = RoulettePlayer('John', 100, 2000)
        >>> p2 = RoulettePlayer('Jane', 100, 2000)
        >>> table = 'input/032e_ascii_roulette_table.txt'
        >>> roulette = Roulette([p1, p2], table)
    """


    def __init__(self, players, table):
        """Create a new game of roulette."""
        self.players = players
        self.winning_number = None
        with open(table, 'r') as fil:
            self.table = fil.read()


    @classmethod
    def new(cls, nplayers=None, table=None):
        """Ask input for a new game of roulette and create that game.

        Unless already provided, the user is asked for the amount of players. This amount of new
        players is then created. Unless already provided, the user is then asked for the path to
        the table ASCII art. A roulette game is instantiated with the gathered information and
        returned.

        :param nplayers: optionally, the desired amount of players (default None)
        :type nplayers: int or None
        :param table: optionally, the path to the table ASCII art (default None)
        :type table: str or None
        :return: a game of roulette with the provided amount of newly created players and the
                 provided table ASCII art
        :rtype: Roulette

        Example::

            >>> roulette = Roulette.new()
            Amount of players: 1
            Enter information for player 1:
            New player name: John
            Starting credits for John: 100
            Goal for John: 2000
            Path to table ASCII art: input/032e_ascii_roulette_table.txt
        """
        # Ask for amount of players and create that amount of new players.
        if nplayers is None:
            nplayers = int(input("Amount of players: "))
        players = []
        for ip in range(nplayers):
            print("Enter information for player {}:".format(ip+1))
            players.append(RoulettePlayer.new())
        # Ask for the path to the table ASCII art.
        if table is None:
            table = input("Path to table ASCII art: ")
        return cls(players, table)


    def winner(self):
        """Check if there is a winner and return that player if there is one.

        A winner is a player who has reached his goal (i.e. his amount of credits is at least his
        goal). If there are multiple winners, only the first one in the list is returned.

        :return: the first winner in the list (if any), None otherwise
        :rtype: RoulettePlayer or None

        Example::

            >>> roulette = Roulette.new(table='input/032e_ascii_roulette_table.txt')
            Amount of players: 1
            Enter information for player 1:
            New player name: John
            Starting credits for John: 100
            Goal for John: 100
            >>> print(roulette.winner())
            John (100 credits)
        """
        for player in self.players:
            if player.credits >= player.goal:
                return player


    def draw_table(self):
        """Draw the ASCII art for the roulette table.

        Example::

            >>> roulette = Roulette.new(nplayers=0)
            Path to table ASCII art: input/032e_ascii_roulette_table.txt
            >>> roulette.draw_table()

                    ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
                    │top│d1 │d2 │d3 │d4 │d5 │d6 │d7 │d8 │d9 │d10│d11│
                  ┌─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┐
                  │row│s1 │s2 │s3 │s4 │s5 │s6 │s7 │s8 │s9 │s10│s11│s12│
                  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
            ┌───┐ ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ┌───┐
            │ba3│ │00 │r3 │b6 │r9 │r12│b15│r18│r21│b24│r27│r30│b33│r36│ │c3 │
            ├───┤ │   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ├───┤
            │ba2│ ├───┤b2 │r5 │b8 │b11│r14│b17│b20│r23│b26│b29│r32│b35│ │c2 │
            ├───┤ │   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ├───┤
            │ba1│ │0  │r1 │b4 │r7 │b10│b13│r16│r19│b22│r25│b28│b31│r34│ │c1 │
            └───┘ └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ └───┘
                      ┌───────────────┬───────────────┬───────────────┐
                      │     1st12     │     2nd12     │     3rd12     │
                      ├───────┬───────┼───────┬───────┼───────┬───────┤
                      │ 1-18  │  even │  red  │ black │  odd  │ 19-36 │
                      └───────┴───────┴───────┴───────┴───────┴───────┘
            split/corner: provide numbers (in order) joined with '+' (e.g. 'r1+b2')
            bet: join value and position with ',' (e.g. '1,r1+b2')
            multiple bets: join bets with ';' (e.g. '1,r1+b2;1,c1;1,even')
        """
        print(self.table)


    def place_bets(self):
        """Allow each player to place his bet(s).

        Each player is asked to place his bet(s). Each player must place at least one bet,
        and all bets that are placed must be valid. After providing correct input, an
        interpretation of all bets made by the player is printed. This interpretation shows
        each bet's value, position, payout and odds for winning.

        Example::

            >>> roulette = Roulette.new(nplayers=1, table='input/032e_ascii_roulette_table.txt')
            Enter information for player 1:
            New player name: John
            Starting credits for John: 100
            Goal for John: 2000
            >>> roulette.place_bets()

            <DRAWING OF ROULETTE TABLE>

            John, it's your turn! You have 100 credits, your goal is 2000 credits.
            Place your bet(s): 50,red
            This is the interpretation of your bet(s):
            - Bet of 50 credits in position 'red':
                Pays out 50 credits if won.
                Odds for winning this bet are 18 against 20.

            <DRAWING OF ROULETTE TABLE>

            All players have placed their bets!
        """
        for player in self.players:
            self.draw_table()
            msg = "{}, it's your turn! You have {} credits, your goal is {} credits.\n"
            msg += "Place your bet(s): "
            print(msg.format(player.name, player.credits, player.goal), end='')
            player.place_bets()
            print("This is the interpretation of your bet(s):")
            [print(bet) for bet in player.bets]
            input()
        self.draw_table()
        input("All players have placed their bets!")


    def spin_wheel(self):
        """Determine a new winning number.

        A random sample is taken from the list of numbers on the roulette wheel and set as
        the game's current winning number.

        Example::

            >>> roulette = Roulette.new(nplayers=0, table='input/032e_ascii_roulette_table.txt')
            >>> roulette.winning_number  ## Nothing is printed, there is no winning number yet.
            >>> roulette.spin_wheel()
            Press [ENTER] to spin the wheel!
            The winning number is: 'b24'
            >>> roulette.winning_number
            'b24'
        """
        input("Press [ENTER] to spin the wheel!")
        self.winning_number = random.sample(rnrs, 1)[0]
        input("The winning number is: '{}'".format(self.winning_number))


    def evaluate_bets(self):
        """Evaluate each player's bet(s) and update credits accordingly.

        Each bet of all players is evaluated. If the game's winning number is in the bet's list of
        winning numbers, the bet's payout is added to the respective player's credits. If the number
        is not in the list, the value of the bet is subtracted from the respective player's credits.

        Example::

            >>> b1 = RouletteBet('50,red')
            >>> b2 = RouletteBet('50,black')
            >>> p1 = RoulettePlayer('John', 100, 2000)
            >>> p1.bets = [b1]
            >>> p2 = RoulettePlayer('Jane', 100, 2000)
            >>> p2.bets = [b2]
            >>> roulette = Roulette([p1, p2], 'input/032e_ascii_roulette_table.txt')
            >>> roulette.winning_number = 'r1'
            >>> roulette.evaluate_bets()

            John, let's see how you did...
            Your bet of 50 credits in position 'red' is won! You gain 50 credits.
            John, that was it for you. You now have 150 credits.

            Jane, let's see how you did...
            Your bet of 50 credits in position 'black' is lost... You lose 50 credits.
            Jane, that was it for you. You now have 50 credits.

            All bets have been evaluated!
        """
        for player in self.players:
            input("\n{}, let's see how you did...".format(player.name))
            for bet in player.bets:
                msg = "Your bet of {} credits in position '{}' is ".format(
                    bet.value(),
                    bet.position(),
                    )
                print(msg, end='')
                if self.winning_number in bet.winning_numbers():
                    input("won! You gain {} credits.".format(bet.payout()))
                    player.credits += bet.payout()
                else:
                    input("lost... You lose {} credits.".format(bet.value()))
                    player.credits -= bet.value()
            msg = "{}, that was it for you. You now have {} credits."
            input(msg.format(player.name, player.credits))
        input("\nAll bets have been evaluated!")


    def remove_broke_players(self):
        """Remove all broke players from the list of players.

        When a player is broke, there is no point in keeping him in the game. This method removes
        all broke players from the list of players.

        Example::

            >>> roulette = Roulette.new(nplayers=1, table='input/032e_ascii_roulette_table.txt')
            Enter information for player 1:
            New player name: John
            Starting credits for John: 0
            Goal for John: 100
            >>> len(roulette.players)
            1
            >>> roulette.remove_broke_players()
            Sorry John, but you are broke. You're out!
            >>> len(roulette.players)
            0
        """
        players_new = []
        for player in self.players:
            if player.credits > 0:
                players_new.append(player)
            else:
                input("Sorry {}, but you are broke. You're out!".format(player.name))
        self.players = players_new


    def play_turn(self):
        """Play a turn of roulette.

        This method executes a sequence of other roulette game methods, representing a full turn
        during a game of roulette. First, all players place their bets. Second, the wheel is spun
        and a new winning number is determined. Third, all bets made by the players are evaluated.
        Fourth, broke players (if any) are removed from the game.

        Example::

            >>> roulette = Roulette.new(nplayers=1, table='input/032e_ascii_roulette_table.txt')
            Enter information for player 1:
            New player name: John
            Starting credits for John: 50
            Goal for John: 100
            >>> roulette.play_turn()

            <DRAWING OF ROULETTE TABLE>

            John, it's your turn! You have 50 credits, your goal is 100 credits.
            Place your bet(s): 25,red
            This is the interpretation of your bet(s):
            - Bet of 25 credits in position 'red':
                Pays out 25 credits if won.
                Odds for winning this bet are 18 against 20.

            <DRAWING OF ROULETTE TABLE>

            All players have placed their bets!
            Press [ENTER] to spin the wheel!
            The winning number is: 'r12'

            John, let's see how you did...
            Your bet of 25 credits in position 'red' is won! You gain 25 credits.
            John, that was it for you. You now have 75 credits.

            All bets have been evaluated!
        """
        self.place_bets()
        self.spin_wheel()
        self.evaluate_bets()
        self.remove_broke_players()


def run():
    """Execute the challenges.032e module."""
    roulette = Roulette.new(table='input/032e_ascii_roulette_table.txt')
    while roulette.winner() is None and len(roulette.players) > 0:
        roulette.play_turn()
    if roulette.winner() is not None:
        print("Congratulations {}, you have reached your goal!".format(roulette.winner().name))
    elif len(roulette.players) == 0:
        print("All players are broke, the house wins!")

