import openai


openai.api_key = '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'


while True:

    prompt = input('\nIntroduce una pregunta: ')
    
    if prompt == 'exit':
            break
    
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens = 2048
    )

    print('\nRespuesta: ', completion.choices[0].text)

