from bs4 import BeautifulSoup
import datetime
import http
import importlib
import os
import praw
import sys
import unittest

from plugins import config as cfg


def execute(challenge_id):
    """Execute a challenge."""
    challenge_fp = os.path.join(cfg.root_dir, 'challenges', '{}.py').format(challenge_id)
    if not os.path.isfile(challenge_fp):
        print("\nERROR: Could not find solution module for challenge {}!\n".format(challenge_id))
        return
    challenge = importlib.import_module('challenges.{}'.format(challenge_id))
    challenge.run()


def prepare(challenge_id):
    """Prepare a challenge's solution module."""
    # Make sure the file doesn't already exist. We don't want to risk overwriting!
    challenge_fp = os.path.join(cfg.root_dir, 'challenges', '{}.py'.format(challenge_id))
    if os.path.isfile(challenge_fp):
        print("\nERROR: Solution module for challenge {} already exists!\n".format(challenge_id))
        return

    # Split challenge id in number and difficulty.
    challenge = {'id': challenge_id}
    challenge['nr'] = int(challenge['id'][:-1])
    challenge['difficulty'] = {'e': 'Easy', 'i': 'Intermediate', 'h': 'Hard'}[challenge['id'][-1]]
    challenge_title = 'challenge #{nr} [{difficulty}]'.format(**challenge).lower()

    # Fetch the url of the challenge's post from Reddit.
    protocol = 'https://'
    url_address = 'www.reddit.com'
    url_path = '/r/dailyprogrammer/wiki/challenges'
    hdr = {'User-Agent': 'Getting DailyProgrammer list of challenges'}
    connection = http.client.HTTPSConnection(url_address)
    connection.request('GET', url_path, headers=hdr)
    page = connection.getresponse().read().decode('utf-8')
    connection.close()
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
    challenge['url'] = protocol + url_address + url_match[0]
    print(challenge['url'])

    print("\nPreparing challenge {} from url:\n{}".format(challenge['id'], challenge['url']))

    # Get challenge data from challenge post using PRAW
    r = praw.Reddit(user_agent='dailyprogrammer')
    challenge_submission = r.get_submission(challenge['url'])
    challenge['description'] = challenge_submission.selftext
    challenge['date'] = str(datetime.date.fromtimestamp(challenge_submission.created))

    # Create the challenge module blueprint by formatting the template.
    template_fp = os.path.join(cfg.root_dir, 'templates', 'challenge.py')
    with open(template_fp, 'r') as fil:
        template = fil.read()
    with open(challenge_fp, 'w') as fil:
        fil.write(template.format(**challenge))
    print("DONE\n")


def runtests(logfn):
    """Execute the project's unit tests and write results to a log file."""
    testloader = unittest.defaultTestLoader
    testsuite = testloader.discover(cfg.tests_dir)
    logfp = os.path.join(cfg.logs_dir, logfn)
    with open(logfp, 'w') as logfile:
        testrunner = unittest.TextTestRunner(logfile, verbosity=2)
        testrunner.run(testsuite)


if __name__ == '__main__':
    actions = {
        'execute': execute,
        'prepare': prepare,
        'runtests': runtests,
    }
    action, arg = sys.argv[1:]
    actions[action](arg)

