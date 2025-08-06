import sounddevice as sd
import queue
import vosk
import json
import re


import csv

club_info = {}
with open("DRC.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        club_info[row['Field']] = row['Info']

 
system_prompt = "You are a bilingual helpful assistant for a drone and robotics club. You speak arabic and english. Always respond in short and concise manner. Reply in english when asked in english and in arabic when asked in arabic If the user says goodbye or anything similar, respond 'see you later' only.  Use this info:\n"
for key, value in club_info.items():
    system_prompt += f"{key}: {value}\n"


import pvporcupine
import pyaudio
import struct
while True:
    porcupine = pvporcupine.create(access_key="RjpL28S8sWCo6LE7RXKPosMZrKPSQdgnhdMJgqqByGXTP23AkvN0Jg==", #need regenrating each key with 7days trial 
                               #    keyword_paths=["/Users/doa/Downloads/abdul_en_raspberry-pi_v3_0_0/abdul_en_raspberry-pi_v3_0_0.ppn"]) # for pi 
        keywords=["alexa"])  # or custom wake word
    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)

    print("Listening for wake word...")

    while True:
        pcm = stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Wake word detected!")
            break  

    # brew install wget
    # wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
    # unzip vosk-model-small-en-us-0.15.zip

    model = vosk.Model("vosk-model-small-en-us-0.15")


    generated_text =''
    
    while "see you" not in generated_text.lower():
        q = queue.Queue()
        def callback(indata, frames, time, status):
            q.put(bytes(indata))

        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                            channels=1, callback=callback):
            rec = vosk.KaldiRecognizer(model, 16000)
            print("Speak into the mic...")
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result_dict = json.loads(rec.Result())  # dict
                    text = result_dict.get("text", "").strip()  # string
                    break
            






        import os
        from openai import OpenAI

        endpoint = "https://models.github.ai/inference"
        model_name = "openai/gpt-4.1-nano"
        token="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"


        client = OpenAI(
            base_url=endpoint,
            api_key=token,
        )
    
        response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text},
                ],
                temperature=1.0,
                max_tokens=1000,
                model=model_name,
            )

        generated_text=response.choices[0].message.content

        from gtts import gTTS
        import os

        # Text-to-speech output # we will use Yazan Model

        tts = gTTS(generated_text, lang='en')

        print(generated_text)
        tts.save("speech.mp3")
        os.system("mpg321 speech.mp3")  # use afplay on macOS if mpg321 not installed
