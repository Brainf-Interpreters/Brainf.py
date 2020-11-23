import sys


def C(c):
    c = ''.join(x for x in c if x in '+-><[].;')
    s = []
    r = []
    for i, g in enumerate(c):
        if g in '.,+-<>':
            r += [g]
        if g == '[':
            s += [i]
            r += [[g]]
        if g == ']':
            if len(s) < 1:
                raise SyntaxError('Bruh where is [')
            _ = s.pop()
            r[_] += [i]
            r += [[g, _]]
    return r


def R(c):
    s, p, i = {0: 0}, 0, 0
    while i < len(c):
        g = c[i]
        if type(g) == list:
            if g[0] == '[' and s[p] == 0:
                i = g[1]
            if g[0] == ']' and s[p] != 0:
                i = g[1]
            i += 1
            continue
        if g == '.':
            print(chr(s[p]), end='')
        if g == '+':
            s[p] += 1
            if s[p] > 255:
                s[p] = 0
        if g == '-':
            s[p] -= 1
            if s[p] < 0:
                s[p] = 255
        if g == '>':
            p += 1
            if p > 255:
                p = 0
        if g == '<':
            p -= 1
            if p < 0:
                p = 255
        if p not in s.keys():
            s[p] = 0
        i += 1
    return s, p


def run(code):
    r2 = R(C(code))
    print('\nSlots:\n' + ' '.join(map(lambda v: f"[{v[1]}]" if v[0]
                                      == r2[1] else str(v[1]), enumerate(r2[0].values()))), r2[1])


def run_file(fn):
    with open(fn, 'r') as f:
        x = f.read()
        run(x)


args = sys.argv
fn = args[-1]
run_file(fn)
