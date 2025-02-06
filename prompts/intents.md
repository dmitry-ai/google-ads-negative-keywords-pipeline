## 1. Given
A list of search queries to Google is provided:
```
%QUERIES%
```

## 2. Your task
For each of the queries from point 1, indicate what, in your opinion, the user wanted to find.

## 3. Requirements for the answers of point 2
### 3.1.
For each search query, the answer must contain 5 sentences.
### 3.2.
The answers must be in English.
### 3.3.
Do not use Markdown: only plain text.
### 3.4.
Each paragraph must contain exactly 1 sentence.
### 3.5.
There must be no blank lines left between paragraphs.
### 3.6.
Do not use contractions like «don't».
Write all such phrases in full: «do not».

## 4. Result formatting
### 4.1.
You must return a JSON object.
Its keys must be the queries from point 1, and the values of the keys must be your answers to the questions of point 2.
### 4.2.
Do not return anything besides JSON.
### 4.3.
Do not wrap the JSON response in backticks or anything else.