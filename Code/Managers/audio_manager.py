import pyaudio, numpy as np
from scipy.fft import fft


class audioManager:

    def __init__(self):

        self.FORMAT = pyaudio.paInt16  # Audio format
        self.CHANNELS = 1             # Mono audio input
        self.RATE = 44100             # Sample rate (samples per second)
        self.CHUNK = 512      # Number of audio frames per buffer

        self.AUDIO = pyaudio.PyAudio()

        self.STREAM = self.AUDIO.open(self.RATE, self.CHANNELS, self.FORMAT, True, self.CHUNK)

        self.audio_volume    = 0
        self.audio_frequency = 0

        self.calibrate_background_noise()

        self.recording = True

    def calibrate_background_noise(self):



        data = self.STREAM.read(44100 * 4)
        audio_data = np.frombuffer(data, dtype=np.int16)

        self.bg_noise = audio_data.max()


    def find_peak_frequency(self, data, rate):

        n = len(data)
        freqs = np.fft.fftfreq(n, 1.0 / rate)
        magnitudes = abs(fft(data))
        peak_frequency = freqs[np.argmax(magnitudes)]

        return abs(peak_frequency)
    
    def find_volume(self, data):

        return np.abs(data).mean()
    
        #whaaat

    def handle_data(self):

       while self.recording:

            data = self.STREAM.read(self.CHUNK)

            audio_data = np.frombuffer(data, dtype=np.int16)

            self.audio_volume = self.find_volume(audio_data)
            self.audio_frequency = self.find_peak_frequency(audio_data, self.RATE)
    
    def get_frequency(self):

        return self.audio_frequency
    
    def get_volume(self):

        return self.audio_volume
    
    def terminate_streaming(self):

        self.recording = False
        