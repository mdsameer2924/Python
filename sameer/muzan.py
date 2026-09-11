def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

def vote_eligiblity(n):
    if n<=17 and n>0:
        print("not eligble to vote")
    elif n>=18:
        print("elible to vote")
    else:
        print("you need to born  on earth")

def add(n,m):
    print(f"{n} + {m} = {n+m}")