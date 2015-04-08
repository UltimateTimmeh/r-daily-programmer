#!/usr/bin/python3


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


    @classmethod
    def ask(cls):
        """Initialize a PersonalInfo object by asking for info."""
        # Ask user for information.
        name = input("Name? > ")
        age = input("Age? > ")
        reddit_username = input("Reddit Username? > ")
        return cls(name, age, reddit_username)


    def write(self, fn, mode='a'):
        """Write self to output file fn."""
        with open(fn, mode) as output_file:
            output_file.write(str(self)+'\n')


if __name__ == '__main__':
    pi = PersonalInfo.ask()
    print(pi)
    pi.write('output.txt')
