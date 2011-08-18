#!/usr/bin/env python
import cookielib
import urllib
import urllib2
import re
import getpass

class PE():
    def __init__(self, username, password):
        self.pattern = re.compile(r'<b>(-?\d+)</b>')
        self.url = "http://projecteuler.net/index.php?section=problems&id=%s"
        self.answers = []
        self.username = username
        self.password = password
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(
                urllib2.HTTPCookieProcessor(self.cj))
        self.params = {
                'username': self.username,
                'password': self.password,
                'login': 'Login',
                }
        self.opener.open("http://projecteuler.net", 
                urllib.urlencode(self.params))
        self.getanswers()
    
    def getanswers(self):
        i = 1
        while True:
            response = self.opener.open(self.url % i)
            result = self.pattern.findall(response.read())
            if result:
                self.answers.append(result[0])
                i += 1
            else:
                with open('answers.txt', 'w') as f:
                    f.write('\n'.join(self.answers))
                break

def main():
    username = raw_input('input your projecteuler username: ')
    password = getpass.getpass('input your projecteuler password: ')
    PE(username, password)

if __name__ == '__main__':
    main()
