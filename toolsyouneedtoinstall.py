import subprocess

def install_package(package_name):
    command = f"apt-get install -y {package_name}"
    subprocess.run(command, shell=True)

# Install dnsx
install_package("dnsx")

# Install naabu
install_package("naabu")

# Install Subfinder
install_package("subfinder")

# Install Dirsearch
#install_package("dirsearch")

#Install Screen
#install_package("screen")
