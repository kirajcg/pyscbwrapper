# scb-api-examples
Some notebooks I created for fetching DeSO (Swedish census data) area data. Transformation of the data and insert to PostgreSQL is also included

## Introduction:
This repository holds some example notebooks which I created when fetching census data from the [SCB API](https://www.scb.se/en/services/open-data-api/api-for-the-statistical-database/). SCB is the Central Bureau of Statistics in Sweden (Nowadays '[Statistics Sweden](https://www.scb.se/en/)').
For ease of use I used the python wrapper, [pyscbwrapper](https://github.com/kirajcg/pyscbwrapper), which also holds its own example code. I made this repository primarily for myself and I dont believe it is clearer than theirs, but I leave it public if it may help someone.

As told in their repository:

To install:
```python
pip install pyscbwrapper
```
To import:
```python
from pyscbwrapper import SCB
```

## Fetch data

## Transform data
