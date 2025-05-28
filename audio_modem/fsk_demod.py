import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter

def bandpass_filter(data, lowcut, highcut, fs, order=6):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)

def fsk_demodulate(filename, mark_freq=2000, space_freq=1000, baud_rate=20):
    sample_rate, data = wavfile.read(filename)
    if len(data.shape) > 1:
        data = data[:, 0]
    data = data.astype(np.float32)
    samples_per_bit = sample_rate // baud_rate
    num_bits = len(data) // samples_per_bit
    bits = []

    for i in range(num_bits):
        chunk = data[i * samples_per_bit:(i + 1) * samples_per_bit]
        f0_energy = np.sum(bandpass_filter(chunk, space_freq - 150, space_freq + 150, sample_rate)**2)
        f1_energy = np.sum(bandpass_filter(chunk, mark_freq - 150, mark_freq + 150, sample_rate)**2)
        bits.append(1 if f1_energy > f0_energy else 0)

    return bits

def bits_to_text(bits):
    # Skip the 16-bit preamble
    chars = []
    i = 16
    while i + 8 <= len(bits):
        byte = bits[i:i+8]
        val = int(''.join(map(str, byte)), 2)
        chars.append(chr(val) if 32 <= val <= 126 else '?')
        i += 8
    return ''.join(chars)
