#!/usr/bin/env python
import cookielib
import urllib
import urllib2
import re
import getpass
import os

class PE():
    def __init__(self, username, password):
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
        self.getpdfs()
    
    def getpdfs(self):
        self.solved = re.compile(r'<img src=".*?icon_tick.png" alt="Solved"')
        self.pattern = re.compile(r'(project/resources/.*?overview.pdf)')
        self.url = "http://projecteuler.net/index.php?section=problems&page=%s"
        self.domain = "http://projecteuler.net/"
        i = 1
        while True:
            response = self.opener.open(self.url % i)
            data = response.read()
            result = self.solved.findall(data)
            if not result:
                break
            pdfs = self.pattern.findall(data)
            for pdf in pdfs:
                os.system('wget %s/%s -O tmp/%s' % (self.domain, pdf,
                    pdf.split('/')[-1]))
            i += 1

def main():
    username = raw_input('input your projecteuler username: ')
    password = getpass.getpass('input your projecteuler password: ')
    PE(username, password)

if __name__ == '__main__':
    main()
