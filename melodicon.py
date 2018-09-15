import os.path
from pathlib import Path
#Local Mock Data and Dicts
OLDLATIN = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z', '&']
GREEK = ['\u0391','\u0392','\u0393', '\u0394', '\u0395', '\u0396', '\u0397', '\u0398', '\u0399', '\u039a', '\u039b', '\u039c', '\u039d', '\u039e', '\u039f', '\u03a0', '\u03a1', '\u03a3','\u03a4', '\u03a5', '\u03a6', '\u03a7', '\u03a8', '\u03a9']                        
GREEKCONV = ['a', 'v', 'y', 'd', 'e', 'z', 'ee', 'th', 'i', 'k', 'l', 'm', 'n', 'ks', 'o', 'p', 'r', 's', 't', 'u', 'f', 'ch', 'psi', 'oh']
FUTHARK = ['\u16A0', '\u16A2', '\u16A6', '\u16A8', '\u16B1', '\u16B2', '\u16B7',
           '\u16B9', '\u16BA', '\u16BE', '\u16C1', '\u16C3', '\u16C7', '\u16C8', '\u16C9', '\u16CB', '\u16CF', '\u16D2', '\u16D6', '\u16D7', '\u16DA', '\u16DC', '\u16DE', '\u16DF']
FUTHARKCONV = ['f', 'u', 'th', 'a', 'r', 'k', 'g', 'w', 'h', 'n', 'i', 'j', 'ae', 'p', 'z', 's', 't', 'b', 'e', 'm', 'l', 'ng', 'd', 'o']
twelvetoneScale = list(range(1, 13))
bTonicScale = ['B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb']
solfegeNames = ['do', 'di', 're', 'me', 'mi', 'fa', 'fi', 'sol', 'le', 'la', 'te', 'ti']
solfegeDict = dict(zip(twelvetoneScale, solfegeNames))
filepath = Path.cwd() / 'midis'
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

def makeunicodedict(alphabetListUnicodeConv, alphabetList):
    # Creates a Unicode Dict to convert Unicode based languages
    unicodedict = dict(zip(alphabetListUnicodeConv, alphabetList))
    return unicodedict

