from pathlib import Path
import openai
from dotenv import dotenv_values
import speech_recognition as sr

config = dotenv_values(".env")
openai.api_key = config.get("API_KEY")
async def getCompletion(prompt, model="gpt-3.5-turbo"):
    print("Creating response...")
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content

def generateImage(prompt):
    print("Generating image...")
    return openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        n=1
    ).data[0].url

def recordAudio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = sr.Recognizer().listen(source)
    return audio

def getTranscript(audioFile):
    return openai.audio.transcriptions.create(
        model="whisper-1",
        file=Path(audioFile.name)
    ).text

def getSpeech(prompt, model="tts-1", filePath="speechSample.mp3"):
    open(filePath, "wb")
    openai.audio.speech.create(
        model=model,
        voice="onyx",
        input=prompt
    ).write_to_file(Path(filePath))

async def chatTalking(prompt, chatAmount=3):
    text = ""
    for _ in range(chatAmount):
        print(prompt)
        prompt = await getCompletion(prompt)
        text += prompt + "\n\n"
        print(prompt)
        prompt = await getCompletion(prompt)
        text += prompt + "\n"
    return text

def getFileContent(fileName):
    output = ""
    with open(fileName, "r") as file:
        for item in file.readlines():
            output += item + "\n"
    return output