#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Morse-Programm von
   Benjamin Müller
   Jonas Kanja
   Josefine Wieacker
   Pia Wilczoch  
   Original: https://github.com/Stevenchi36/LED-Morse-Code-for-Raspberry-Pi
"""

import RPi.GPIO as GPIO
import time

control_pin=11                           #Assign pin #11 to a variable
GPIO.setmode(GPIO.BCM)
GPIO.setup(control_pin, GPIO.OUT)

#Python dictionary containing characters and the matching morse code
converted = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--",":":"---...","?":"..--..","'":".----.","-":"-....-","/":"-..-.","(":"-.--.-",")":"-.--.-","\"":".-..-.","@":".--.-.","=":"-...-","[":"-.--.-","]":"-.--.-","$":"...-..-","+":".-.-.",";":"-.-.-.","_":"..--.-","!":"---."}

speedPercent = 30                       #Change to proportionately alter speed; 100 = Normal Speed; 50 = Half Speed
longTime = 30.0 / speedPercent           #Duration of the dash
shortTime = 10.0 / speedPercent          #Duration of the period
intraTime = 30.0 / speedPercent          #Duration of space between flash on same character
spaceTime = 200.0 / speedPercent          #Duration between words
betweenCharTime = 30.0 / speedPercent    #Duration between characters
inputString = ""

#Flash LED for the dash
def longFlash():
        print "."
        GPIO.output(control_pin, GPIO.HIGH)
        time.sleep(longTime)
        GPIO.output(control_pin, GPIO.LOW)

#Flash LED for the period
def shortFlash():
        print "-"
        GPIO.output(control_pin, GPIO.HIGH)
        time.sleep(shortTime)
        GPIO.output(control_pin, GPIO.LOW)

#Sleep for time of a space
def space():
    time.sleep(spaceTime)

#Ask for input
#returns the input
def getInput():
    return raw_input("Please enter text or type \"quit\" to exit: ")

#Make input lowercase and assign it to a variable
inputString = getInput().lower()
#While the input isn't "quit"
while (inputString != "quit"):
    #Go through each character of the input
    for c in inputString:
        #If it is a space
        if c == " ":
            space()
        #If it is in the dictionary
        elif c in converted:
            #convert character to the morse code
            morseconverted = converted[c]
            #goes through each character in the morse code
            for symbol in morseconverted:
                #If the symbol is a dash
                if symbol == "-":
                    longFlash()
                    time.sleep(intraTime)
                #If the symbol is a period
                elif symbol == ".":
                    shortFlash()
                    time.sleep(intraTime)
                #If the symbol is somehow not a dash or period
                else:
                    print "Not a '-' or '.'"
            time.sleep(betweenCharTime)
        #If the character is not supported in the dictionary
        else:
            print "'" + c + "'" + " is not a supported character"
    #Ask for input again
    inputString = getInput().lower()
