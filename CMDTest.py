import subprocess

try:
    print("Running Command...")
    result = subprocess.run(["pip", "install", "beautifulsoup4"], check=True, text=True, capture_output=True)
    print("Command Output:\n", result.stdout)
    print("Command Completed")
except subprocess.CalledProcessError as e:
    print("Error: Command failed with the following error:")
    print(e.stderr)
except Exception as e:
    print(f"Unexpected Error: {str(e)}")
