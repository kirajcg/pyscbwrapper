# pyscbwrapper
Version 0.0.3

Python wrapper for SCB's API, which can be found at http://www.scb.se/en/api.


Dependencies: requests>=2.12.4

To import: 
```python
from pyscbwrapper import SCB
```

Examples of usage: 
```python
scb = SCB('en') # Navigates to https://api.scb.se/OV0104/v1/doris/en/ssd/
scb.go_down('BE') # Navigates to https://api.scb.se/OV0104/v1/doris/en/ssd/BE
scb.go_up() # Navigates back to https://api.scb.se/OV0104/v1/doris/en/ssd/
scb.info() # Fetches metadata associated with https://api.scb.se/OV0104/v1/doris/en/ssd/
scb = SCB('sv', 'BE') # Navigates directly to https://api.scb.se/OV0104/v1/doris/sv/ssd/BE (Data in Swedish)
scb = SCB('en', 'BE', 'BE0701', 'MedelAlderNY') # Navigates directly to https://api.scb.se/OV0104/v1/doris/en/ssd/BE/BE0701/MedelAlderNY
scb.get_url() # Returns 'https://api.scb.se/OV0104/v1/doris/en/ssd/BE/BE0701/MedelAlderNY'
scb.get_data(query) # Fetches data associated with https://api.scb.se/OV0104/v1/doris/en/ssd/BE/BE0701/MedelAlderNY, according to json formatted query (see link above)
```
