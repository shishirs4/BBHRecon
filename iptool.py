import subprocess

print("""
██████╗ ██████╗ ██╗  ██╗    ███████╗██╗  ██╗██╗███████╗██╗  ██╗██╗██████╗ 
██╔══██╗██╔══██╗██║  ██║    ██╔════╝██║  ██║██║██╔════╝██║  ██║██║██╔══██╗
██████╔╝██████╔╝███████║    ███████╗███████║██║███████╗███████║██║██████╔╝
██╔══██╗██╔══██╗██╔══██║    ╚════██║██╔══██║██║╚════██║██╔══██║██║██╔══██╗
██████╔╝██████╔╝██║  ██║    ███████║██║  ██║██║███████║██║  ██║██║██║  ██║
╚═════╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
""")

def fetch_ips_from_domains(domain_file):
    command = f"dnsx -silent -a -resp-only -l {domain_file}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip().split('\n')
    sorted_ips = sorted(output)  # Sort the IP addresses

    with open("ip_addresses.txt", 'w') as file:
        for ip in sorted_ips:
            file.write(ip + '\n')

    print("IP addresses saved to ip_addresses.txt")

# Example usage
domain_file = input("Enter the path to the FinalDomain.txt file: ")

fetch_ips_from_domains(domain_file)
