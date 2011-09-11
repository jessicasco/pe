#!/usr/bin/env python
def main():
    print max(
            sum(int(i) for i in str(a**b)) 
            for a in range(2, 100) 
            for b in range(100)
            )

if __name__ == '__main__':
    main()
