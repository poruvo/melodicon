#Local Mock Data and Dicts

#Alphabets
oldLatin = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z', '&']

GREEK = ['\u0391','\u0392','\u0393', '\u0394', '\u0395', '\u0396', '\u0397', '\u0398', '\u0399', '\u039a', '\u039b', '\u039c', '\u039d', '\u039e', '\u039f', '\u03a0', '\u03a1', '\u03a3','\u03a4', '\u03a5', '\u03a6', '\u03a7', '\u03a8', '\u03a9']                        

twelvetoneScale = list(range(1, 13))
bTonicScale = ['B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb']
solfegeNames = ['do', 'di', 're', 'me', 'mi', 'fa', 'fi', 'sol', 'le', 'la', 'te', 'ti']
solfegeDict = dict(zip(twelvetoneScale, solfegeNames))
inputReturn = []

#--------------Functions----------------------------

def makemusicalphabetbyhalf(alphabet, twelvetone):
    # Create A-Z music scale from selected alphabet
    musicalphahalf = dict(zip(alphabet, twelvetone))
    return musicalphahalf


def makemusicscale(tonicscale, twelvetone):
    # Creates user's musical scale based on their tonic
    scaledict = dict(zip(twelvetone, tonicscale))
    return scaledict


def compareuserinput(musicdictam, musicdictnz, userinput):
    # Compare user input to selected music scale/alphabet and returns scale degrees
    import re
    returnedinput = []
    userinputed = userinput.upper()
    userinputed = userinputed.replace(" ", "")
    userinputed = userinputed.replace(",", "")
    userinputed = re.sub("[^A-Za-z]", "", userinputed)
    for letter in userinputed:
        if letter in musicdictam.keys():
            returnedinput.append(musicdictam.get(letter))
        elif letter in musicdictnz.keys():
            returnedinput.append(musicdictnz.get(letter))
        elif letter == 'U':
            returnedinput.append(musicdictnz.get('V'))
        elif letter == 'W':
            returnedinput.append(musicdictnz.get('V'))
            returnedinput.append(musicdictnz.get('V'))
        elif letter == 'J':
            returnedinput.append(musicdictam.get('G'))
        else:
            if letter not in musicdictam.keys() or musicdictnz.keys():
                returnedinput.append('%')
    print('Your Input: ' + userinput)
    print(' - '.join(userinputed) + '\n')
    return returnedinput


def populatescaledegrees(musicscale, returnedinput):
    # Converts user's scale degrees into notes
    notenames = []
    for x in returnedinput:
        if x in musicscale.keys():
            notenames.append(musicscale.get(x))
    print(('='*12) + 'NOTES' + ('='*12))
    print(' - '.join(notenames) + '\n')


def populatesolfege(solfdict, returnedinput):
    # Convert user's scale degrees into solfege
    solfnames = []
    for x in returnedinput:
        if x in solfdict.keys():
            solfnames.append(solfdict.get(x))
    print(('='*12) + 'SOLFEGE' + ('='*12))
    print(' - '.join(solfnames) + '\n')


def createmidifile(scaledegrees):
    # Convert user input to midi file.
    import os  
    import os.path
    from pathlib import Path
    filepath = Path.cwd() / 'midis'
    p = str(filepath)
    if not os.path.exists(p):
            os.makedirs(p)
            os.chdir(p) 

    if os.path.isdir(p) == True:
        os.chdir(p)
        print("Inside Directory")
        print(p)
    else:
        p = Path.cwd() / 'midis'
        if not os.path.exists(p):
            os.makedirs(p)
        os.chdir(p)

    savecheck = 0
    while savecheck == 0:
        usersave = input("Create MIDI File? (Y/N): ")
        usersave = usersave.upper()
        if usersave == "Y":

            from midiutil.MidiFile import MIDIFile
            for i in range(len(scaledegrees)):
                scaledegrees[i] = int(scaledegrees[i] + 71)
            filename = ""
            while filename == "":
                filename = input("Enter your filename:  ")
                
                if(os.path.isfile(filename+".mid")):
                    print("Error: File already exists!!")
                    filename = ""
                elif filename == "":
                    print("No characters detected.")
                    filename = ""
                else:
                    filename = filename + ".mid"
                    continue
    
                       
            degrees = scaledegrees  # MIDI note number
            track = 0
            channel = 0
            time = 1  # In beats
            duration = 1  # In beats
            tempo = 85  # In BPM
            volume = 100  # 0-127, as per the MIDI standard
            MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
            # automatically)
            MyMIDI.addTempo(track, time, tempo)
            for i, pitch in enumerate(degrees):
                MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
            print('Saving ' + filename + ' to ' + p + '...')    
            with open(filename, "wb") as output_file:
                MyMIDI.writeFile(output_file)
            p = str(Path.cwd() / '')
            os.chdir(p)
            savecheck += 1
        elif usersave == 'N':
            p = str(Path.cwd() / '')
            os.chdir(p)
            savecheck += 1
        else:
            print('Invalid Input. Try Again')
            continue