def compareuserinput(musicdictam, musicdictnz, userinput, alphabetList, globalTranspose):
    # Compare user input to selected music scale/alphabet and returns scale degrees
    import re
    returnedinput = []
    userinputed = userinput.replace(" ", "")
    userinputed = userinputed.replace(",", "")
    userinputed = re.sub("[^A-Za-z&]", "", userinputed)
    if alphabetList == OLDLATIN:
        translationinput = []
        userinputed = userinputed.upper()
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
                    pass
    elif alphabetList == GREEK:
        # Convert user input into alphabet like-sectors and then convert to unicode, then use the index to match the notes
        arrayConvDictAM = (makeunicodedict(GREEKCONV[0:12], GREEK[0:12]))
        arrayConvDictNO = (makeunicodedict(GREEKCONV[12:24], GREEK[12:24]))
        translationinput = []
        userinputed = userinputed.lower()
        for letter in userinputed:
                if letter in arrayConvDictAM.keys():
                    uniconvinput = (arrayConvDictAM.get(letter))
                    if uniconvinput in musicdictam.keys():
                            returnedinput.append(musicdictam.get(uniconvinput))
                            translationinput.append(arrayConvDictAM.get(letter))
                elif letter in arrayConvDictNO.keys():
                    uniconvinput = arrayConvDictNO.get(letter)
                    if uniconvinput in musicdictnz.keys():
                            returnedinput.append(musicdictnz.get(uniconvinput))
                            translationinput.append(arrayConvDictNO.get(letter))
                elif letter == 'h':
                    uniconvinput = arrayConvDictAM.get('ee')
                    if uniconvinput in musicdictam.keys():
                        returnedinput.append(musicdictam.get(uniconvinput))
                        translationinput.append(arrayConvDictAM.get('ee'))
                elif letter == 'c':
                    uniconvinput = arrayConvDictAM.get('k')
                    if uniconvinput in musicdictam.keys():
                        returnedinput.append(musicdictam.get(uniconvinput))
                        translationinput.append(arrayConvDictAM.get('k'))
                elif letter == 'g':
                    uniconvinput = arrayConvDictAM.get('y')
                    if uniconvinput in musicdictam.keys():
                        returnedinput.append(musicdictam.get(uniconvinput))
                        translationinput.append(arrayConvDictAM.get('y'))
                else:
                    if letter not in arrayConvDictAM.keys() or arrayConvDictNO.keys():
                        pass
                        translationinput.append('%')
        if 'rh' or 'rho' in userinputed:
          #Find Occurence of [value, value], then convert to [single value]
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('rh'):
                tIndex = tempreturnedinput.find('5')
                hIndex = tIndex + 1
                if '57' in tempreturnedinput:
                    # Find occurence of [57]
                    del translationinput[tIndex:hIndex+1]
                    translationinput.insert(tIndex, 'Ρ')
                    del returnedinput[tIndex:hIndex+1]
                    returnedinput.insert(tIndex, 5)
                    iterator += 1
                if '573' in tempreturnedinput:
                     # Find occurence of [5, %, 3]
                    del translationinput[tIndex:hIndex+2]
                    translationinput.insert(tIndex, 'Ρ')
                    del returnedinput[tIndex:hIndex+2]
                    returnedinput.insert(tIndex, 5)
                    iterator += 1
        if 'th' in userinputed:
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('th'):
                tIndex = tempreturnedinput.find('77')
                hIndex = tIndex + 1
                # Find occurence of [77]
                if '77' in tempreturnedinput:
                    del translationinput[tIndex:hIndex+1]
                    translationinput.insert(tIndex, 'Θ')
                    del returnedinput[tIndex:hIndex+1]
                    returnedinput.insert(tIndex, 8)
                    iterator += 1
        if 'ee' in userinputed:
          #Find Occurence of [value, value], then convert to [single value]
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('ee'):
                tIndex = userinputed.find('ee')
                hIndex = tIndex + 1
                # Find occurence of [55]
                if '55' in tempreturnedinput:
                    del translationinput[tIndex:hIndex+1]
                    translationinput.insert(tIndex, 'Η')
                    del returnedinput[tIndex:hIndex+1]
                    returnedinput.insert(tIndex, 7)
                    iterator += 1
        if 'ks' in userinputed:
          #Find Occurence of [value, value], then convert to [single value]
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('ks'):
                tIndex = tempreturnedinput.find('106')
                hIndex = tIndex + 1
                # Find occurence of [106]
                if '106' in tempreturnedinput:
                    del translationinput[tIndex:hIndex+1]
                    translationinput.insert(tIndex, 'Ξ')
                    del returnedinput[tIndex:hIndex+1]
                    returnedinput.insert(tIndex, 2)
                    iterator += 1
        if 'ch' in userinputed:
          #Find Occurence of [value, value], then convert to [single value]
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('ch'):
                tIndex = tempreturnedinput.find('107')
                hIndex = tIndex + 1
                # Find occurence of [107]
                if '107' in tempreturnedinput:
                    del translationinput[tIndex:hIndex+1]
                    translationinput.insert(tIndex, 'Χ')
                    del returnedinput[tIndex:hIndex+1]
                    returnedinput.insert(tIndex, 10)
                    iterator += 1
        if 'psi' in userinputed:
          #Find Occurence of [value, value, value], then convert to [single value]
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('psi'):
                tIndex = tempreturnedinput.find('469')
                hIndex = tIndex + 1
                # Find occurence of [469]
                if '469' in tempreturnedinput:
                    del translationinput[tIndex:hIndex+2]
                    translationinput.insert(tIndex, 'Ψ')
                    del returnedinput[tIndex:hIndex+2]
                    returnedinput.insert(tIndex, 11)
                    iterator += 1
        if 'oh' in userinputed:
          #Find Occurence of [value, value], then convert to [single value]
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('oh'):
                tIndex = userinputed.find('oh')
                hIndex = tIndex + 1
                # Find occurence of [37]
                if '37' in tempreturnedinput:
                    del translationinput[tIndex:hIndex+1]
                    translationinput.insert(tIndex, 'Ω')
                    del returnedinput[tIndex:hIndex+1]
                    returnedinput.insert(tIndex, 12)
                    iterator += 1
    elif alphabetList == FUTHARK:
        # Convert user input into alphabet like-sectors and then convert to unicode, then use the index to match the notes
        uniconvinput = list
        translationinput = []
        arrayConvDictFJ = (makeunicodedict(FUTHARKCONV[0:12], FUTHARK[0:12]))
        arrayConvDictAEO = (makeunicodedict(FUTHARKCONV[12:24], FUTHARK[12:24]))
        userinputed = userinputed.lower()
        for letter in userinputed:
            if letter in arrayConvDictFJ.keys():
                uniconvinput = (arrayConvDictFJ.get(letter))
                if uniconvinput in musicdictam.keys():
                        returnedinput.append(musicdictam.get(uniconvinput))
                        translationinput.append(arrayConvDictFJ.get(letter))
            elif letter in arrayConvDictAEO.keys():
                uniconvinput = arrayConvDictAEO.get(letter)
                if uniconvinput in musicdictnz.keys():
                        returnedinput.append(musicdictnz.get(uniconvinput))
                        translationinput.append(arrayConvDictAEO.get(letter))
            else:
                if letter not in arrayConvDictFJ.keys() or arrayConvDictAEO.keys():
                    pass
                    translationinput.append('%')
        if 'th' in userinputed:
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('th'):
                tIndex = tempreturnedinput.find('59')
                hIndex = tempreturnedinput.find('59') + 1
                if '559' in tempreturnedinput:
                    tIndex = tempreturnedinput.find('59')    
                if tIndex == (hIndex - 1):
                    # Find occurence of [59] and replace with [3]
                    if '59' in tempreturnedinput:
                        tempreturnedinput = tempreturnedinput.replace('59','', 1)
                        temptranslationinput = temptranslationinput.replace('ᛏᚺ', '', 1)
                        translationinput.remove('ᛏ')
                        translationinput.remove('ᚺ')
                        translationinput.insert(tIndex, 'ᚦ')
                        returnedinput.remove(5)
                        returnedinput.remove(9)
                        returnedinput.insert(tIndex, 3)
                        iterator += 1
        if 'ae' in userinputed:
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('ae'):
                tIndex = tempreturnedinput.find('4')
                hIndex = tIndex + 1
                        # Find occurence of [47] and replace with [1]
                if '47' in tempreturnedinput:
                    del translationinput[tIndex:hIndex+1]
                    translationinput.insert(tIndex, 'ᛇ')
                    del returnedinput[tIndex:hIndex+1]
                    returnedinput.insert(tIndex, 1)
                    iterator += 1            

        if 'ng' in userinputed:
            iterator = 0
            tempreturnedinput = ''.join(map(str, returnedinput))
            temptranslationinput = ''.join(map(str, translationinput))
            while iterator < userinputed.count('ng'):
                tIndex = tempreturnedinput.find('10')
                hIndex = tIndex + 1
            # Find occurence of [107] and replace with [10]
                if '107' in tempreturnedinput:
                    del translationinput[tIndex:hIndex+1]
                    translationinput.insert(tIndex, 'ᛜ')
                    del returnedinput[tIndex:hIndex+1]
                    returnedinput.insert(tIndex, 1)
                    iterator += 1
    else:
        print('Error, defaulting to Old Latin!')
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
                    pass
    print('\nIndex/Scale Degrees:')
    print(returnedinput)
    transposeInput = returnedinput
    if globalTranspose != 0:
        for degree in range(len(transposeInput)):
            transposeInput[degree] = transposeInput[degree] + abs(globalTranspose)
            if transposeInput[degree] > 12:
                transposeInput[degree] -= 12
        print('\n$$$ Transposition Degrees $$$')
        print(transposeInput)
        returnedinput = transposeInput
    else:
        pass
    if alphabetList == GREEK:
        print(translationinput)
        print(''.join(map(str, translationinput)))
        print('\nYour Input: ' + userinputed)
    if alphabetList == FUTHARK:
        print(translationinput)
        print(''.join(map(str, translationinput)))
        print('\nYour Input: ' + userinputed)
    if alphabetList == OLDLATIN:
        print('\nYour Input: ' + userinput)
        print(' - '.join(userinputed) + '\n')
    else:
        pass
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

