# Melodicon
An program that converts letters, words, and phrases to musical pitches using an alphanumeric index.

## Purpose 
This program was written to attempt to bridge the gap between 'music' and 'words'. The Melodicon uses a twelve-tone musical scale to convert characters from a phrase, name, or string into note pitches or solfege.

Use this program as a tool to create interesting musical phrases or motifs to use in your own personal projects!

Additionally, the user can export their converted word/phrase to a MIDI File.

## Usage
The program has a numeric menu with 6 options.

The default __scale__ is a twelvetone scale starting from pitch _B4_  

The default __alphabet__ reference is a modified version of the _Old Latin_ alphabet.   


### Menu
***
#### 1) Convert a Word, Phrase, or String
Converts a word, phrase, or string into solfege or notes.  
#### 2) Change Alphabet
Change the alphabet index of the melodicon  
TODO: IMPLEMENT THIS FEATURE
#### 3) Change Scale Tonic
Change the scale tonic of the melodicon  
TODO: IMPLEMENT THIS FEATURE
#### 4) Convert Scale Degrees to Possible Letters
Convert numerical values to possible letter pairs
(This is intended to show the user the _possible_ letter combinations to form words with.  
TODO: IMPLEMENT THIS FEATURE
#### 5) Restore Defaults
Return alphabet index and music scale to _'Old Latin'_ and _'B4'_ respectively.  
(This feature will be implemented after the scale/alphabet change features are both added)
#### 6) Exit
Exit the program  
***

## Dependencies
This program needs the following packages to run:  

[MIDIUtil](https://pypi.org/project/MIDIUtil/) - A Python Library for writing MIDI files by [Mark Conway Wirt](https://pypi.org/project/MIDIUtil/#data)


## Contributing
1) Fork
2) Create your branch: `git checkout -b my-addition`
3) Commit changes: `git commit -am 'Add This Feature'`
4) Push to branch: git push origin my-addition
5) Submit a Pull Request

## History
Version 0.0.1 - First Commit + README.md

### Changelog

## Credits
Program developed by Stephon X. Jones

## Sidenote
I don't plan on this being a heavily-developed project.
This is something I plan on keeping up with in my spare time.
If you have any suggestions please feel free to make a pull req.

## License
MIT License

Copyright (c) 2018 poruvo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