##  MENU
def mainmenu():
    menucheck = 0
    tonicScale = []
    userchanged = []
    if tonicScale == []:
        tonicScale = bTonicScale
    else:
        tonicScale = userchanged
    while menucheck == 0:
        print('''Welcome to the Melodicon! Choose your menu option below:
            1) Convert Words/Phrases/Names
            2) Change Alphabet
            3) Change Scale Tonic
            4) Convert Scale Degrees to Possible Letters
            5) Restore Defaults
            6) Exit''')
        menuinput = input("Enter a number to select an option: ")
        if menuinput == '1':
            repeatcheck = 0
            while repeatcheck == 0:
                themelodicon(tonicScale)
                reconvertcheck = 0
                while reconvertcheck == 0:
                    convertagain = input("Convert more words? (Y/N): ")
                    convertagain = convertagain.upper()
                    if convertagain == 'Y':
                        reconvertcheck += 1
                        continue
                    elif convertagain == 'N':
                        reconvertcheck += 1
                        repeatcheck += 1
                    else:
                        print("Invalid Input. Try Again")
                        continue
        elif menuinput == '2':
         print(GREEK)
            #TODO - Change Alphabet
            ## Change the default alphabet from 'Old Latin' to a different lexical index.

            # Take the user input and convert it into the unicode lexicog 24-letter dict index
            # Compare the user input to the regular alphabet, then transfer indexes to new 24 char alphabet,
            # Display the new alpha characters with solfege and convert into MIDI.
            

        elif menuinput == '3':
            inputCheck = 0
            changeCheck = 0
            #Change the scale tonic of the Melodicon
            #    changeScaleTonisc(tonicScale)
            from collections import deque
            #Show me whats in the thing
            if tonicScale == []:
                tonicScale = bTonicScale
                s = deque(tonicScale)
                print(s)
            else:
                s = deque(tonicScale)
                print(s)
            #TODO - Change Scale Tonic
            ##Change the default tonic note from 'B' to another 12-tone pitch index.
            
            while changeCheck == 0:
                changescale = input("Which note would you like to change your tonic to?: \n New Tonic (Move in semitones): ")
                while inputCheck == 0:
                    try:
                        changescale = int(changescale)
                        inputCheck += 1
                    except ValueError:
                        print("Invalid input, not an integer! Try again.")
                        changescale = input("Which note would you like to change your tonic to?: \n New Tonic (Move in semitones): ")
                        continue
                    changescale = -int(changescale)
                    if changescale < 12 and changescale > -12:
                        s.rotate(changescale)
                        userchanged = list(s)
                        print (userchanged + "\n")
                        baseTonic = userchanged
                        tonicScale = userchanged
                        changeCheck =+ 1
                        break
                    else:
                        print("Invalid Input, please enter an integer")
                        continue
                
        elif menuinput == '4':
            #TODO - Reverse Melodicon 
            ## Show the possible letter pairs of numeric scale degrees that are entered.
            repeatcheck = 0
            while repeatcheck == 0:
                reversemelodicon(tonicScale)
                reconvertcheck = 0
                while reconvertcheck == 0:
                    convertagain = input("Convert more words? (Y/N): ")
                    convertagain = convertagain.upper()
                    if convertagain == 'Y':
                        reconvertcheck += 1
                        continue
                    elif convertagain == 'N':
                        reconvertcheck += 1
                        repeatcheck += 1
                    else:
                        print("Invalid Input. Try Again")
                        continue

        elif menuinput == '5':
            #TODO - Restore Defaults !! THIS IS IMPORTANT
            ## Restore the OldLatin and B-Scale defaults.
            tonicScale = bTonicScale
            print("Default settings restored.\n")

        elif menuinput == '6':
            #Exit the Program
            menucheck += 1
            return
        else:
            print('Invalid Input. Try Again.')
            continue

#---------THE MELODICON-----------------
def themelodicon(tonicScale):
    print('''
    Welcome to the Melodicon!
    OldLatin is the default alphabet!
    (Invalid characters will be met with '%')
    U = V
    W = UU
    J = G
    ''')
    if tonicScale == bTonicScale:
        print("(Your Scale Tonic is " + tonicScale[0] +  ")")
    else:
        print("(Your Scale Tonic is " + tonicScale[0])
    print(oldLatin)
    userMusicDictAM = makemusicalphabetbyhalf(oldLatin[0:12], twelvetoneScale)
    userMusicDictNZ = makemusicalphabetbyhalf(oldLatin[12:24], twelvetoneScale)
    userScale = makemusicscale(tonicScale, twelvetoneScale)
    wordInput = input("Please enter a word, name, or phrase to convert: ")
    userReturn = compareuserinput(userMusicDictAM, userMusicDictNZ, wordInput)
    populatescaledegrees(userScale, userReturn)
    populatesolfege(solfegeDict, userReturn)
    createmidifile(userReturn)
    return

#---------RESERVE MELODICON--------------
def reversemelodicon(tonicScale):
    print('''
    The Reverse Melodicon!
    Turn your scale degrees into letters for possible word combinations!
    OldLatin is the default alphabet!
    (Invalid characters will be met with '%')
    U = V
    W = UU
    J = G

    ''')
    if tonicScale == bTonicScale:
        print("(Your Scale Tonic is " + tonicScale[0] +  ")")
    else:
        print("(Your Scale Tonic is " + tonicScale[0])
    print(oldLatin)
    #For Each character in the string, check to see if its in a dict
    #for Each character that IS in a dict, add it to a temp value
    # Display each scale degree and the two possible letters
    # Leave instructions for converting into MIDI
    return
#------------MAIN----------------------
def __init__():
    tonicScale = []
    mainmenu()

#--------BOILERPLATE------------#
__init__()
