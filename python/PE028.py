#!/usr/bin/env python
def main():
    s = 1
    m = 1
    step = 2
    for i in range(500):
        s += (m + step) + (m + 2 * step) + (m + 3 * step) + (m + 4 *step)
        m = m + 4 * step
        step += 2
    print s

if __name__ == '__main__':
    main()
