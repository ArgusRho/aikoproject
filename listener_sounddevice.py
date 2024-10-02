import sounddevice as sd 
import wave #saving audio data into wav file?

def record_audio(duration=5, fs=44100):
    """Record audio for a specified duration and sample rate."""
    print("[process] Recording Voice...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("[process] Recording finished.")
    return audio_data

def save_audio_to_wav(audio_data, filename='output.wav', fs=44100):
    """Save recorded audio data to a WAV file."""
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16 bits
        wf.setframerate(fs)
        wf.writeframes(audio_data.tobytes())
    print(f"Audio saved to {filename}.")
    return filename