# pyscbwrapper
Version 0.1.1

Python wrapper for Statistics Sweden's API, which can be found at http://www.scb.se/en/api.

News in version 0.1:  
Compatible with changes in the API.  
Includes a function for generating JSON queries from user-supplied input.  
It is now possible to go up and down in the metadata tree more than one step at a time.

News in version 0.1.1:  
Bugfixes: Variables with space in their names can now be accessed by removing the spaces.  
New functionality: get_variables() returns a dict instead of only writing to the terminal.  

News in version 0.1.2:
Security fix: Updated API URL from HTTP to HTTPS to ensure secure communication with Statistics Sweden's API. 
This resolves issues with empty or invalid responses caused by using the insecure HTTP connection.

Dependencies: requests>=2.21.0

To install: 
```python
pip install pyscbwrapper
```

To import: 
```python
from pyscbwrapper import SCB
```

For info on usage, see the included notebooks. For detailed usage examples, see the subfolder fetch-deso-data-examples.




[![Mentioned in Awesome Official Statistics ](https://awesome.re/mentioned-badge.svg)](http://www.awesomeofficialstatistics.org)
