import time
import multiprocessing


def kmp_matcher(t, p):
    n = len(t)
    m = len(p)
    lps = [0]*m
    lps = compute_lps(p)
    i = 0
    j = 0
    while i < n:
        if p[j] == t[i]:
            i = i + 1
            j = j +1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i = i+1
        if j == m:
            print("match at: %i" % (i - j))
            j = lps[j-1]


def compute_lps(p):
    m = len(p)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k-1]
        if p[k] == p[q]:
            k = k + 1
        pi[q] = k
    return pi


if __name__ == '__main__':
    with open('book.txt', 'r') as myfile:
        txt = myfile.read().replace('\n', '')
pattern = "tiptoe"
#print("text: %s, pattern: %s" % (txt, pattern))
print("kmp:")
t = time.time()
kmp_matcher(txt, pattern)
print("Time taken is ", time.time() - t)