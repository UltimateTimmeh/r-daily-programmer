#!/usr/bin/python3
"""
Module with class containing personal information.
"""


class PersonalInfo(object):
    """A class containing personal info. Be careful!"""


    def __init__(self, name, age, reddit_username):
        """Initialize the personal information."""
        self.name = name
        self.age = age
        self.reddit_username = reddit_username


    def __str__(self):
        """Format self as string."""
        # Format and print output.
        out = ("Your name is '{name}', you are {age} years old and " +
               "your Reddit username is '{reddit_username}'.")
        return out.format(**self.__dict__)


    def write(self, fn, mode='a'):
        """Write self to output file fn."""
        with open(fn, mode) as output_file:
            output_file.write(str(self)+'\n')


if __name__ == '__main__':

    name = input("Name? > ")
    age = input("Age? > ")
    reddit_username = input("Reddit Username? > ")
    pi = PersonalInfo(name, age, reddit_username)
    print(pi)
    pi.write('example_output.txt')