def createmidifile(scaledegrees, filepath):
    # Convert user input to midi file.
    savecheck = 0
    import os
    import os.path
    from pathlib import Path
    p = str(filepath)
    while savecheck == 0:
        defaultpath = os.getcwd()
        print('Current directory')
        print(defaultpath)
        usersave = input("Create MIDI File? (Y/N): ")
        usersave = usersave.upper()
        if usersave == "Y":
            if os.path.exists(filepath) == True:
                os.chdir(p)
                print("Inside Directory")
            if os.path.exists(filepath) == False:
                print('Creating Directory')
                os.makedirs(p)
                os.chdir(p)
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

#  MENU
def mainmenu():
    menucheck = 0
    tonicScale = []
    userAlphabet = []
    userchangedTransposition = [0,1,2,3,4,5,6,7,8,9,10,11]
    userchangedScale = []
    globalTranspose = 0
    if tonicScale == [] and userAlphabet == []:
        tonicScale = bTonicScale
        userAlphabet = OLDLATIN
    else:
        tonicScale = userchangedScale
        if userAlphabet == [] or OLDLATIN:
            userAlphabet = OLDLATIN
        else:
            menuinput = 2
    while menucheck == 0:
        print('''Welcome to the Melodicon! Choose your menu option below:
            1) Convert Words/Phrases/Names
            2) Change Alphabet
            3) Change Scale Tonic
            4) Restore Defaults
            5) Exit''')
        menuinput = input("Enter a number to select an option: ")
        if menuinput == '1':
            if globalTranspose == 0 and tonicScale[0] != 'B':
                print('''
                Be careful, you must have really messed around with your settings. 
                ''')
            # OPTION 1 - THE MELODICON
            repeatcheck = 0
            while repeatcheck == 0:
                themelodicon(tonicScale,userAlphabet, globalTranspose)
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
         # OPTION 2 -Change the default alphabet from 'Old Latin' to a different lexical index.
         inputCheck = 0
         alphaSelectCheck = 0
         while alphaSelectCheck == 0:
            print('''
            ## Select a Number to Choose an Alphabet ##
                1) Old Latin
                2) Greek
                3) Elder Futhark ''')
            userAlphaSelect = input("What alphabet would you like to select?: ")
            while inputCheck == 0:
                if userAlphaSelect == "":
                    userAlphabet = OLDLATIN
                    alphaSelectCheck += 1
                try:
                    userAlphaSelect = int(userAlphaSelect)
                    inputCheck += 1
                except ValueError:
                    print('''Invalid Option. Please Try Again.
                
                            ## Select a Number to Choose an Alphabet ##
                                1) Old Latin
                                2) Greek
                                3) Elder Futhark ''')
                    userAlphaSelect = input("What alphabet would you like to select?: ")
                    continue
                if userAlphaSelect == 1:
                    userAlphaSelect = OLDLATIN
                    print("Your alphabet is now Old Latin!" + "\n")
                    print(OLDLATIN)
                    alphaSelectCheck +=1
                    inputCheck += 1
                    break
                elif userAlphaSelect == 2:
                    userAlphaSelect = GREEK
                    print("Your alphabet is now Greek!" + "\n")
                    print(GREEK)
                    alphaSelectCheck += 1
                    break
                elif userAlphaSelect == 3:
                    userAlphaSelect = FUTHARK
                    print("Your alphabet is now Futhark!" + "\n")
                    print(FUTHARK)
                    alphaSelectCheck +=1
                    break
                elif userAlphaSelect == '':
                    userAlphabet = OLDLATIN
                    print('Defaulting to Old Latin' + "\n")
                    alphaSelectCheck += 1
                    break
                else: 
                    inputCheck = 0
                    print('''Invalid Option. Please Try Again.
                
                            ## Select a Number to Choose an Alphabet ##
                                1) Old Latin
                                2) Greek
                                3) Elder Futhark ''')
                    userAlphaSelect = input("What alphabet would you like to select?: ")
                    continue
            userAlphabet = userAlphaSelect
            if userAlphabet == 0:
                userAlphabet = OLDLATIN
            
        elif menuinput == '3':
            # OPTION 3 Change the scale tonic of the Melodicon
            inputCheck = 0
            changeCheck = 0
            from collections import deque
            if tonicScale == []:
                tonicScale = bTonicScale
                s = deque(tonicScale)
                t = deque(userchangedTransposition)
                print("Your Current Scale: " + str(list(s)))
            else:
                s = deque(tonicScale)
                t = deque(userchangedTransposition)
                print("Your Current Scale: " + str(list(s)))
            # Change the default tonic note from 'B' to another 12-tone pitch index.
            while changeCheck == 0:
                changescale = input(
                    "\nWhich note would you like to change your tonic to?: \n New Tonic (Move in semitones): " + "\n")
                while inputCheck == 0:
                    if changescale == str(''):
                        changeCheck += 1
                        inputCheck += 1
                    else:
                        try:
                            changescale = int(changescale)
                            inputCheck += 1
                        except ValueError:
                            print("Invalid input, not an integer! Try again.")
                            changescale = input(
                                "\nWhich note would you like to change your tonic to?: \n New Tonic (Move in semitones): " + "\n")
                            inputCheck = 0
                            continue
                        changescale = -int(changescale)
                        if changescale <= 12 and changescale >= -12:
                            if changescale == 0:
                                print("\nYour Scale did not change.")
                                changeCheck =+ 1
                                break
                            else:
                                s.rotate(changescale)
                                t.rotate(changescale)
                                userchangedScale = list(s)
                                userchangedTransposition = list(t)
                                print("\nYour New Scale: " + str(list(userchangedScale)))
                                tonicScale = userchangedScale
                                globalTranspose = userchangedTransposition[0]
                                # globalTranspose = userchangedTransposition[0].value
                                changeCheck =+ 1
                                break
                        else:
                            print(
                                "Invalid Input, please enter an integer within -12 to 12" + "\n")
                            inputCheck = 0
                            changescale = input(
                                "\nWhich note would you like to change your tonic to?: \n New Tonic (Move in semitones): "  + "\n")
                            continue 
                                    
        elif menuinput == '4':
            # OPTION  4 Restore the OldLatin and B-Scale defaults.
            tonicScale = bTonicScale
            userAlphabet = OLDLATIN
            globalTranspose = 0
            print("Default settings restored.\n")

        elif menuinput == '5':
            # OPTION 5 Exit the Program
            menucheck += 1
            return
        else:
            print('Invalid Input. Try Again.')
            continue
