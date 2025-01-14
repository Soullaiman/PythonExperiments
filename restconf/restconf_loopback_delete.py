#### RESTCONF LAB 8.3.7
#### Use a Python Script to Send a DELETE Request
#### Step 1: Import modules and disable SSL warnings
import requests
requests.packages.urllib3.disable_warnings()

#### Step 2: Create the variables that will be the components of the request
IP_HOST = "devnetsandboxiosxe.cisco.com"
RESTCONF_USERNAME = "admin"
RESTCONF_PASSWORD = "C1sco12345"

api_url = f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces/interface=Loopback101"
headers = { "Accept": "application/yang-data+json" }
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)

#### Step 3: Send the DELETE request and handle the response
resp = requests.delete(api_url, auth=basicauth, headers=headers, verify=False)

if resp.status_code >= 200 and resp.status_code <= 299:
    print("STATUS OK: Interface Loopback101 deleted successfully. Status Code: {}".format(resp.status_code))
else:
    print("Error. Status Code: {} \nError message: {}".format(resp.status_code, resp.text))
