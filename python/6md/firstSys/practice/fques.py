# Easy: Print the name of the script being executed.
import sys # this module provide arugemnt in cli  

print(f"Name of this script: {sys.argv[0]}")
sys.argv.append("sameer")
# print(sys.argv[1])
for i in sys.argv:
    print(i)

print(sys.version)
# TODO finish list, dict , tup, string set first then learn this module