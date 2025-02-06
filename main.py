# 2025-02-04 Dmitrii Fediuk https://upwork.com/fl/mage2pro
# 1) «About negative keywords»:
# https://support.google.com/google-ads/answer/2453972
# https://archive.is/OYLaq
# 2) «Add negative keywords to campaigns»:
# https://support.google.com/google-ads/answer/7102995
# https://archive.is/lUIED
from dotenv import load_dotenv as ⵗenv
from more_itertools import chunked as ⵗchunked
from pathlib import Path
import json
import openai
import os

# 2025-02-04
# @used-by main()
# @used-by read_file_in_batches()
fp = lambda v: os.path.join(os.path.dirname(__file__), v)

def read_file_in_batches(f):
    batch_size = int(os.getenv('dfBatchSize'))
    ᛡmax = int(os.getenv('dfMaxBatches'))
    with open(fp(f), 'r', encoding='utf-8') as contents:
        lines = (line.strip('\n') for line in contents)
        for i, chunk in enumerate(ⵗchunked(lines, batch_size), 1):
            if i > ᛡmax:
                return
            yield chunk

def prompt(s: str) -> str: return Path(fp(f'prompts/{s}.md')).read_text(encoding='utf-8')

def main():
    ⵗenv('config/private.env')
    ⵗenv('config/public.env')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    ᛡopenai = openai.OpenAI()
    r = []
    for chunk in read_file_in_batches('queries.txt'):
        intents = ᛡopenai.chat.completions \
            .create(model='o1', messages=[{
                'content': prompt('intents').replace('%QUERIES%', '\n'.join(chunk)), 'role': 'user'
            }]) \
            .choices[0].message.content
        nks = ᛡopenai.chat.completions \
            .create(model='o1', messages=[{
                'content': prompt('negative-keywords').replace('%INTENTS%', intents), 'role': 'user'
            }]) \
            .choices[0].message.content
        r.extend(nks.splitlines())
    r = list(dict.fromkeys(r))
    r.sort()
    print('\n'.join(r))

if __name__ == '__main__':
    main()