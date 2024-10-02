from vosk import Model, KaldiRecognizer
import wave #saving audio data into wav file?
import json #to handle data from vosk
import os #for file deletion and management

#self made modules:
import listener_sounddevice as listen

def transcribe_audio(filename='output.wav'):
    """Transcribe audio from a WAV file using Vosk."""
    if not os.path.exists("vosk-model"):
        print("[warning] Please download the Vosk model and extract it to the 'vosk-model' folder.")
        return ""

    model = Model("vosk-model")
    recognizer = KaldiRecognizer(model, 44100)

    transcription = ""
    
    with wave.open(filename, 'rb') as wf:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print(f"[process] Raw result: {result}")  # Print the raw result
                result_text = extract_text(result)
                if result_text:  # Only append non-empty results
                    print(f"[process] Extracted text: {result_text}")
                    transcription += result_text + " "  # Append text with space
    
    # Skip the final result as it's not providing useful output in this case
    return transcription.strip()  # Strip any leading/trailing spaces

def extract_text(result_json): #take the entire raw data with labels
    print("[process] taking the entire vosk json result.")
    if 'text' in result_json: #apparently vosk's raw result have '"text" :' in it
        print("[process] extracting...") #for debugging if this code runs
        return result_json
    return ""

def extract_vosk_json(raw): #only take the sentence text
    """Extract the transcription text from the result JSON."""
    print("[process] extracting transcription from vosk json.")
    result = json.loads(raw)
    text = result.get('text', '')
    return text

#record and transcription mainly uses this one
def transcription_sequence():
    duration = 5  # Record for 5 seconds
    audio_data = listen.record_audio(duration)
    wav_filename = listen.save_audio_to_wav(audio_data)
    transcription = transcribe_audio(wav_filename)
    # Delete the temporary WAV file
    os.remove(wav_filename)
    print(f"[process] deleted temporary file: {wav_filename}")
    return transcription

def transcription_sequence_custom_time(time):
    duration = time
    audio_data = listen.record_audio(duration)
    wav_filename = listen.save_audio_to_wav(audio_data)
    transcription = transcribe_audio(wav_filename)
    # Delete the temporary WAV file
    os.remove(wav_filename)
    print(f"[process] deleted temporary file: {wav_filename}")
    return transcription