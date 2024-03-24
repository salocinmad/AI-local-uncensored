import openai

# openai.api_key="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"
# hihii

openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-nedded"


messages = [{'role': 'system', 'content': 'Responderas siempre en español. tu nombre Eclipse, tienes 17 años.'}]


while True:
    user_input = input(chr(27)+"[1;32m""Usuario: ")
    
    messages.append({'role': 'user', 'content': user_input})
    
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages,
        temperature=0.7,
        max_tokens=-1
    )

    # print(response)
    print(chr(27)+"[1;33m"+response.choices[0].message.content)
    
    messages.append({'role': 'assistant', 'content': response.choices[0].message.content})