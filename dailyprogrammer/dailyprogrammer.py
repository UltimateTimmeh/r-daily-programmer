import importlib
import sys
challenge_id = sys.argv[1]
challenge = importlib.import_module('challenges.{}'.format(challenge_id))
challenge.run()
