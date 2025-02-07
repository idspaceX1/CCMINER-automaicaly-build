import os
import subprocess
import sys

def check_command(command):
    """Check if a command is available on the system."""
    return subprocess.call(['which', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def install_dependencies():
    """Install necessary dependencies for building ccminer."""
    dependencies = ['git', 'cmake', 'build-essential', 'libcurl4-openssl-dev', 'libjansson-dev', 'libssl-dev']
    for dependency in dependencies:
        try:
            print(f"Checking for {dependency}...")
            if not check_command(dependency):
                print(f"{dependency} is not installed. Installing...")
                subprocess.check_call(['sudo', 'apt-get', 'install', '-y', dependency])
            else:
                print(f"{dependency} is already installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {dependency}: {e}")
            sys.exit(1)

def clone_ccminer():
    """Clone the ccminer repository from GitHub."""
    try:
        print("Cloning ccminer repository...")
        subprocess.check_call(['git', 'clone', 'https://github.com/tpruvot/ccminer.git'])
    except subprocess.CalledProcessError as e:
        print(f"Error cloning ccminer repository: {e}")
        sys.exit(1)

def build_ccminer():
    """Build the ccminer software."""
    try:
        print("Building ccminer...")
        os.chdir('ccminer')
        subprocess.check_call(['mkdir', 'build'])
        os.chdir('build')
        subprocess.check_call(['cmake', '..'])
        subprocess.check_call(['make'])
        print("ccminer built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error building ccminer: {e}")
        sys.exit(1)

def main():
    """Main function to execute the build process."""
    try:
        install_dependencies()
        clone_ccminer()
        build_ccminer()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
