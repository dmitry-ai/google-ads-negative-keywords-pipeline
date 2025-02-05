# 2025-02-04 Dmitrii Fediuk https://upwork.com/fl/mage2pro
# 1) «About negative keywords»:
# https://support.google.com/google-ads/answer/2453972
# https://archive.is/OYLaq
# 2) «Add negative keywords to campaigns»:
# https://support.google.com/google-ads/answer/7102995
# https://archive.is/lUIED
from dotenv import load_dotenv
from more_itertools import 𑀰chunked
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
        for i, chunk in enumerate(𑀰chunked(lines, batch_size), 1):
            if i > ᛡmax:
                return
            yield chunk

def main():
    load_dotenv('config/private.env')
    load_dotenv('config/public.env')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    prompt = Path(fp('prompt.md')).read_text(encoding='utf-8')
    rr = []
    ᛡopenai = openai.OpenAI()
    for chunk in read_file_in_batches('queries.txt'):
        res = ᛡopenai.chat.completions \
            .create(model='o1', messages=[{
                'content': prompt.replace('`QUERIES`', '\n'.join(chunk)), 'role': 'user'
            }]) \
            .choices[0].message.content
        try:
            ᛡjson = json.loads(res)
        except json.JSONDecodeError:
            print('OpenAI returned an invalid JSON response:')
            print(res)
            exit(1)
        for i in ᛡjson:
            rr.append(i)
    r = []
    for i in rr:
        if 'no' == i.get('relevant'):
            r.extend(i.get('rules', []))
    r = list(set(r)) # 2025-02-04 It removes duplicates
    r.sort()
    print('\n'.join(r))

if __name__ == '__main__':
    main()