#!/usr/bin/python3
"""
This module contains a function for left, right and center justifying
text. The main body asks for the path to a file and a type of justification
to be applied to it. The justified text is written to a file that has the
same path with '_justified' appended before the file extension.
"""

import os

justifications = {
    'left': '<',
    'right': '>',
    'center': '^'
    }


def justify_text(text, justify='left'):
    """Justify text."""
    if justify in justifications:
        justify = justifications[justify]
    elif justify not in justifications.values():
        error = "Unknown justification '{}'."
        raise ValueError(error.format(justify))

    text_stripped = [line.strip() for line in text.split('\n')]
    max_length = max([len(line) for line in text_stripped])
    text_justified = '\n'.join([
        '{0:{1}{2}}'.format(line, justify, max_length) for line in text_stripped
        ])

    return text_justified


if __name__ == '__main__':
    # Get user input.
    text_in_fn = input('File to justify? > ')
    justify = input('Justfy left, right or center? > ')

    # Set path to output file.
    path, ext = os.path.splitext(text_in_fn)
    text_out_fn = path + '_justified' + ext

    # Read, justify and write.
    with open(text_in_fn, 'r') as text_in_file:
        text_in = text_in_file.read()
    text_out = justify_text(text_in, justify)
    with open(text_out_fn, 'w') as text_out_file:
        text_out_file.write(text_out)
