import numpy as np
import matplotlib.pyplot as plt
import wave as wv
import librosa as lb
import soundfile as sf


class FrameGenerator:
    def __init__(data_buffer, sample_rate:int):
        self.data_buffer=data_buffer
        self.sample_rate=sample_rate
