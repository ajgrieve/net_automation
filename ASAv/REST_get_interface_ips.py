import json
import requests
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":
    auth = HTTPBasicAuth("cisco", "cisco")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = "https://192.168.1.21/api/interfaces/physical"
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    if response.status_code == 200:
        output = json.loads(response.text)
        format_str = "{: <20} {: <20} {: <10} {: <15}"
        text_headings = ["Interface", "Name", "Enabled", "IPv4"]
        print(format_str.format(*text_headings))
        for interface in output['items']:
            if interface['shutdown'] == False:
                enabled = "Yes"
            else:
                enabled = "No"

            if interface['ipAddress'] == "NoneSelected":
                ipaddress = "None"
            else:
                ipaddress = interface['ipAddress']['ip']['value']
            print(format_str.format(interface['hardwareID'], interface['name'], enabled, ipaddress))
    else:
        print("Request error: "+str(response.status_code))
