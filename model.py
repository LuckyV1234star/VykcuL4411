import base64
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting, Part



def multiturn_generate_content():
    vertexai.init(project="savvy-bonito-440904-q7", location="asia-east2")
    model = GenerativeModel(
        "gemini-1.5-flash-001",
    )
    chat = model.start_chat()


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0.5,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

multiturn_generate_content()


import google.generativeai as genai
import os


