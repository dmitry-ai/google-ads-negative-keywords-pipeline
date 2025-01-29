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

## 4. How I want to accomplish point 4
I want to accomplish point 4 in the following way:
4.1) A list of irrelevant search queries is compiled (point 5 below).
4.2) For each element of the list of search queries (point 5 below), determine whether this query is relevant to my company’s services.

## 5. List of search queries
railcar mover rental
#1 pet mover
#1 us pet mover
√© preciso mover
02 01 mover 4029357733 can s618034583078548 card 3466
02 honda crv does not move then starts moving
1 2 x 170 inch belt mover deck
1 64 round bale mover
1 bedroom long distance mover canada
1 day mover salary

## 6. Your task
Fulfill point 4.2.

## 7. Criteria of an irrelevant search query
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

## 8. The format of your answer
### 8.1.
Your answer must be a table with 4 columns.

### 8.2.
Each line of the list from point 5 must correspond to exactly one line of your table.

### 8.3.
The rows of the table must be placed in exactly the same sequence as the elements of the list in point 5.

### 8.4.
Each row of the table must have exactly 5 cells:
8.4.1) The sequential number of the line (start from 1).
8.4.2) The element of the list from point 5.
8.4.3) Do you consider the search query from point 8.4.2 to be relevant to my company’s services? (based on point 7 above).
The value of the cell must be exactly one word: «yes» or «no».
8.4.4) If the value of the cell in point 8.4.3 is «no», then specify the exact subpoints of point 7 above, on the basis of which you made the decision from point 8.4.3.
The value of the cell must simply be the list of subpoints from point 7, separated by commas.
8.4.5) If the value of the cell in point 8.4.3 is «no», then specify the rules for Google Ads in Google Ads format that will carry out the task from point 4 for that specific query.

## 9. Example of the correct answer format
In this example, for brevity, there are only 5 lines.
You will have as many lines as determined by point 8.2.
~~~
| № | Search query | Relevant? | Reasons for irrelevance | Rule for Google Ads |
|---|-------------|-----------|-------------------------|---------------------|
| 1 | railcar mover rental | no | 7.1, 7.3 | -`railcar mover` -rental |
| 2 | #1 pet mover | no | 7.1, 7.3 | -`pet mover` |
| 3 | #1 us pet mover | no | 7.1, 7.3 | -`pet mover` -`us pet` |
| 4 | √© preciso mover | no | 7.1, 7.4 | -`preciso mover` |
| 5 | 02 01 mover 4029357733 can s618034583078548 card 3466 | no | 7.1 | -`card` -`can` |
~~~