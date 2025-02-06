# Google Ads Negative Keywords Pipeline
## 1. General description
- This tool helps Google Ads advertisers automatically process large volumes of search query reports to identify and filter out irrelevant traffic.  
- The pipeline utilizes OpenAI API to analyze search terms and generate comprehensive lists of negative keywords based on specific exclusion criteria.  
- The solution addresses a common challenge where advertisers need to process millions of search queries monthly but cannot effectively do this through ChatGPT interface due to input limitations.  
- The system works by breaking down large search query lists into manageable batches, processing them through OpenAI API with carefully crafted prompts, and combining the results into a clean list of negative keywords.  
- Each search query is evaluated against multiple criteria including geographical relevance, service type match, DIY intentions, competitor brand mentions, and budget-related indicators.  
- The negative keywords generated by this pipeline can be directly imported into Google Ads campaigns, saving hours of manual review work.

## 2. How to use
### 2.1.
The program uses the OpenAI API, model `o1`.  
### 2.2.
In order for the program to work, an API key is required.  
It must be placed in the file `config/private.env` in the format:
```
OPENAI_API_KEY = <your key>
```
### 2.3.
The file with search queries: [`queries.txt`](https://github.com/dmitry-ai/google-ads-negative-keywords-pipeline/blob/main/queries.txt)
### 2.4. 
The file with public parameters: [`config/public.env`](https://github.com/dmitry-ai/google-ads-negative-keywords-pipeline/blob/main/config/public.env)  
The program has 2 public parameters: `dfBatchSize` and `dfMaxBatches`.
#### `dfBatchSize`
This is the number of search queries for simultaneous processing.  
The higher the value, the fewer resources OpenAI will devote to each query, and this will reduce the quality of the OpenAI response.
#### `dfMaxBatches`
This is the number of batches (each of size `dfBatchSize`) that the program will process.  
Limiting this value saves money and time when testing the program.