def hanoi_recursive(n, stab_a, stab_b, stab_c):
    if n == 1:
        stab_b.insert(0, stab_a.pop(0))
    else:
        hanoi_recursive(n-1, stab_a, stab_c, stab_b)
        stab_b.insert(0, stab_a.pop(0))
        hanoi_recursive(n-1, stab_c, stab_b, stab_a)


def main():

    n = int(input('Bitte geben Sie die gewuenschte Anzahl an Scheiben ein: '))
    stab_a = [x for x in range(1, n+1)]
    stab_b = []
    stab_c = []
    print('Spielbeginn: ', 'A =', stab_a, 'B =', stab_b, 'C =', stab_c)
    hanoi_recursive(n, stab_a, stab_b, stab_c)
    print('Spielende: ', 'A =', stab_a, 'B =', stab_b, 'C =', stab_c)


if __name__ == "__main__":
    main()

