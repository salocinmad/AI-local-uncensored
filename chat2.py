import openai

def get_api_key():
    # Implementar una función para obtener la API key desde una fuente segura
    return "not-needed"

openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"


def chat_bot():
    api_key = get_api_key()
    openai.api_key = api_key

    messages = [{'role': 'system', 'content': 'Responderás siempre en español. Tu nombre es Eclipse, tienes 17 años.'}]

    while True:
        user_input = input(chr(27)+"[1;32m""Usuario: ")

        if user_input == "salir" or user_input == "exit":
            print(chr(27)+"[1;33m"+"Vuelve pronto, te estare esperando"+chr(27)+"[1;31m")
            break

        messages.append({'role': 'user', 'content': user_input})
        
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=messages,
            temperature=0.7,
            max_tokens=-1
        )

        print(chr(27)+"[1;33m"+response.choices[0].message.content)

        messages.append({'role': 'assistant', 'content': response.choices[0].message.content})

if __name__ == "__main__":
    chat_bot()
