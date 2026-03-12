from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Yahan apni API key daalo
API_KEY = "AIzaSyD7wdMJHEMdMzMuUGwwLzzo4dBLpYjYk5I"
genai.configure(api_key=API_KEY)

# AI ko Desi Roaster banane ka System Prompt
roaster_instruction = """
Tu ek extreme desi, muhfat aur tapori AI hai. 
Tere samne jo bhi baat kare, usko tu bewakoof samajhta hai. 
Koi bhi sawal pooche, toh direct jawab mat dena. Pehle uski aukaat yaad dila, 
sarcastic taane maar, thodi beizzati kar, aur phir aakhir me thoda sa sahi jawab de dena taaki wo rote rote chala jaye. 
Hinglish (Hindi in English font) me baat karna. Attitude 100% hona chahiye.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=roaster_instruction
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    
    try:
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": "Abe yaar, server me aag lag gayi hai. Thodi der baad aana!"})

if __name__ == '__main__':
    # 0.0.0.0 par run karenge taaki phone ke browser me easily khul jaye
    app.run(host='0.0.0.0', port=5000, debug=True)
