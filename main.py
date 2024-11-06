import os
import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')


photo = genai.upload_file(path="C:\\Users\\lucky\\Documents\\coding\\cathay\\img\\drink.jpg")

response = model.generate_content([photo, "Recognize the image I provided, and tell this is plastic, paper, can, for non of above. Answering only one word within [\"plastic\", \"paper\", \"can\", \"none\"]"])

print(response.text)