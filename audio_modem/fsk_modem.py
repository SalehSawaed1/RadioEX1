import numpy as np
from scipy.io.wavfile import write

def text_to_bits(text):
    preamble = '10101010' * 2  # for sync
    bits = ''.join(f'{ord(c):08b}' for c in text)
    return preamble + bits

def fsk_modulate(bits, sample_rate=44100, baud_rate=20, f0=1000, f1=2000):
    samples_per_bit = sample_rate // baud_rate
    signal = []

    for bit in bits:
        freq = f1 if bit == '1' else f0
        t = np.linspace(0, 1, samples_per_bit, endpoint=False)
        wave = np.sin(2 * np.pi * freq * t)
        signal.extend(wave)

    signal = np.array(signal)
    signal /= np.max(np.abs(signal))  # Normalize
    return (signal * 32767).astype(np.int16)

def save_audio(audio, filename, sample_rate=44100):
    write(filename, sample_rate, audio)
    print(f"[✓] Saved modulated audio to {filename}")
