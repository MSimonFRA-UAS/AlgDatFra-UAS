def hanoi_iterative(n, stab_a, stab_b, stab_c):
    check_even = (n % 2 == 0)
    for k in range(1, 1 << n):
        print(k)
        print(k & (k-1))
        s = (k & (k-1)) % 3
        t = ((k | (k-1)) + 1) % 3
        if s == 0:
            if t == 1:
                stab_b.insert(0, stab_a.pop(0))
            elif t == 2:
                stab_c.insert(0, stab_a.pop(0))
        elif s == 1:
            if t == 0:
                stab_a.insert(0, stab_b.pop(0))
            elif t == 2:
                stab_c.insert(0, stab_b.pop(0))
        elif s == 2:
            if t == 0:
                stab_a.insert(0, stab_c.pop(0))
            elif t == 1:
                stab_b.insert(0, stab_c.pop(0))
    if not check_even:
        stab_b, stab_c = stab_c, stab_b
    return stab_a, stab_b, stab_c, k 


def main():

    n = int(input('Bitte geben Sie die gewuenschte Anzahl an Scheiben ein: '))
    stab_a = [x for x in range(n)]
    stab_b = []
    stab_c = []
    print('Spielbeginn: ', 'A =', stab_a, 'B =', stab_b, 'C =', stab_c)
    stab_a, stab_b, stab_c, k = hanoi_iterative(n, stab_a, stab_b, stab_c)
    print('Anzahl Spielzuege: ', k)
    print('Spielende: ', 'A =', stab_a, 'B =', stab_b, 'C =', stab_c)


if __name__ == "__main__":
    main()