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
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_KEY')
    client = openai.OpenAI()
    r = client.chat.completions.create(
        model='o1-preview',
        messages=[
            {'role': 'user', 'content': get_prompt().replace('`QUERIES`', get_queries().strip())},
        ],
    )
    return r.choices[0].message.content

def main():
    table = create_table()
    print(table)

if __name__ == '__main__':
    main()
