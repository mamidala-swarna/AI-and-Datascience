# Install Module called requests (pip install requests)
import requests 
r = requests.get('https://www.python.org/')
# HTTP Status Codes - https://miro.medium.com/v2/0*emwCsVL6_veL1d0I 
print("HTTP Status Code",r.status_code)

import requests 
r = requests.get('https://www.python.org/ravi')
# HTTP Status Codes - https://miro.medium.com/v2/0*emwCsVL6_veL1d0I 
print("HTTP Status Code",r.status_code)