#Local Mock Data and Dicts

oldLatin = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z', '&']
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
    # Add deques to allow user to change/iterate through tonics
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
    p = Path.cwd() / 'midis'
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
            print(f'saving {filename} to {p}')
            with open(filename, "wb") as output_file:
                MyMIDI.writeFile(output_file)
            p = Path.cwd() / ''
            os.chdir(p)
            savecheck += 1
        elif usersave == 'N':
            p = Path.cwd() / ''
            os.chdir(p)
            savecheck += 1
        else:
            print('Invalid Input. Try Again')
            continue


##  MENU
def mainmenu():
    menucheck = 0
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
                themelodicon()
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
                        print("Invalid Input. Try Again1")
                        continue
        elif menuinput == '2':
            print("Feature Not Added Yet!")
            #TODO - Change Alphabet
            ## Change the default alphabet from 'Old Latin' to a different lexical index.
        elif menuinput == '3':
            print("Feature Not Added Yet!")
            #TODO - Change Scale Tonic
            ##Change the default tonic note from 'B' to another 12-tone pitch index.
        elif menuinput == '4':
            print("Feature Not Added Yet!")
            #TODO - Reverse Melodicon 
            ## Show the possible letter pairs of numeric scale degrees that are entered.
        elif menuinput == '5':
            print("Feature Not Added Yet!")
            #TODO - Restore Defaults !! THIS IS IMPORTANT
            ## Restore the OldLatin and B-Scale defaults.
        elif menuinput == '6':
            #Exit the Program
            menucheck += 1
            return
        else:
            print('Invalid Input. Try Again.')
            continue

#---------THE MELODICON-----------------
def themelodicon():
    print('''
    Welcome to the Melodicon!
    OldLatin is the default alphabet!
    (Invalid characters will be met with '%')
    U = V
    W = UU
    J = G
    ''')
    print(oldLatin)
    userMusicDictAM = makemusicalphabetbyhalf(oldLatin[0:12], twelvetoneScale)
    userMusicDictNZ = makemusicalphabetbyhalf(oldLatin[12:24], twelvetoneScale)
    userScale = makemusicscale(bTonicScale, twelvetoneScale)
    wordInput = input("Please enter a word, name, or phrase to convert: ")
    userReturn = compareuserinput(userMusicDictAM, userMusicDictNZ, wordInput)
    populatescaledegrees(userScale, userReturn)
    populatesolfege(solfegeDict, userReturn)
    createmidifile(userReturn)
    return
#------------MAIN----------------------
def __init__():
    mainmenu()

#--------BOILERPLATE------------#
__init__()
