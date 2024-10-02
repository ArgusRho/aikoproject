[README](../README.md)
# resources
https://docs.anaconda.com/miniconda/ \
cmd codes to install stuff (needs pip and conda installed first):
- pip install vosk
- conda install sounddevice 

download:
- https://alphacephei.com/vosk/models 

# Coqui TTS
use this en one:
```
tts --text "I want some pizza" --model_name "tts_models/en/ljspeech/tacotron2-DDC" --vocoder_name "vocoder_models/ja/kokoro/hifigan_v1" --out_path C:\Users\ASUS\Downloads
```
it is downloaded to this directory after you write these tts codes above:

`C:\Users\ASUS\AppData\Local\tts`

those codes are not for downloading the model but those are the ones worked to download it. found the command on command line after I write their documentation command.

we will use the one I found on gpt instead, `tts_models/en/ljspeech/tacotron2-DDC`. this en model is just 100mb and requires no vocoder (800mb) download like the jp one. but maybe this uses the previous vocoder i downloaded for jp? but they say not all vocoder is interchangeable.

I misdownload. lucky we have gpt saying the name of the en female model.

little note, this jp one is male and it is big:
```
tts --text "I want some pizza" --model_name "tts_models/ja/kokoro/tacotron2-DDC" --vocoder_name "vocoder_models/ja/kokoro/hifigan_v1" --out_path C:\Users\ASUS\Downloads
```
this jp is 1.3gb and cant read en words.

# vosk
so my guess the vosk differentiate noise with voice using difference ratio. so if the recording ends while you still talking your voice will be cancelled because it counts as noise, it has no actual silence to compare the ratio to. idk Im noob.