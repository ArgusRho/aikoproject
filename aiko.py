print("=============== A.I.K.O. voice assistant by [ArgusRho] ===============")

import re #for regex search
import tts_coqui as ttsc

def tts_switcher():
    choice = input("AIKO: use Text To Speech? (y/n): ")
    if choice == 'n':
        switching = False
        ttsc.tts_switching(switching)
    else:
        switching = True
        ttsc.tts_switching(switching)

tts_switcher() #disable or enable tts. I put this disabling here because tts is heavy to load.

#self made modules:
import commands as cm
import transcriber_vosk as transcribe

def detect_hello(transcription):
    """Detect the word 'hello' in the transcription."""
    print(f"Checking transcription: {transcription}")  # Debug print to see the transcription

    # Use regex to search for the word 'hello' (case-insensitive)
    if re.search(r'\bhello\b', transcription, re.IGNORECASE):
        message = "The hello wake call detected in the transcription. Aiko stand by."
        print(f"AIKO: {message}")
        ttsc.say(message)
        return True
    else:
        message = "wake call is not detected"
        print(f"AIKO: {message}")
        ttsc.say(message)
        return False

def main():
    transcription = transcribe.transcription_sequence()#recording
    print(f"Transcription result: {transcription}")  # Debug print to confirm transcription before detection
    
    hello_detection = False
    if transcription:# If there is transcription, check for the word "hello" using detect_hello function
        hello_detection = detect_hello(transcription) #returns true or false
    if (hello_detection):
        cm.orders()
    else: {
        print("AIKO: the program does not detect any words said in 5 seconds, or the wake call is not said. shutting down...")
    }

if __name__ == "__main__":
    main()
