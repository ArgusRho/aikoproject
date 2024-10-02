#expandable random functionality module
import re #for regex search

#self made modules:
import transcriber_vosk as transcribe
import tts_coqui as ttsc

def sentence_repeat():
    """repeats the sentence you said like parrot"""
    Active = True
    while Active:
        transcription = transcribe.transcription_sequence()
        if re.search(r'\bquit\b', transcription, re.IGNORECASE): #for keyword 'quit' in the `transcription` string
            print("AIKO: quit order received. back to command selection.")
            Active = False
        elif transcription:
            print("[process] sentence-repeat sequence running.")
            extracted_vosk = transcribe.extract_vosk_json(transcription)
            print(f"[process] extracted vosk: {extracted_vosk}")
            ttsc.say(extracted_vosk)
            continue