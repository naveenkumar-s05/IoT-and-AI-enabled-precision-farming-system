import google.generativeai as genai

# ðŸ”‘ Replace this with your Gemini API key
genai.configure(api_key="AIzaSyA2l7xl_XuZ6nnBNAGCSs_R3qBwC0cMzBc")

try:
    # List available models to verify your key
    print(" Checking available models...")
    models = list(genai.list_models())
    for m in models:
        print("-", m.name)

    # Pick one model (usually 'gemini-1.5-flash-latest' works)
    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    # Test a simple prompt
    print("\n Sending test prompt to Gemini...")
    response = model.generate_content("Say hello! Who are you?")
    print("\n Gemini Response:\n", response.text)

except Exception as e:
    print("\n Error occurred:\n", e)
