# Simple QRSS keyer in CircuitPython

# import packages
import board
import digitalio
import time

keyerout = digitalio.DigitalInOut(board.GP0)  # GP0 output keying on/off or FSK the transmitter
keyerout.direction = digitalio.Direction.OUTPUT
keyerout.value = False

dit = 6 # the common QRSS dit is 6s long
dah = 3*dit
btwditdah = dit
btwchar = 2*dit
wordspace = 6*dit


morseabc = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}



callsign = "HA7TP".upper()
while True:
    for letter in callsign:
        for element in morseabc[letter]:
            if element == ".":
                keyerout.value = True
                time.sleep(dit)
                keyerout.value = False
                time.sleep(btwditdah)
            else:
                keyerout.value = True
                time.sleep(dah)
                keyerout.value = False
                time.sleep(btwditdah)
        time.sleep(btwchar)
    time.sleep(wordspace)