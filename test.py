def secret(*args, **kwargs):
    return sum([ord(a) for a in args[0]])-1
    
s = input()
print(secret(s))