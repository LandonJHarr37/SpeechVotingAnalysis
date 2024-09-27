# Write your code here :-)
"""
Speech Object
This class will create a speech object that will
hold a speech and relevant information
Landon Harrison
vers - 09/26/2024
"""

class SpeechObject:
    def __init__ (tR, obName, name, speaker, textFile, reach):
        tR.textFile = textFile
        tR.reach = None

    def reading(tR):
        with open(tR.textFile, "r", encoding= 'utf-8') as tR.name:
            content = tR.name.read()
        return content

    def reachVal(tR):
        if (tR.reach == None):
            tR.reach = input("How many people did this speech reach?" +
                            "\nEnter here: ")
        else:
            print("already filled out")

    def printSO(tR, nameA):
        print("Speech name is: (iHADSpeech)"+
                ", Speech reach was: (" + str(tR.reach) + ").")

