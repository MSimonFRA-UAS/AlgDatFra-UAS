def write(m, n, stab_a, stab_b, stab_c):
    pre = 'Spielzug %d, Rekursionstiefe: %d :' % (m, n)
    print(pre, '%s = %s' % stab_a, '%s = %s' % stab_b, '%s = %s' % stab_c)


def hanoi_recursive_extended(n, stab_a, stab_b, stab_c, k, m):
    if n == 1:
        stab_b[1].insert(0, stab_a[1].pop(0))
        write(m+1, n, stab_a, stab_b, stab_c)
        return m+1
    else:
        m = hanoi_recursive_extended(n-1, stab_a, stab_c, stab_b, k+1, m)
        stab_b[1].insert(0, stab_a[1].pop(0))
        write(m+1, n, stab_a, stab_b, stab_c)
        m = hanoi_recursive_extended(n-1, stab_c, stab_b, stab_a, k+1, m+1)
        return m


def main():

    n = int(input('Bitte geben Sie die gewuenschte Anzahl an Scheiben ein: '))
    stab_a = ('A', list(range(1, n+1)))
    stab_b = ('B', [])
    stab_c = ('C', [])
    print('Spielbeginn :', '%s = %s' % stab_a, '%s = %s' % stab_b, '%s = %s' % stab_c)
    cnt = hanoi_recursive_extended(n, stab_a, stab_b, stab_c, 0, 0)
    print('Anzahl Spielzüge :', cnt)
    print('  Spielende :', '%s = %s' % stab_a, '%s = %s' % stab_b, '%s = %s' % stab_c)


if __name__ == "__main__":
    main()

