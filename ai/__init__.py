import openai
def consultarchatgpt(produto):
    openai.api_key = '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'
    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = 'O que voce acha do ' + produto + '?'
    # Set the maximum number of tokens to generate in the response
    max_tokens = 2048

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text
