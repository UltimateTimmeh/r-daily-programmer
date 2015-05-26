#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/qxuug/3152012_challenge_25_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/025e.py

| **Challenge name:** Vote Counter (reddit_, source_)
| **Challenge number:** 25
| **Difficulty:** Easy
| **Submission date:** 2012-03-15
| **Status:** Complete

Description
-----------

In an election, the person with the majority of the votes is the winner. Sometimes due to similar
number of votes, there are no winners.

Your challenge is to write a program that determines the winner of a vote, or shows that there are
no winners due to a lack of majority.

Example run
-----------

::

    $ python3 dailyprogrammer.py 025e
    List of votes: ['A', 'A', 'B', 'C', 'A', 'B']
      'A' has won the election!
      He got 3 votes (50% of total)
    List of votes: ['A', 'A', 'B', 'C', 'A', 'B', 'B']
      ['A', 'B'] got the same amount of votes!
      They each got 3 votes (43% of total)
    List of votes: []
      There are no votes!

Module contents
---------------
"""

from plugins.listtools import count_items, most_prevalent_items


def determine_election_winners(votes):
    """Count votes to determine the winner(s) of an election.

    Returns a list with the winner(s), the amount of votes the winner(s) got and what
    percentage this is of the total amount of votes.

    :param list votes: the list of votes
    :return: tuple containing a list with the winner(s), the amount of votes for the winner(s)
             and the percentage of total votes for for the winner(s)
    :rtype: tuple(list, int, float)

    Example::

        >>> determine_election_winners(['A', 'B', 'A', 'C'])
        (['A'], 2, 0.5)
        >>> determine_election_winners(['A', 'B', 'B', 'A', 'C'])
        (['A', 'B'], 2, 0.4)
    """
    if votes == []:
        return ([], 0, 0)
    count = count_items(votes)
    winners = most_prevalent_items(votes)
    winnervotes = count[winners[0]]
    totalvotes = sum([v for p, v in count.items()])
    return (winners, winnervotes, winnervotes/totalvotes)


def run():
    """Execute the challenges.025e module."""
    votess = [
        ['A', 'A', 'B', 'C', 'A', 'B'],
        ['A', 'A', 'B', 'C', 'A', 'B', 'B'],
        [],
    ]
    for votes in votess:
        print("List of votes: {}".format(votes))
        winners = determine_election_winners(votes)
        if len(winners[0]) == 0:
            print("  There are no votes!")
        elif len(winners[0]) == 1:
            print("  '{}' has won the election!".format(winners[0][0]))
            print("  He got {} votes ({:.0f}% of total)".format(winners[1], 100*winners[2]))
        else:
            print("  {} got the same amount of votes!".format(winners[0]))
            print("  They each got {} votes ({:.0f}% of total)".format(winners[1], 100*winners[2]))

