from fsk_modem import text_to_bits, fsk_modulate, save_audio
import matplotlib.pyplot as plt

def main():
    text = input("Enter message to encode (max 32 characters): ").strip()
    if len(text) < 1 or len(text) > 32:
        print("❌ Message length invalid.")
        return

    bits = text_to_bits(text)
    print(f"[INFO] Bitstream: {bits}")

    audio = fsk_modulate(bits)
    save_audio(audio, "output.wav")

    # Optional waveform plot
    plt.plot(audio[:2000])
    plt.title("FSK Signal (First 2000 Samples)")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