#---------THE MELODICON-----------------
def themelodicon(tonicScale, alphabetList, globalTranspose):
    print("\nWelcome to the Melodicon!\n")
    print("Visit: https://github.com/poruvo/melodicon/edit/master/README.md for instructions.")
    if alphabetList == OLDLATIN:
        print('''\n(Invalid characters will removed.)
                U = V
                W = UU
                J = G
                ---
                A B C D E F G H I  K  L  M
                1 2 3 4 5 6 7 8 9 10 11 12
                N O P Q R S T V X  Y  Z  &
                ---
                ''')
        print("Your alphabet is Old Latin!")
    else: 
        if alphabetList == GREEK:
            print('''\n(Invalid characters will removed.)
            H = EE
            C = K
            G = Y
            OH = Omega
            ---
            Α Β Γ Δ Ε Ζ Η Θ Ι  Κ  Λ  Μ
            1 2 3 4 5 6 7 8 9 10 11 12
            Ν Ξ Ο Π Ρ Σ Τ Υ Φ  Χ  Ψ  Ω
            ---
            ''')
            print(("Your alphabet is Greek!") + str(alphabetList))
        elif alphabetList == FUTHARK:
            print('\n(Invalid characters will be removed)')
            print('''
            ----
            ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ ᚷ ᚹ ᚺ  ᚾ   ᛁ  ᛃ
            1 2 3 4 5 6 7 8 9 10 11 12
            ᛇ ᛈ ᛉ ᛋ ᛏ ᛒ ᛖ ᛗ ᛚ  ᛜ  ᛞ  ᛟ
            ---
            ''')
            print(("Your alphabet is Futhark!"))
    userMusicDictAM = makemusicalphabetbyhalf(alphabetList[0:12], twelvetoneScale)
    userMusicDictNZ = makemusicalphabetbyhalf(alphabetList[12:24], twelvetoneScale)
    userScale = makemusicscale(tonicScale, twelvetoneScale)
    print("### (Your Scale Tonic is " + tonicScale[0] + ') ###')
    wordInput = input("Please enter a word, name, or phrase to convert: ")
    userReturn = compareuserinput(userMusicDictAM, userMusicDictNZ, wordInput, alphabetList, globalTranspose)
    populatescaledegrees(userScale, userReturn)
    populatesolfege(solfegeDict, userReturn)
    createmidifile(userReturn, filepath)
    return
#------------MAIN----------------------
def __init__():
    mainmenu()
#--------BOILERPLATE------------#
__init__()
