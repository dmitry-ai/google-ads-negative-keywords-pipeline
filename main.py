from dotenv import load_dotenv
import json
import openai
import os

def get_prompt():
    with open(os.path.join(os.path.dirname(__file__), 'prompt.md'), 'r', encoding='utf-8') as f:
        return f.read()

def read_in_batches(batch_size, max_batches):
    with open(os.path.join(os.path.dirname(__file__), 'queries.txt'), 'r', encoding='utf-8') as f:
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

def create_table():
    load_dotenv('config/public.env')
    load_dotenv('config/private.env')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    batch_size = int(os.getenv('dfBatchSize', 5))
    max_batches = int(os.getenv('dfMaxBatches', 2))
    prompt = get_prompt()
    all_results = []
    offset = 0
    for chunk in read_in_batches(batch_size, max_batches):
        joined_queries = '\n'.join(chunk)
        content = prompt.replace('`QUERIES`', joined_queries)
        client = openai.OpenAI()
        r = client.chat.completions.create(
            model='o1',
            messages=[{'role': 'user', 'content': content}]
        )
        raw_response = r.choices[0].message.content
        try:
            chunk_json = json.loads(raw_response)
        except json.JSONDecodeError:
            print('OpenAI returned an invalid JSON response:')
            print(raw_response)
            exit(1)
        for obj in chunk_json:
            obj['line_number'] = offset + obj['line_number']
            all_results.append(obj)
        offset += len(chunk)
    rules_list = []
    for obj in all_results:
        if obj.get('relevant') == 'no':
            rules_list.extend(obj.get('rules', []))
    rules_list.sort()
    return '\n'.join(rules_list)

def main():
    table = create_table()
    print(table)

if __name__ == '__main__':
    main()
