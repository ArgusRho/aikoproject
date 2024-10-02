TTS_ON = False

def say(message):
    global TTS_ON  # Not strictly needed here, as you're not modifying it in this function
    # if TTS_ON flag is true, Initialize TTS with the downloaded model 
    if TTS_ON:
        from TTS.api import TTS #imported after it is checked TTS_ON because these imports are heavy for startup
        import sounddevice as sd 
        import numpy as np #looks like it is for audio data in numpy array

        tts = TTS(model_name = "tts_models/en/ljspeech/tacotron2-DDC")

        # Convert text to speech and save as a .wav file
        #tts.tts_to_file(text="Hello, this is a test using Coqui TTS.", file_path="says.wav")

        # Generate speech and get the audio output
        audio_data = tts.tts(text=message, return_audio=True)

        # Check if audio_data is a list and convert to a numpy array
        if isinstance(audio_data, list):
            audio_np = np.array(audio_data, dtype=np.float32)  # Convert list to NumPy array
        else:
            audio_np = np.frombuffer(audio_data, dtype=np.float32)  # If it's already bytes

        print(message)

        # Play the audio
        sd.play(audio_np, samplerate=22050)  # Adjust the samplerate if needed
        sd.wait()  # Wait until playback is finished

def tts_switching(switcher):
    global TTS_ON #by default, variables inside a function are local. use this to access global variable for this function. by declaring TTS_ON as global in the function, you lose the ability to create a local variable with the same name within this function.
    TTS_ON = switcher
    if TTS_ON:
        status = 'enabled'
    else:
        status = 'disabled'
    print(f"[process] TTS {status}")