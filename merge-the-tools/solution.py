def make_u(s):    
    m = {}
    res = ""
    for c in s:
        if c not in m:
            m[c] = True
            res += c
    return res
def merge_the_tools(s, k):
    # your code goes here
    n = len(s) // k
    for i in range(n):
        print(make_u(string[k*i:k*(i+1)]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)