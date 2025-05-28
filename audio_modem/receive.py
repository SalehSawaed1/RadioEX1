from fsk_demod import fsk_demodulate, bits_to_text

def main():
    print("[⏳] Decoding from output.wav...")
    bits = fsk_demodulate("output.wav")
    print(f"[🧩] Raw bits: {''.join(map(str, bits))}")
    message = bits_to_text(bits)
    print(f"[📥] Decoded message: {message}")

if __name__ == "__main__":
    main()
