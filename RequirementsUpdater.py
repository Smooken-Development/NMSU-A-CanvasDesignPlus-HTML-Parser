import subprocess
import shutil
import pkg_resources

def checkAndInstall():
    packages = ["beautifulsoup4", "pyperclip", "customtkinter"]

    if not shutil.which("pip"):
        print("Error: 'pip' is not installed.")
        return
    
    for package in packages:
        try:
            if package not in pkg_resources.working_set.by_key:
                print(f"Installing {package}")
                subprocess.check_call([shutil.which("pip"), "install", package])
            else:
                print(f"{package} is up-to-date.")

        except subprocess.CalledProcessError as e:
            print("Error: Command failed with the following error:")
            print(f"Command: {' '.join(e.cmd)}")
            print("Error Output:\n", e.stderr)
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")

# checkAndInstall()