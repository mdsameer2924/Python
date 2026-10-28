import subprocess

# We run a command and pass data directly into its stdin using the input parameter
result = subprocess.run(
    ["wl-copy"],  # 'cat' reads from stdin and prints it back out
    input="Hello from java!",  # This text is fed directly into the command
    text=True,  # Tells subprocess to treat input/output as text strings
    capture_output=True,  # Captures the response
)

print("What came back:", result.stdout)
# Output: What came back: Hello from Python!
