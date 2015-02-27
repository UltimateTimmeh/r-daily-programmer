## Information

**Challenge name:** [Password protect](http://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/)  
**Challenge number:** 5  
**Difficulty:** Easy  
**Submission date:** 2012-02-13  
**Status:** Complete

## Description

Your challenge for today is to create a program which is password protected, and wont open unless
the correct user and password is given.

For extra credit, have the user and password in a seperate .txt file. For even more extra credit,
break into your own program :).

## Development notes

*<2015-02-27, 12:13>*  
In this challenge I will make use of the TextMenu class developed in 002e and the random password
generator in 004e to make the program a bit more fun. Users will get a menu, where they can choose
if they want to create a new user, or log in. When creating a new user, a username and password have
to be provided. If the provided password is left blank, then a random 8-character password is
generated for them. I will also apply encryption and salting to the password before storing it in
a file, just for fun.

*<2015-02-27, 14:46>*  
So this is what I have. Upon executing the code the user is presented a menu:

1. Log in: The user is asked for a username and a password. If the user does not exist, or the password is
   not correct, logging in fails. If successful, the user can now select option 3.
2. Create new user: The user is asked for a new username until he provides one that does not yet exist.
   Afterwards the user optionally provides a password, but if he leaves this field blank a random
   8-character password is generated for him. The new user is then added to the user_database.txt file.
3. Look at secret code: This is the part of the code that really matters. You need to be logged in to be
   able to see it. In this example it doesn't do anything special, it just shows you a 'secret' code which
   is actually just a random string.

There is one example user in the database: 'john_smith' with password 'rdailyprogrammer'.

The fun thing is that, because the password is salted and hashed, you can't just look in the
user_database.txt file to steal a valid username and password to break into the program. It's still pretty
easy to access the secret code without actually logging in though. All that is required is that the
variable `user` is defined in passwordprotect.py's namespace. So simply open python3.4 in a terminal and
do the following:

    >>> import passwordprotect
    >>> passwordprotect.user = ''
    >>> passwordprotect.protected_code()

And there you have it. I guess this challenge is complete.
