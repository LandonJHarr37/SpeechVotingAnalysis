# Write your code here :-)
"""
Speech analysis program
This program will take prominent speeches given by well-known
figures and give an impact level based on
Landon Harrison
vers - 09/25/2024
"""
from SpeechObject import SpeechObject

iHADSpeech = SpeechObject("iHADSpeechO", "I Have A Dream",
                                "Martin Luther King Jr.", "TRiHADSpeech_trimmed.txt", None)

iHADSpeech.reading()
iHADSpeech.reachVal()

iHADSpeech.printSO("iHADSpeech")

