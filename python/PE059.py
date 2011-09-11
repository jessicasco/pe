#!/usr/bin/env python
def main():
    line = open("PE059.txt").readline()[:-2].split(',')
    eng = r" !\"'(),-.:;0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for a in range(ord('a'),ord('z')+1):
        for b in range(ord('a'),ord('z')+1):
            for c in range(ord('a'),ord('z')+1):
                m = [a, b, c]
                n = []
                for i in range(len(line)):
                    t = int(line[i]) ^ m[i%3]
                    if chr(t) in eng:
                        n.append(t)
                    else:
                        break
                else:
                    print sum(n)

if __name__ == '__main__':
    main()
