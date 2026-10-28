# import sys

# # Example run: python script.py deploy --force
# print(f"Script name: {sys.argv[0]}") # Output: script.py
# print(f"Total arguments passed: {len(sys.argv) - 1}")
# print(f"All arguments: {sys.argv}")  # Output: ['script.py', 'deploy', '--force']cd
# sys.argv()


import sys

print(f"current file name is: {len(sys.argv)}")
a = 5
if sys.argv[1] == "-h":
    print("Asking for Help use --help flag")
elif sys.argv[1] == "-sq":
    print(f"{a} square: {a * a}")
