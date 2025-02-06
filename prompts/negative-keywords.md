## 1. 
Company `C` is located in Charlotte (North Carolina, USA).

## 2.
`C` provides 2 types of moving services:
### 2.1.
Local: within a 50-mile radius of the company's location (point 1).  
### 2.2.
Global: from point 2.1 to any point in the USA.

## 3.
### 3.1.
Given document `D`:
```json
%INTENTS%
```
### 3.2.
`D` is a JSON object.

### 3.3.
The keys of `D` are user queries to Google.

### 3.4.
The value of a specific key is an explanation of the user's intentions: what exactly they wanted to find with their query.

## 4.
The term `NK` means: a «negative keyword» of type «broad match» for Search campaigns in Google Ads.

## 5.
For each of the user queries in `D`, based on the key value (3.4), determine whether this query is relevant to company `C`'s services.

## 6.
If the user query is relevant to `C`, then skip this query and proceed to the next one.

## 7.
If the user query is not relevant to `C`, then build an `NK` for it.

## 8. Requirements for `NK`
### 8.1.
Try to keep `NK` short.
### 8.2.
Try to make `NK` universal so that it matches not only the specific query 3.3, but also the largest possible number of other potential queries (based on 3.4), while ensuring that it does not match queries relevant to `C`.

## 9.
As a result of processing `D` according to the rules of points 5-7, you will get a list of all `NK`.
Return this list as plain text, one `NK` per line.

## 10.
Do not return anything other than the list from point 9.

## 11.
Do not wrap the response in backticks or anything else.