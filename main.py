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
import openai
import os

fp = lambda v: os.path.join(os.path.dirname(__file__), v)

def batches(f):
    size = int(os.getenv('dfBatchSize'))
    ᛡmax = int(os.getenv('dfMaxBatches'))
    with open(fp(f), 'r', encoding='utf-8') as s:
        lines = (line.strip('\n') for line in s)
        for i, chunk in enumerate(ⵗchunked(lines, size), 1):
            if i > ᛡmax:
                return
            yield chunk

def main():
    ⵗenv('config/private.env')
    ⵗenv('config/public.env')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    ᛡopenai = openai.OpenAI()
    r = []
    prompt = lambda v: Path(fp(f'prompts/{v}.md')).read_text(encoding='utf-8')
    def query(v1, v2, v3) -> str:
        c = prompt(v1).replace(f'%{v2}%', v3)
        res = ᛡopenai.chat.completions.create(model='o1', messages=[{'content': c, 'role': 'user'}])
        return res.choices[0].message.content
    for batch in batches('queries.txt'):
        intents = query('intents', 'QUERIES', '\n'.join(batch))
        nks = query('negative-keywords', 'INTENTS', intents)
        r.extend(nks.splitlines())
    r = list(dict.fromkeys(r))
    r.sort()
    print('\n'.join(r))

if __name__ == '__main__':
    main()