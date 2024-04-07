# ENG2ROM-Dictionary-Midi-P
A Romanian words to English arpabet phonemes dictionary for Synthesizer V by Midi-P (me).

This dictionary was generated with the help of the Python add-on, spacey-syllables (https://github.com/sloev/spacy-syllables/blob/master/README.md) and a list of all 190000+ Romanian words (rodictionary.txt).
The code used is in the rolang.py file, in case someone wants to modify it.

# Installing and using the dictionary

Download the ENG2ROM.json file, then put it in the english-arpabet folder, in the japanese-romaji and in the mandarin-xsampa (if there are other languages, like spanish and cantonese, put in those folders too) from the dicts folder in Synthesizer V, right under the databases folder. Open Synthesizer V and go to the Dictionary panel, then select a database that supports English (native or cross-lingual) and click "New" in the Dictionary panel. For each language supported ("english" and "arpabet", "japanese" and "romaji", "mandarin" and "xsampa", etc.), write "ENG2ROM", then save.

To use the dictionary, simply click the ENG2ROM dictionary and set the singing language to English for the chosen voicebank, then type the Romanian words, diacritics included (note that 'ș' and 'ț' do not appear in the entered lyrics, but the sounds they represent, 'sh' and 't s', appear in the phonetic tranlation and they work, so don't worry).

# Warning: THIS IS NOT A PLUG-AND-PLAY SOLUTION. Phoneme adjustement is needed for some syllables to sound better.
