import os
import openai
from dotenv import load_dotenv
def get_prompt():
    with open(os.path.join(os.path.dirname(__file__), 'prompt.md'), 'r', encoding='utf-8') as f:
        return f.read()

def get_queries():
    with open(os.path.join(os.path.dirname(__file__), 'queries.txt'), 'r', encoding='utf-8') as f:
        return f.read()

def create_table():
    load_dotenv('config/public.env')
    load_dotenv('config/private.env')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    batch_size = int(os.getenv('dfBatchSize', 5))
    max_batches = int(os.getenv('dfMaxBatches', 2))
    all_queries = get_queries()
    chunks = [all_queries[i:i+batch_size] for i in range(0, len(all_queries), batch_size)]
    chunks = chunks[:max_batches]
    prompt = get_prompt()
    all_results = []
    offset = 0
    for c in chunks:
        joined_queries = '\n'.join(c)
        content = prompt.replace('`QUERIES`', joined_queries)
        client = openai.OpenAI()
        r = client.chat.completions.create(model='o1-preview', messages=[{'role': 'user', 'content': content}])
        chunk_json = json.loads(r.choices[0].message.content)
        for obj in chunk_json:
            obj['line_number'] = offset + obj['line_number']
            all_results.append(obj)
        offset += len(c)
    return json.dumps(all_results, ensure_ascii=False, indent=4)

def main():
    table = create_table()
    print(table)

if __name__ == '__main__':
    main()
