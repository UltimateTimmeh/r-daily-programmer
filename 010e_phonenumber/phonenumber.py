"""Module containing a class for phone number objects.

Can check if the phone number is valid in its country. Can
also find in which countries the number would be valid.
"""

import validformats as vfs


class PhoneNumber(object):
    """Class representing a phone number."""


    def __init__(self, number, country='US'):
        """Initialize the phone number object."""
        self.number = number
        self.country = country


    def __str__(self):
        """String representation of a phone number."""
        return self.number


    def format(self):
        """Return the format of the phone number."""
        format = self.number
        for digit in '0 1 2 3 4 5 6 7 8 9'.split():
            format = format.replace(digit, 'x')
        return format


    def valid(self):
        """Check if the number is valid in its country."""
        format = self.format()
        valid_formats = vfs.formats_by_country[self.country]
        return format in valid_formats


    def find_valid_countries(self):
        """Find all countries in which the phone number would be valid."""
        ff = self.format()
        valid_countries = [
            cc for cc,vf in vfs.formats_by_country.items() if ff in vf
            ]
        return valid_countries


if __name__ == '__main__':

    # Initialize test data.
    test_countries = [
        'US',
        'BE',
        ]
    test_numbers = [
        # Valid US examples.
        '1234567890',
        '123-456-7890',
        '123.456.7890',
        '(123)456-7890',
        '(123) 456-7890',
        '456-7890',
        # Valid BE examples.
        '011 32 43 54',
        '02 345 67 89',
        '0800 10 800',
        '016 655 655',
        '03 454 4123',
        '03 454 5268',
        '03 454 3245',
        '02-345 67 89',
        # Invalid examples.
        '123-45-6789',
        '123:4567890',
        '123/456-7890',
        '09/123.45.67',
        ]

    # Texts that can be printed during testing.
    txt_checking = "Checking validity of number '{}'..."
    txt_isvalid = "    This number is {}valid in '{}'."
    txt_validcountries = "    It is valid in all of the following countries: {}"
    txt_validnowhere = "    This number is valid nowhere!"

    # Tests for the PhoneNumber class.
    for nn in test_numbers:
        print(txt_checking.format(nn))
        phonenumber = PhoneNumber(nn)
        for cc in test_countries:
            phonenumber.country = cc
            # Check if the number is valid in the given country.
            if phonenumber.valid():
                fill = ''
            else:
                fill = 'in'
            print(txt_isvalid.format(fill, cc))

        # Check in which countries the number is valid.
        validcountries = phonenumber.find_valid_countries()
        if len(validcountries) > 0:
            print(txt_validcountries.format(', '.join(validcountries)))
        else:
            print(txt_validnowhere)

# End
