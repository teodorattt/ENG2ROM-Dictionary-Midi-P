import json
import spacy
from spacy_syllables import SpacySyllables

nlp = spacy.load("en_core_web_sm")

nlp.add_pipe("syllables", after="tagger",config={"lang": "ro_RO"})

print("First we add nlp")

# open file in read mode
f = open('rodictionary.txt', 'r', encoding='utf-8')

print("Then we open the file and create the words list")

words = [x for x in f.readlines()]
#silabe = np.array([], dtype=object)
eng2rom = []
rolist = [words[r] for r in range(len(words)) if r == 0 or words[r] != words[r-1]]
f.close()

print("then we add the other arrays and close the file")

silabe = [[(token.text, token._.syllables, token._.syllables_count) for token in nlp(str(w))][0][1] for w in rolist]
#silabe = np.array([np.array([(token.text, token._.syllables, token._.syllables_count) for token in nlp(str(w))][1], dtype=object) for w in rolist], dtype=object)

#for w in rolist:
#    doc = nlp(str(w))
#    data = [(token.text, token._.syllables, token._.syllables_count) for token in doc]
#    silabe.append(data[0][1])

print("we finished adding silables from words to list")

for cuv in silabe:
    arpapron = ""
    if cuv != None and cuv != '':
        for j in range(len(cuv)):
            s = str(cuv[j])
            for i in range(len(s)):
                #litera a
                if s[i] in 'Aa':
                    if i+1 < len(s):
                        if s[i+1] in 'Ii':
                            arpapron += 'ay'
                        elif s[i+1] in 'Uu':
                            arpapron += 'aw'
                        else:
                            arpapron += 'aa'
                    else:
                        arpapron += 'aa'
                #litera b
                elif s[i] in 'Bb':
                    arpapron += 'b'
                #litera c
                elif s[i] in 'Cc':
                    if i+1 < len(s):
                        if s[i+1] in 'EIei':
                            arpapron += 'ch'
                        else:
                            arpapron += 'k'
                    else:
                        arpapron += 'k'
                #litera d
                elif s[i] in 'Dd':
                    if i+1 < len(s) - 1:
                        if s[i+1] in 'Rr':
                            arpapron += 'dr'
                        else:
                            arpapron += 'd'
                    else:
                        arpapron += 'd'
                #litera e
                elif s[i] in 'Ee':
                    if i+1 < len(s):
                        if s[i+1] in 'AOUaou':
                            if s[i-1] in 'CcGg' and i-1 >= 0:
                                arpapron += ''
                            else:
                                arpapron += 'eh'
                        elif s[i+1] in 'Ii':
                            arpapron += 'ey'
                        else:
                            arpapron += 'eh'
                    elif s == cuv[0] and i == 0:
                        if i+1 < len(s) - 1:
                            if s[i+1] in 'Aa':
                                arpapron += 'y'
                            else:
                                arpapron += 'y eh'
                        elif len(s) == 1:
                            arpapron += 'eh'
                        else:
                            arpapron += 'y eh'
                    else:
                        arpapron += 'eh'
                #litera f
                elif s[i] in 'Ff':
                    arpapron += 'f'
                #litera g
                elif s[i] in 'Gg':
                    if i+1 < len(s):
                        if s[i+1] in 'EIei':
                            arpapron += 'jh'
                        else:
                            arpapron += 'g'
                    else:
                        arpapron += 'g'
                #litera h
                elif s[i] in 'Hh':
                    if i-1 >= 0:
                        if s[i-1] in 'CcGg':
                            arpapron += ''
                        else:
                            arpapron += 'hh'
                    else:
                        arpapron += 'hh'
                #litera i
                elif s[i] in 'Ii':
                    if i > 0:
                        if s[i-1] in 'AEOaeo':
                            arpapron += ''
                        elif i < len(s) and s[i-1] in 'UĂÎÂuăîâ':
                            arpapron += 'y'
                        elif i == len(s) - 1 and s == cuv[-1]:
                            arpapron += 'y'
                        elif i+1 < len(s) and s[i+1] in 'AOUaou':
                            if s[i-1] in 'GgCc' and i > 0:
                                arpapron += ''
                            else:
                                arpapron += 'y'   
                        elif s == cuv[-1] and i == len(s) - 1:
                            if s[i-1] in 'CcGg':
                                arpapron += ''
                            elif s[i-1] in 'ȚțȘș':
                                arpapron += 'y'
                            else:
                                arpapron += 'ih'                                                     
                        else:
                            arpapron += 'iy'                 
                    elif i < len(s) - 1 and s[i+1] in 'AaEeOoUuĂă':
                        arpapron += 'y'
                    else:
                        arpapron += 'iy'
                #litera ă
                elif s[i] in 'Ăă':
                    if i+1 < len(s):
                        if s[i+1] in 'Rr':
                            arpapron += 'er'
                        elif s[i+1] in 'Uu':
                            arpapron += 'ow'
                        else:
                            arpapron += 'uh'
                    else:
                        arpapron += 'uh'
                #litera â si î
                elif s[i] in 'ÂâÎî':
                    arpapron += 'ax'
                #litera j
                elif s[i] in 'Jj':
                    arpapron += 'zh'
                #litera k
                elif s[i] in 'Kk':
                    arpapron += 'k'
                #litera l
                elif s[i] in 'Ll':
                    arpapron += 'l'
                #litera m
                elif s[i] in 'Mm':
                    arpapron += 'm'
                #litera n
                elif s[i] in 'Nn':
                    arpapron += 'n'
                #litera o
                elif s[i] in 'Oo':
                    if i+1 <= len(s) - 1:
                        if s[i+1] in 'Ii':
                            arpapron += 'oy'
                        else:
                            arpapron += 'ao'
                    else:
                        arpapron += 'ao'
                #litera p
                elif s[i] in 'Pp':
                    arpapron += 'p'
                #litera q
                elif s[i] in 'Qq':
                    if i+1 < len(s) - 1:
                        if s[i+1] in 'Uu':
                            arpapron += 'k y'
                        else:
                            arpapron += 'k'
                    else:
                        arpapron += 'k'
                #litera r
                elif s[i] in 'Rr':
                    if i > 0:
                        if s[i-1] in 'DTĂdtă':
                            arpapron += ''
                        else:
                            arpapron += 'r'
                    else:
                        arpapron += 'r'
                #litera s
                elif s[i] in 'Ss':
                    arpapron += 's'
                #litera ș
                elif s[i] in 'Șș':
                    arpapron += 'sh'
                #litera t
                elif s[i] in 'Tt':
                    if i+1 < len(s) - 1:
                        if s[i+1] in 'Rr':
                            arpapron += 'tr'
                        else:
                            arpapron += 't'
                    else:
                        arpapron += 't'
                #litera ț
                elif s[i] in 'Țț':
                    arpapron += 't s'
                #litera u
                elif s[i] in 'Uu':
                    if i > 0:
                        if s[i-1] in 'Ii':
                            arpapron += 'uw'
                        elif s[i-1] in 'AaĂă':
                            arpapron += ''
                        else:
                            arpapron += 'w'
                    else:
                        arpapron += 'w'
                #litera v si w
                elif s[i] in 'VvWw':
                    arpapron += 'v'
                #litera x
                elif s[i] in 'Xx':
                    arpapron += 'k s'
                #litera y
                elif s[i] in 'Yy':
                    arpapron += 'iy'
                #litera z
                elif s[i] in 'Zz':
                    arpapron += 'z'

                if i+1 == len(s)-1:
                    if s[i+1] in 'Ii' and s[i] in 'AEOaeo':
                        arpapron += ''
                    elif s[i+1] in 'Uu' and s[i] in 'AaĂă':
                        arpapron += ''
                    elif s[i] in 'EIei' and s[i-1] in 'CcGg':
                        if s[i+1] in 'AaOoUu':
                            arpapron += ''
                        else:
                            arpapron += ' '               
                    else:
                        arpapron += ' '
                elif i < len(s) - 1:
                    if s[i+1] in 'Hh' and s[i] in 'CcGg':
                        arpapron += ''
                    elif s[i+1] in 'Rr' and s[i] in 'TtDdĂă':
                        arpapron += ''
                    else:
                        arpapron += ' '
                else:
                    arpapron += ''

            if j < len(cuv) - 1:
                arpapron += ' '

    #eng2rom.append(arpapron)
    eng2rom.append(arpapron)

print("then we create arpabet pronontiation list for romanian words")

rodict = {}
rodict["data"] = []

print("then we create the rodict dictionary")

for i in range(len(rolist)):
    d = {}
    r = rolist[i].replace('\n', '')
    d["w"] = str(r)
    d["p"] = str(eng2rom[i])
    rodict["data"].append(d)


with open("ENG2ROM.json", "w", encoding='utf-8') as outfile: 
    json.dump(rodict, outfile, indent = 4)

print("we then add the words and their prononciation to a json file named ENG2ROM")