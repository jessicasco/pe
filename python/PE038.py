#!/usr/bin/env python
    
def main():
    s = set(str(i) for i in range(1, 10))
    
    Max = 0
    for i in range(1, 10000):
        t = ""
        for j in range(1, 10):
            t += str(i * j)
            if len(t) == 9:
                if set(t) == s and int(t) > Max:
                    Max = int(t)
                break   
            if len(t) > 9:
                break
    print Max

if __name__ == '__main__':
    main()
