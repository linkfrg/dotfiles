import subprocess
import json

input_text = subprocess.run("cliphist list", capture_output=True, shell=True, text=True).stdout

lines = input_text.split('\n')  # Split the text into lines

# Remove any leading/trailing whitespace from each line
lines = [line.strip() for line in lines if line.strip()]

# Print the resulting list
print(lines)

subprocess.run(["eww", "update", f"clipboard={json.dumps(lines)}"])

