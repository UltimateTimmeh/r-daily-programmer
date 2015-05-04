# cipher - Functions for encoding and decoding messages

## Description

This module contains several functions for encoding, decoding and brute-force-decoding messages
using a cipher.

## Functions

- **caesar(**msg, n, dir='encode'**)**

  Encode or decode `msg` using a caesar cipher with a right shift of `n`.

- **caesar\_brute\_force(**msg_encoded**)**

  Return all possible options for decoding a caesar-cipher-encoded message.
