def backtrack(a, k, n):  # 주어진 배열 a, 결정할 원소 k, 원소 개수 n
    c = [0] * MAXCANDIDATES

    if k == n:
        for i in range(0, k):
            print(a[i], end=" ")
        print()
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)


def construct_candidates(a, k, n, c):
    in_perm = [False] * (NMAX + 1)

    for i in range(k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, NMAX + 1):
        if not in_perm[i]:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


MAXCANDIDATES = 3
NMAX = 3
a = [0] * NMAX
backtrack(a, 0, 3)
