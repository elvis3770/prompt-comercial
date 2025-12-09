"""
Test if Gemini API key is valid with vision
"""
import google.generativeai as genai

API_KEY = "AIzaSyBjC2f1xIGu9l3fcSuRbfxGz0HzQgFRZHQ"

try:
    genai.configure(api_key=API_KEY)
    
    # Test with gemini-2.5-flash (newer version, might have quota)
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Say 'API key works!'")
    
    print("[OK] API KEY FUNCIONA CON gemini-2.5-flash")
    print(f"Respuesta: {response.text}")
    
except Exception as e:
    print("[ERROR]")
    print(f"Error: {e}")
