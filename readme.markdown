tapword
=======

A python experiment for recognizing tap combinations.

tap.py
------

A simple script which listens for character input.  The q character quits the
program.  The space character counts as a tap. All other characters are ignored.
The timing between taps is analyzed and the relative length of each tap with
respect to the rest of the taps in a set is computed.  These lengths are then
classified into 's' (short) and 'l' (long).  When a specific sequence appears at
the end of the current set, a match is indicated.  The current set is reset
after a delay of one second.

Please Note: I have not yet tested this code on a Windows system, though the
code is written with Windows support.  It works correctly on a Mac and should
work just as well on any other Unix flavored machine.

---

The general aim of this project is to investigate various methods of
interpreting taps as input. I hope to eventually port this code to a
microcontroller to enable a sort of tap input, perhaps through a piezoelectric
element.

