import requests

API_KEY = 'f77db97a-bdf4-4195-8142-58e5ae4bd2be'

def get_domain_details(domain):
    url = f"https://fullhunt.io/api/v1/domain/{domain}/details"
    headers = {"X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_subdomains(domain):
    url = f"https://fullhunt.io/api/v1/domain/{domain}/subdomains"
    headers = {"X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('hosts', [])
    else:
        return []

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + '\n')

def main():
    domain = input("Enter the domain you want to collect information for: ")
    
    domain_details = get_domain_details(domain)
    if domain_details:
        ip_addresses = []
        subdomains = []

        for host in domain_details['hosts']:
            ip_addresses.append(host['ip_address'])

        subdomains = get_subdomains(domain)

        save_to_file('ip_addresses.txt', ip_addresses)
        save_to_file('subdomains.txt', subdomains)

        print("IP addresses saved to 'ip_addresses.txt'")
        print("Subdomains saved to 'subdomains.txt'")
    else:
        print("Failed to retrieve domain details.")

if __name__ == "__main__":
    main()
