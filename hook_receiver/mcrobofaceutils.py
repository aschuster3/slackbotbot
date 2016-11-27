#!/usr/bin/python
# mcroboface.py

import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 17      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 15      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Define various facial expressions
smileData   = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
winkData    = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
frownData   = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
grimaceData = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
oooohData   = [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
          
# Initialis the McRoboFace controllers
face = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
face.begin()

def clearFace():
  for i in range(0, face.numPixels()):
    face.setPixelColor(i, 0)
  face.show()                               

def showFace (data, Red, Green, Blue):
  for i in range(0, face.numPixels()):
    if (data[i] > 0):
      face.setPixelColor(i, Color(Green, Red, Blue))
    else:
      face.setPixelColor(i, 0)
  face.show()                               

def smile():
  try:
    clearFace()
    showFace(smileData, 0, 255, 0)
    time.sleep(5)

  finally:
    clearFace()

def wink():
  try:
    clearFace()
    showFace(smileData, 0, 255, 0)
    time.sleep(2)
    clearFace()
    showFace(winkData, 0, 255, 0)
    time.sleep(1)
    clearFace()
    showFace(smileData, 0, 255, 0)
    time.sleep(2)

  finally:
    clearFace()
