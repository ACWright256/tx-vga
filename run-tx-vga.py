from src.python.constants.constants import PYDIR
print(PYDIR)


import numpy as np
import matplotlib.pyplot as plt
import wave as wv
import librosa as lb
import soundfile as sf

def main():
    SR=44100
    x_domain=np.arange(0,200,0.5)
    test_sine=np.sin(x_domain)
    sf.write("test.wav",test_sine, SR)

if __name__ == '__main__':
    main()