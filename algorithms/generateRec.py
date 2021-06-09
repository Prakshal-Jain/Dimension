import keyboard
import argparse
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback

left = [0]
right = [0]
isStop = [False]

def getAngle_intensity(angle):
    left[0] = (angle / 360)*100
    right[0] = 100 - left[0]
    print(left[0], right[0])

def stop():
    isStop[0] = True

def re_start():
    isStop[0] = False

def record(file):
    q = queue.Queue()
    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        for item in indata:
            item[0] = ((left[0]/100)*item[1])
            item[1] = ((right[0]/100)*item[1])
        q.put(indata.copy())

    channels = 2
    with sf.SoundFile(file, mode='x', samplerate=44100,
                        channels=channels, subtype=None) as file:
        with sd.InputStream(samplerate=44100, device=None,
                            channels=channels, callback=callback):
            while True:
                file.write(q.get())
                if isStop[0]:
                    print("Stopped Recordinggg!!")
                    q.queue.clear()
                    break