# 2025-02-04 Dmitrii Fediuk https://upwork.com/fl/mage2pro
# 1) «About negative keywords»:
# https://support.google.com/google-ads/answer/2453972
# https://archive.is/OYLaq
# 2) «Add negative keywords to campaigns»:
# https://support.google.com/google-ads/answer/7102995
# https://archive.is/lUIED
from dotenv import load_dotenv
import json
import openai
import os
from pathlib import Path

# 2025-02-04
# @used-by main()
# @used-by read_file_in_batches()
fp = lambda v: os.path.join(os.path.dirname(__file__), v)

def read_file_in_batches(name):
    batch_size = int(os.getenv('dfBatchSize'))
    max_batches = int(os.getenv('dfMaxBatches'))
    with open(fp(name), 'r', encoding='utf-8') as f:
        lines = []
        batches_count = 0
        for line in f:
            lines.append(line.strip('\n'))
            if len(lines) == batch_size:
                yield lines
                batches_count += 1
                if batches_count == max_batches:
                    return
                lines = []
        if lines and batches_count < max_batches:
            yield lines

def main():
    load_dotenv('config/public.env')
    load_dotenv('config/private.env')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    prompt = Path(fp('prompt.md')).read_text(encoding='utf-8')
    all_results = []
    offset = 0
    for chunk in read_file_in_batches('queries.txt'):
        joined_queries = '\n'.join(chunk)
        content = prompt.replace('`QUERIES`', joined_queries)
        client = openai.OpenAI()
        res = client.chat.completions \
            .create(model='o1', messages=[{'role': 'user', 'content': content}]) \
            .choices[0].message.content
        try:
            ᛡjson = json.loads(res)
        except json.JSONDecodeError:
            print('OpenAI returned an invalid JSON response:')
            print(res)
            exit(1)
        for i in ᛡjson:
            i['line_number'] = offset + i['line_number']
            all_results.append(i)
        offset += len(chunk)
    r = []
    for obj in all_results:
        if obj.get('relevant') == 'no':
            r.extend(obj.get('rules', []))
    r = list(set(r)) # 2025-02-04 It removes duplicates
    r.sort()
    print('\n'.join(r))

if __name__ == '__main__':
    main()
