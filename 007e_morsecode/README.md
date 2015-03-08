## Information

**Challenge name:** [Morse code](http://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/)  
**Challenge number:** 7  
**Difficulty:** Easy  
**Submission date:** 2012-02-15  
**Status:** Complete

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

### *2015-03-05, 16:40*

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

    .... . .-.. .-.. ---   -.. .- .. .-.. -.--   .--. .-. --- --. .-. .- -- -- . .-.   --. --- --- -..   .-.. ..- -.-. -.-   --- -.   - .... .   -.-. .... .- .-.. .-.. . -. --. . ...   - --- -.. .- -.--

Which is apparently equal to (spoiler warning!):

    HELLO DAILY PROGRAMMER GOOD LUCK ON THE CHALLENGES TODAY

That looks like it could be correct. Up next is developing the beeping, after that it should
be done.

### *2015-03-06, 09:02*

I decided to use the `\a` character (system bell) to "print" the beep. The reason is because
this should be OS independent. First, however, I had to find a way to activate the system bell
in the terminal on Debian Jessie, since it was apparently off by default. This is what I had
to do to set it to 'on' in the terminal, but 'off' system-wide by default:

1. Apparently the bell setting in the xfce4 terminal is a "hidden setting". The only way to
   change it is by editing the terminal's configuration file.
2. Open (or create, if it does not exist) the file `/home/user/.config/xfce4/terminal/terminalrc`
   in a text editor.
2. Edit the file so it contains at least the following:

        [Configuration]
        MiscBell=TRUE

   *Note: For me this messed up my terminal settings (background changed from white to black),
   so I had to change the preferences back to what it was manually, but this did not affect
   the setting of the bell.*

3. If you log out and back in, the change should have taken effect. You can test by simply
   pressing backspace in the terminal, or by launching python in the terminal and printing
   the `\a` character.
4. If it does not work, then perhaps the bell is deactivated system-wide by default. You
   can check this with `xset q | grep bell` in the terminal. If "percent" is zero,
   the bell is off. You can turn it on with `xset b on`. Then it should work.
5. If the bell is activated system-wide by default, activating the bell in the terminal by
   default as well will be very annoying. The terminal will constantly beep, and it will
   drive you crazy. Because of this, the bell should automatically be switched off system-wide
   when logging in. You can do this by adding the following lines to the `/home/user/.bashrc`
   file:

        # Turn off system bell by default
        if [ -n "$DISPLAY" ]; then
          xset b off
        fi

6. If you log in now, the bell should be deactivated system-wide, and allowed in the
   terminal. You can always check the system bell settings with `xset q | grep bell`,
   turn it on with `xset b on` and see if it now works in the terminal by printing the `\a`
   character in python. To deactivate the bell, use `xset b off`.

Now on to the actual implementation of the Morse code sequence beeping.

### 2015-03-03, 15:04

To make the beeping of the Morse code a bit easier I will work with only two characters,
a 'space' and a 'dot'. Dashes are three subsequent dots. In the Morse sequence of a single
character there is always a blank between dots and dashes. The character spacing is three
blanks. The word spacing is seven blanks. This is pretty much the international standard.
The Morse sequence of the challenge becomes:

    . . . .   .   . ... . .   . ... . .   ... ... ...       ... . .   . ...   . .   . ... . .   ... . ... ...       . ... ... .   . ... .   ... ... ...   ... ... .   . ... .   . ...   ... ...   ... ...   .   . ... .       ... ... .   ... ... ...   ... ... ...   ... . .       . ... . .   . . ...   ... . ... .   ... . ...       ... ... ...   ... .       ...   . . . .   .       ... . ... .   . . . .   . ...   . ... . .   . ... . .   .   ... .   ... ... .   .   . . .       ...   ... ... ...   ... . .   . ...   ... . ... ...

Beeping seems to work. The beep settings (pitch and duration for blanks and dots) can be
changed, but it seems that the current default settings cause a clear beep sequence that
is relatively easy to follow. Challenge complete!
