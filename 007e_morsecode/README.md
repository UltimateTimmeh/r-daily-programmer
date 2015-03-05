## Information

**Challenge name:** [Morse code](http://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/)  
**Challenge number:** 7  
**Difficulty:** Easy  
**Submission date:** 2012-02-15  
**Status:** In progress

## Description

Write a program that can translate Morse code in the format of `...---...`. A space will
be placed between letters and a slash will be placed between words. This is your Morse
to translate:

    .... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / 
    --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . 
    -. --. . ... / - --- -.. .- -.--

For bonus, add the capability of going from a string to Morse code.  
Super-bonus if your program can flash or beep the Morse.

## Development notes

*2015-03-05, 16:40*  
I have decided to make this a bit more expansive than required. The first important decision
was to go the object-oriented route, with the definition of a MorseConvention object. With
this object a Morse code convention can be loaded, and the convention can be used to encode
text or decode a Morse sequence. Morse code conventions are stored in .mrs files, and require
a specific layout to be valid:

- Lines beginning with `#` will be ignored.
- A 'code name' must be specified: `MC=<code name>`.
- A 'character spacing convention' must be specified: `CS=<spacing convention>`. This is the
  sequence of Morse characters that will be placed between characters. In the 'International'
  convention, for example, this is three spaces.
- All other characters are optional, and can be defined as: `<character>=<morse>`.

The second important decision was to once again incorporate the TextMenu class that was
developed in challenge 002e. The user is presented with a menu in with which three things
can be done:

1. **Choose the Morse code convention:** So far there are two conventions. The 'International'
   convention (loaded by default), and the 'Reddit' convention, which can be used to decode
   the (altered) sequence in the challenge description.
2. **Encode and print:** Provide the text that needs to be encoded, and the Morse sequence will
   be printed.
3. **Encode and beep:** Provide the text that needs to be encoded, and the Morse sequence will
   be beeped (still in development).
4. **Decode:** Provide the Morse sequence that needs to be decoded, and the text will be
   printed.   

Since slashes are obviously not a valid Morse character, I will replace it with an extra
space. This means the spacing between characters is one unit, and the spacing between
words is three units. The sequence to decode becomes:

    .... . .-.. .-.. ---   -.. .- .. .-.. -.--   .--. .-. --- --. .-. .- -- -- . .-.   
    --. --- --- -..   .-.. ..- -.-. -.-   --- -.   - .... .   -.-. .... .- .-.. .-.. . 
    -. --. . ...   - --- -.. .- -.--

Which is apparently equal to (spoiler warning!):

    HELLO DAILY PROGRAMMER GOOD LUCK ON THE CHALLENGES TODAY

That appears to be correct. Up next is developing the beeping, after that it should be done.
