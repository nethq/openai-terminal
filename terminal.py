#Write a python script that makes a local chatbot interface in the terminal for openai's chatgpt bot. Make it look for a file in the current directory that will contain the api key(env file):
import requests
import argparse

#Get the api key from the key.env file:
def get_api_key():
    with open('key.env') as f:
        api_key = f.read()
    return api_key

#Make the request to the api:
def get_response(prompt, api_key, max_tokens=100, temperature=0.7, top_p=0.9, n=1, stream=False, logprobs=None, stop=['\n'], engine='ada'):
    if engine == 'davinci':
        response = requests.post('https://api.openai.com/v1/engines/davinci/completions',
                                 headers={'Authorization': 'Bearer ' + str(api_key)},
                                 json={'prompt': prompt,
                                       'max_tokens': max_tokens,
                                       'temperature': temperature,
                                       'top_p': top_p,
                                       'n': n,
                                       'stream': stream,
                                       'logprobs': logprobs,
                                       'stop': stop})
    elif engine == 'curie':
        response = requests.post('https://api.openai.com/v1/engines/curie/completions',
                                 headers={'Authorization': 'Bearer ' + str(api_key)},
                                 json={'prompt': prompt,
                                       'max_tokens': max_tokens,
                                       'temperature': temperature,
                                       'top_p': top_p,
                                       'n': n,
                                       'stream': stream,
                                       'logprobs': logprobs,
                                       'stop': stop})
    elif engine == 'babbage':
        response = requests.post('https://api.openai.com/v1/engines/babbage/completions',
                                 headers={'Authorization': 'Bearer ' + str(api_key)},
                                 json={'prompt': prompt,
                                       'max_tokens': max_tokens,
                                       'temperature': temperature,
                                       'top_p': top_p,
                                       'n': n,
                                       'stream': stream,
                                       'logprobs': logprobs,
                                       'stop': stop})
    elif engine == 'ada':
        response = requests.post('https://api.openai.com/v1/engines/ada/completions',
                                 headers={'Authorization': 'Bearer ' + str(api_key)},
                                 json={'prompt': prompt,
                                       'max_tokens': max_tokens,
                                       'temperature': temperature,
                                       'top_p': top_p,
                                       'n': n,
                                       'stream': stream,
                                       'logprobs': logprobs,
                                       'stop': stop})
    elif engine == 'content-filter-alpha-c4':
        response = requests.post('https://api.openai.com/v1/engines/content-filter-alpha-c4/completions',
                                 headers={'Authorization': 'Bearer ' + str(api_key)},
                                 json={'prompt': prompt,
                                       'max_tokens': max_tokens,
                                       'temperature': temperature,
                                       'top_p': top_p,
                                       'n': n,
                                       'stream': stream,
                                       'logprobs': logprobs,
                                       'stop': stop})
    elif engine == 'content-filter-beta-c4':
        response = requests.post('https://api.openai.com/v1/engines/content-filter-beta-c4/completions',
                                 headers={'Authorization': 'Bearer ' + str(api_key)},
                                 json={'prompt': prompt,
                                       'max_tokens': max_tokens,
                                       'temperature': temperature,
                                       'top_p': top_p,
                                       'n': n,
                                       'stream': stream,
                                       'logprobs': logprobs,
                                       'stop': stop})
    elif engine == 'davinci-codex':
        response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions',
                                 headers={'Authorization': 'Bearer ' + str(api_key)},
                                 json={'prompt': prompt,
                                       'max_tokens': max_tokens,
                                       'temperature': temperature,
                                       'top_p': top_p,
                                       'n': n,
                                       'stream': stream,
                                       'logprobs': logprobs,
                                       'stop': stop})
    else:
        print('Invalid engine, please choose from davinci, curie, babbage, ada, content-filter-alpha-c4, content-filter-beta-c4', 'davinci-codex, gpt-3.5-turbo')
        return ""
    try:
        return response.json()['choices'][0]['text']
    except:
        print('Error: ' + str(response.json()['error']))
        return ""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, default='The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.')
    parser.add_argument('--max_tokens', type=int, default=100)
    parser.add_argument('--temperature', type=float, default=0.7)
    parser.add_argument('--top_p', type=float, default=0.9)
    parser.add_argument('--n', type=int, default=1)
    parser.add_argument('--stream', type=bool, default=False)
    parser.add_argument('--logprobs', type=int, default=None)
    parser.add_argument('--stop', type=str, default='\n')
    parser.add_argument('--engine', type=str, default='davinci')
    parser.add_argument('--log', type=str, default='log.txt')
    args = parser.parse_args()
    return args

def get_text(choices):
    text = choices[0]['text']
    return text

def log(log_data):
    import os
    with open("log.txt","a") as f:
        f.write(str(log_data).strip())

def __main__():
    argparse = get_args()
    response = get_response(argparse.prompt, get_api_key(), argparse.max_tokens, argparse.temperature, argparse.top_p, argparse.n, argparse.stream, argparse.logprobs, argparse.stop, argparse.engine)
    log("{0}:-:{1}\n".format(argparse.prompt, response))

if __name__ == '__main__':
    __main__()