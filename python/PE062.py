#!/usr/bin/env python
def main():
    d = {}
    i = 1
    while True:
        t = "".join(sorted(list(str(i*i*i)), reverse=True))
        if t in d:
            d[t] += [i]
            if len(d[t]) == 5:
                j = i + 1
                while True:
                    b = j * j * j
                    if b > int(t):
                        a = min(d[t])
                        print a * a * a
                        return
                    s = "".join(sorted(list(str(j*j*j)), reverse=True))
                    if s == t:
                        break
                    j += 1
        else:
            d[t] = [i]
        i += 1

if __name__ == '__main__':
    main()
