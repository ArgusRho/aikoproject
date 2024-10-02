import re #for regex search

#self made modules:
import transcriber_vosk as transcribe
import module_2024 as m2024
import tts_coqui as ttsc

def flip_TTS_ON_value():
    #By importing ttsc, you gain access to its global variable TTS_ON.
    ttsc.TTS_ON = not ttsc.TTS_ON  # Flip the value of TTS_ON boolean
    print(f"[process] TTS_ON is now: {ttsc.TTS_ON}")
    if ttsc.TTS_ON:
        ttsstatus = 'enabled'
    else:
        ttsstatus = 'disabled'
    print(f"[process] TTS is now {ttsstatus}")

def orders():
    listening = True
    while listening:
        print("AIKO: waiting for command.")
        order = transcribe.transcription_sequence()#recording
        if re.search(r'\bquit\b', order, re.IGNORECASE): #for keyword 'quit' in the `order` string
            listening = False #to exit the order-receiving loop
        elif re.search(r'\bvoice\b', order, re.IGNORECASE): #disable or enable tts.
            flip_TTS_ON_value()
            continue
        elif re.search(r'\bsay\b', order, re.IGNORECASE): 
            print("[process] initiating sentence-repeat.")
            m2024.sentence_repeat()
            continue
        elif re.search(r'\binternet\b', order, re.IGNORECASE):
            ttsc.say("the internet module is not yet added.")
            print("[warning] the internet module is not yet added.")
            continue
        else:
            available_orders = 'negative. please give the available orders: '
            available_orders += 'quit, voice, say, internet'
            ttsc.say(available_orders)
            print(f"AIKO: {available_orders}")
            continue