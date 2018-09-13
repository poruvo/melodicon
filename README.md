# Melodicon
An program that converts letters, words, and phrases to musical pitches using an alphanumeric index.

## Purpose 
This program was written to attempt to bridge the gap between 'music' and 'words'. The Melodicon uses a twelve-tone musical scale to convert characters from a phrase, name, or string into note pitches or solfege.

Here is an example of the index.

Your scale degrees are 1-12 and the corresponding characters for each alphabet are located at the top and the bottom of each scale degree.

This system is what makes the melodicon a twelve-tone alphanumeric composing index.

<pre>
OLD LATIN
A B C D E F G H I  K  L  M
1 2 3 4 5 6 7 8 9 10 11 12
N O P Q R S T V X  Y  Z  &
---
GREEK
Α Β Γ Δ Ε Ζ Η Θ Ι  Κ  Λ  Μ
1 2 3 4 5 6 7 8 9 10 11 12
Ν Ξ Ο Π Ρ Σ Τ Υ Φ  Χ  Ψ  Ω
---
ELDER FUTHARK
ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ ᚷ ᚹ ᚺ  ᚾ   ᛁ  ᛃ
1 2 3 4 5 6 7 8 9 10 11 12
ᛇ ᛈ ᛉ ᛋ ᛏ ᛒ ᛖ ᛗ ᛚ  ᛜ  ᛞ  ᛟ
</pre>

Use this program as a tool to create interesting musical phrases or motifs to use in your own personal projects!

Additionally, the user can export their converted word/phrase to a MIDI File.

This program requires Python 3.6.

## Usage
The program has a numeric menu with 5 options.

The default __scale__ is a twelvetone scale starting from pitch _B4_  

The default __alphabet__ reference is a modified version of the _Old Latin_ alphabet.

Traditionally, you may be inclined to try out words that you know or words that you feel. However, I encourage you to translate some of those words into other latin-based languages or into complete ancient greek or elder futhark translations. (Or, try pure greek and futhark words.)

For example: 

**KING** in English, B[10,9,1,7] (( B - A#/Bb - D - G#/Ab ))

   translates to:
    
**REGIS** in Latin. B[5,5,7,9,6] ((D#/Eb - D#/Eb - F - G - E ))

   translates to:

**ROI** in French. B[5,2,9] ((D#/Eb - C - G ))


As you can see, these provide very different musical phrases.
Furthermore, these three words share the same meaning.
Feel free to be as creative as you like! 
There are no wrong words! (notes)

### Menu
***
#### 1) Convert a Word, Phrase, or String
Converts a word, phrase, or string into solfege or notes.

#### 2) Change Alphabet
Change the alphabet index of the melodicon.
(The default alphabet is Old Latin.)

#### 3) Change Scale Tonic
Change the scale tonic of the melodicon
(The default scale tonic is B.)

The scale tonic will be changed in semitones, **use integers ranging from -12 to 12**

#### 4) Restore Defaults
Return alphabet index and music scale to _'Old Latin'_ and _'B4'_ respectively.  

#### 5) Exit
Exit the program  
***

## Dependencies
This program needs the following packages to run word to MIDI conversion:  

[MIDIUtil](https://pypi.org/project/MIDIUtil/) - A Python Library for writing MIDI files by [Mark Conway Wirt](https://pypi.org/project/MIDIUtil/#data)


## Contributing
1) Fork
2) Create your branch: `git checkout -b my-addition`
3) Commit changes: `git commit -am 'Add This Feature'`
4) Push to branch: git push origin my-addition
5) Submit a Pull Request
6) Code It
7) Push It Back Up
8) Celebrate!

## Editing Your Melodicon
Since I made this program with simple sets of local data, it is possible to edit your index to suit the characters that you need.
At the top of the code, simply replace the characters you wish to have appear by replacing them in the CONST arrays I have initialized.

If you have any issues trying to EDIT the index for YOUR melodicon, please let me know.

(If you mess it up, just redownload the melodicon.py :D )

## History
Version 0.7.7 - Open Source Code - Needs Refactoring, Fully Functional

### Changelog
0.7.7 - Fixed 'L' + 'TH' Futhark bug.

0.7.6 - Fixed '&' Old Latin bug.

0.7.5 - Removed Reverse Melodicon from code, edited docs, planned to fix bug with '&' character in OldLatin dictionary.

0.1.0 - Initial Commit

## Credits
Program developed by Stephon X. Jones

## Sidenote
I don't plan on this being a heavily-developed project.  
This is something I plan on keeping up with in my spare time.  
If you have any suggestions please feel free to make a pull req or let me know what ideas you have!

## License
MIT License

Copyright (c) 2018 poruvo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
