import requests
import json
import os


print ("""
██████╗ ██████╗ ██╗  ██╗    ███████╗██╗  ██╗██╗███████╗██╗  ██╗██╗██████╗ 
██╔══██╗██╔══██╗██║  ██║    ██╔════╝██║  ██║██║██╔════╝██║  ██║██║██╔══██╗
██████╔╝██████╔╝███████║    ███████╗███████║██║███████╗███████║██║██████╔╝
██╔══██╗██╔══██╗██╔══██║    ╚════██║██╔══██║██║╚════██║██╔══██║██║██╔══██╗
██████╔╝██████╔╝██║  ██║    ███████║██║  ██║██║███████║██║  ██║██║██║  ██║
╚═════╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                             "By: Shishir Sharma  "
""")

def get_sub_domains(domain):
    url = "https://api.securitytrails.com/v1/domain/" + domain + "/subdomains"
    #print(url)
    querystring = {"children_only": "true"}
    headers = {
        'accept': "application/json",
        'apikey': "(put your api key )"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result_json = json.loads(response.text)
    sub_domains = [i + '.' + domain for i in result_json['subdomains']]
    f = open("security_trails_domains.txt", 'w+')
    for i in sub_domains:
        f.write(i + '\n')
    f.close()
    return sub_domains

domain = input("\nMujhe Domain Do jaldi : ")


get_sub_domains(domain)
