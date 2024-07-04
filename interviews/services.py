import requests
from django.conf import settings

class GeminiAiService:
    def __init__(self):
        self.__gemini_api_key = settings.GEMINI_API_KEY
        self.__gemini_ai_base_url = settings.GEMINI_AI_BASE_URL

    def get_chat_completion(self, messages):
        payload = {
            "contents": [
                {
                    "role": message.role,
                    "parts": [
                        {"text": message.content}
                    ]
                } for message in messages
            ]
        }
        headers = {'Content-Type': 'application/json',
                   'x-goog-api-key': f'{self.__gemini_api_key}'}
        
        response = requests.post(
            self.__gemini_ai_base_url,
            json=payload,
            headers=headers,
        )

        if response.status_code == 200:
            response_data = response.json()

            if "candidates" in response_data:
                if response_data['candidates'][0]['content']['role'] == 'model':
                    return response_data['candidates'][0]['content']['parts'][0]['text']
                else:
                    raise Exception("A role da resposta não é 'model'.")
            else:
                raise Exception("A chave 'candidates' não foi encontrada na resposta.")

        else:
            raise Exception("Erro ao enviar prompt para a API: {}".format(response.status_code))