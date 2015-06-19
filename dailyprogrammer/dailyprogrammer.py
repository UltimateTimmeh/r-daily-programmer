from bs4 import BeautifulSoup
import datetime
import importlib
import os
import praw
import sys
from urllib.request import urlopen


def execute(challenge_id):
    """Execute a challenge."""
    if not os.path.isfile(os.path.join('challenges', '{}.py'.format(challenge_id))):
        print("\nERROR: Could not find solution module for challenge {}!\n".format(challenge_id))
        return
    challenge = importlib.import_module('challenges.{}'.format(challenge_id))
    challenge.run()


def prepare(challenge_id):
    """Prepare a challenge's solution module."""
    # Make sure the file doesn't already exist. We don't want to risk overwriting!
    challenge_path = os.path.join('challenges', '{}.py'.format(challenge_id))
    if os.path.isfile(challenge_path):
        print("\nERROR: Solution module for challenge {} already exists!\n".format(challenge_id))
        return

    # Split challenge id in number and difficulty.
    challenge = {'id': challenge_id}
    challenge['nr'] = int(challenge['id'][:-1])
    challenge['difficulty'] = {'e': 'Easy', 'i': 'Intermediate', 'h': 'Hard'}[challenge['id'][-1]]
    challenge_title = 'challenge #{} [{}]'.format(challenge['nr'], challenge['difficulty'].lower())

    # Fetch the url of the challenge's post from Reddit.
    url_base = 'http://www.reddit.com'
    url = url_base + '/r/dailyprogrammer/wiki/challenges'
    page = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(page)
    url_match = [link.get('href') for link in soup.find_all('a') \
        if link.string is not None and challenge_title in link.string.lower()]

    if len(url_match) == 0:
        print("\nERROR: No challenge with title '{}' was found.\n".format(challenge_title))
        return
    elif len(url_match) > 1:
        print("\nWARNING: Multiple challenges with title '{}' were found:".format(challenge_title))
        print('\n'.join(url_match))
        print("Automatically picking the first one. Others will have to be prepared manually.\n")
    challenge['url'] = url_base + url_match[0]

    print("\nPreparing challenge {} from url:\n{}".format(challenge['id'], challenge['url']))

    # Get challenge data from challenge post using PRAW
    r = praw.Reddit(user_agent='dailyprogrammer')
    challenge_submission = r.get_submission(challenge['url'])
    challenge['description'] = challenge_submission.selftext
    challenge['date'] = str(datetime.date.fromtimestamp(challenge_submission.created))

    # Create the challenge module blueprint by formatting the template.
    template_path = os.path.join('templates','challenge.py')
    with open(template_path, 'r') as fil:
        template = fil.read()
    with open(challenge_path, 'w') as fil:
        fil.write(template.format(**challenge))
    print("DONE\n")


if __name__ == '__main__':
    actions = {
        'execute': execute,
        'prepare': prepare,
    }
    action,  challenge_id = sys.argv[1:]
    actions[action](challenge_id)

