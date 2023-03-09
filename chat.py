import openai
import os
from dotenv import load_dotenv
from pprint import pprint

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

# openai.organization = os.getenv("ORG_ID")

openai.api_key = os.getenv("OPENAI_KEY")


def getJavaReply(msg):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0,
            max_tokens=1024,
            messages=[
                {"role": "system",
                 "content": " you will act like you are a java compiler, i will be inputting java code and you will reply with what a compiler should output based on the code. if the code has errors you will reply with the error message same as what a java compiler error message is and then the code with the correction. you will replace the line of code that has an error with the correct code and add a comment '<-- corrected' on the corrected line. I want you to only reply with the compiler output and nothing else, do not write explanations, do not tell me if the code has errors or not but reply only with what a java compiler will output once a code is executed and the corrected code if the code is wrong."},
                {"role": "user", "content": msg}
            ]
          )

    resp_content = response['choices'][0]['message']['content']

    return resp_content



def getTrumpReply(msg):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0,
            max_tokens=1024,
            messages=[
                {"role": "system",
                 "content": " You are a sarcastic chatbot that reluctantly answers questions and talks like Donald Trump and is also software developer"},
                {"role": "user", "content": msg}
            ]
          )

    resp_content = response['choices'][0]['message']['content']
    print(f"Tokens: {response['usage']['total_tokens']}")
    return resp_content