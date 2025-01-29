## 1.
My company is located in Charlotte (North Carolina, USA).

## 2.
My company provides 2 types of moving services:
1.1) Local: within a 50-mile radius from point 1.  
1.2) Global: from point 1.1 to any point in the USA.

## 3.
I advertise the services of my company (point 1) in Google search results by means of Google Ads.

## 4. My strategic objective
I want the ads of the advertising campaign from point 3 to not appear in Google search results if the Google user (hereinafter — `User`) has made a search query irrelevant to the company’s services (point 2).

## 5. How I want to accomplish point 4
I want to accomplish point 4 in the following way:
4.1) A list of irrelevant search queries is compiled (point 5 below).  
4.2) For each element of the list of search queries (point 5 below), determine whether this query is relevant to my company’s services.

## 6. List of search queries
`QUERIES`

## 7. Your task
Fulfill point 4.2.

## 8. Criteria of an irrelevant search query
Consider the query irrelevant if at least one of the statements in this point 7 is true for this query:

### 7.1.
The query does not match the company’s services (point 2).

### 7.2.
The `User` needs a move that is too small.

### 7.3.
The `User` is looking for my company’s competitors.  
For example: the query contains brand names, manufacturers, models, and so on.

### 7.4.
The `User` wants to carry out the move independently or is doing general research (for example, looking for a process, stages, and so on).

### 7.5.
The `User` is limited in budget and is looking for cheap services.

## 8. The JSON format of your answer

### 8.1.
Your answer must be a JSON array.

### 8.2.
For each line of the list from point 6, you must create exactly one JSON object in this array.

### 8.3.
The objects must be placed in exactly the same sequence as the lines in point 6.

### 8.4.
Each JSON object must have exactly 5 fields:
8.4.1) `line_number`: the sequential number of the line (start from 1).  
8.4.2) `search_query`: the element of the list from point 6.  
8.4.3) `relevant`: do you consider the search query from point 8.4.2 to be relevant to my company’s services? (based on point 7).  
The value of this field must be exactly one word: «yes» or «no».  
8.4.4) `reasons_for_irrelevance`: if the value of the field in point 8.4.3 is «no», then specify the exact subpoints of point 7 above, on the basis of which you made the decision.  
The value of this field must be the list of subpoints from point 7, separated by commas.  
8.4.5) `google_ads_rule`: if the value of the field in point 8.4.3 is «no», then specify the rules for Google Ads in Google Ads format that will carry out the task from point 4 for that specific query.

## 9. Example of the correct JSON answer format
Below is an example with only 5 lines. You will have as many lines as determined by point 8.2.
```json
[
	{
		"line_number": 1,
		"search_query": "railcar mover rental",
		"relevant": "no",
		"reasons_for_irrelevance": [7.1, 7.3],
		"rules": ["-railcar mover", "-rental"]
	},
	{
		"line_number": 2,
		"search_query": "#1 pet mover",
		"relevant": "no",
		"reasons_for_irrelevance": [7.1, 7.3],
		"rules": ["-pet mover"]
	},
	{
		"line_number": 3,
		"search_query": "#1 us pet mover",
		"relevant": "no",
		"reasons_for_irrelevance": [7.1, 7.3],
		"rules": ["-pet mover", "-us pet"]
	},
	{
		"line_number": 4,
		"search_query": "√© preciso mover",
		"relevant": "no",
		"reasons_for_irrelevance": [7.1, 7.4],
		"rules": ["-preciso mover"]
	},
	{
		"line_number": 5,
		"search_query": "02 01 mover 4029357733 can s618034583078548 card 3466",
		"relevant": "no",
		"reasons_for_irrelevance": [7.1],
		"rules": ["-card", "-can"]
	}
]
```

## 10. 
### 10.1.
Do not return anything besides JSON.
### 10.2.
Do not wrap the JSON response in backticks (```json) or anything else.