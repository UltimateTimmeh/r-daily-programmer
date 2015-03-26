## Information

**Challenge name:** [Phone number](http://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/)  
**Challenge number:** 10  
**Difficulty:** Easy  
**Submission date:** 2012-02-18  
**Status:** Complete

## Description

The exercise today asks you to validate a telephone number, as if written on an input form.
Telephone numbers can be written as ten digits, or with dashes, spaces, or dots between the
three segments, or with the area code parenthesized; both the area code and any white space
between segments are optional.

Thus, all of the following are valid telephone numbers:

- 1234567890
- 123-456-7890
- 123.456.7890
- (123)456-7890
- (123) 456-7890 (note the white space following the area code)
- 456-7890

The following are not valid telephone numbers:

- 123-45-6789
- 123:4567890
- 123/456-7890.

[Source](http://www.programmingpraxis.com)

## Development notes

### 2015-03-26, 08:44

**Description**

I solved this one by creating a module that contains valid phone number formats for various
countries (so far only the US and Belgium). A phone number's 'format' is defined as the phone
number string in which all digits are replaced by the character 'x'. Thus, a list of valid
formats is simply a list of strings containing 'x'es and spacing characters (if any).

I then created a `PhoneNumber` class that has the number and the country as attributes.
The method `valid` returns if the number is valid in the country by checking if the number's
format is in the list of that country's valid formats. Simple. I also added a method that
returns a list of all countries in which the number would be valid.

The main body of the `phonenumber` module runs a few tests on the `PhoneNumber` class (using,
among others, the test data provided in the challenge) to check if everything is working as
expected.

**Excerpt from output**

    $ python3.4 phonenumber.py 
    Checking validity of number '1234567890'...
        This number is valid in 'US'.
        This number is invalid in 'BE'.
        It is valid in all of the following countries: US
    Checking validity of number '123-456-7890'...
        This number is valid in 'US'.
        This number is invalid in 'BE'.
        It is valid in all of the following countries: US
    ...
    Checking validity of number '011 32 43 54'...
        This number is invalid in 'US'.
        This number is valid in 'BE'.
        It is valid in all of the following countries: BE
    Checking validity of number '02 345 67 89'...
        This number is invalid in 'US'.
        This number is valid in 'BE'.
        It is valid in all of the following countries: BE
    ...
    Checking validity of number '123-45-6789'...
        This number is invalid in 'US'.
        This number is invalid in 'BE'.
        This number is valid nowhere!
    ...
    Checking validity of number '09/123.45.67'...
        This number is invalid in 'US'.
        This number is invalid in 'BE'.
        This number is valid nowhere!

**Sources**

- [Valid phone numbers in the US](http://search.cpan.org/~kennedyh/Number-Phone-US-1.5/lib/Number/Phone/US.pm)
- [Valid phone numbers in Belgium](http://taaladvies.net/taal/advies/tekst/52/)

This challenge is complete!
