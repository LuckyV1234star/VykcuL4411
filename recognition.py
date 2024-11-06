import os
import google.generativeai as genai
import threading

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')


photo = genai.upload_file(path="C:\\Users\\lucky\\Documents\\coding\\cathay\\img\\airpod.jpg")

#response = model.generate_content(photo, "Recognize the image I provided, and tell this if plastic, tetra-pak,or can, if not, reply none. Answering with one word only within:[\"plastic\", \"tetra-pak\", \"can\", \"none\"]")
response = model.generate_content([photo, "識別我提供的圖片，識別圖中物品為塑料、紙包飲品還是金屬製品，並回覆：塑膠、紙包飲品或是金屬製品。注意，其中可能會出現不屬於塑料、紙包飲品或是金屬製品的情況，則回覆：其他。你的回覆應該且只僅為一個詞語從這個集中提取：['塑膠','紙包飲品',金屬製品,'其他']"])

print(response.text)