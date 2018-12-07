def next_p(s2):
    i = 0
    j = -1 
    next = [0]*(len(s2)+1)
    next[0] = -1     
    while i < len(s2):
        if j == -1 or list(s2)[i] == list(s2)[j]:
            i+= 1
            j+=1
            next[i] = j
        else:
            j = next[j]
    return next
if __name__ == "__main__":
    s2 = "abcdab" 
    print(next_p(s2))