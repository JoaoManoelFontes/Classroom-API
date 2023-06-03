import requests
import json


API_KEY = "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"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

params = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Divida temas de trabalho sobre as inteligências artificiais."}]
}
params = json.dumps(params)

req = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=params)
print(req.json()['choices'][0])
# print(openai.ChatCompletion.create(prompt="This is a test", max_tokens=5))
