#!/usr/bin/env python
import subprocess
import shlex
import glob
import os
import threading

DEBUG = False

def verify_python(answers):
    excludefiles = ["pell.py"]
    curdir = os.path.abspath(os.path.dirname(__file__))
    curdir += '/python'
    pyfiles = glob.glob(curdir + '/' + '*.py')
    wrongpyfiles = []
    for pyfile in pyfiles:
        pyfilename = pyfile.split('/')[-1]
        if pyfilename in excludefiles:
            continue
        if DEBUG:
            print pyfilename, '  checked:', 
        cmd = 'python %s' % pyfilename
        result = subprocess.check_output(shlex.split(cmd), cwd=curdir)[:-1]
        index = int(pyfilename.split('.')[0][2:]) - 1
        if result == answers[index]:
            pass
            if DEBUG:
                print 'OK!'
        else:
            if DEBUG:
                print 'Not right!'
            wrongpyfiles.append(pyfilename)
    print 'python files verified, total %s files' % len(pyfiles)
    if wrongpyfiles:
        print 'These python file(s) need fix(es):', " ".join(wrongpyfiles)

def verify_java(answers):
    curdir = os.path.abspath(os.path.dirname(__file__))
    curdir += '/java'
    javafiles = glob.glob(curdir + '/' + '*.java')
    wrongjavafiles = []
    for javafile in javafiles:
        javafilename = javafile.split('/')[-1]
        if DEBUG:
            print javafilename, 'checked:', 
        cmd = 'javac %s' % javafilename
        result = subprocess.check_output(shlex.split(cmd), cwd=curdir)[:-1]
        assert result == ''
        cmd = 'java %s' % javafilename.split('.')[0]
        result = subprocess.check_output(shlex.split(cmd), cwd=curdir)[:-1]
        index = int(javafilename.split('.')[0][2:]) - 1
        if result == answers[index]:
            pass
            if DEBUG:
                print 'OK!'
        else:
            if DEBUG:
                print 'Not right!'
            wrongjavafiles.append(javafilename)
    print 'java   files verified, total %s files' % len(javafiles)
    if wrongjavafiles:
        print 'These file(s) need fix(es):', " ".join(wrongjavafiles)

def verify_c(answers):
    curdir = os.path.abspath(os.path.dirname(__file__))
    curdir += '/c'
    cfiles = glob.glob(curdir + '/' + '*.c')
    wrongcfiles = []
    for cfile in cfiles:
        cfilename = cfile.split('/')[-1]
        if DEBUG:
            print cfilename, '   checked:', 
        cmd = 'gcc -Wall -std=c99 -lm %s' % cfilename
        result = subprocess.check_output(shlex.split(cmd), cwd=curdir)[:-1]
        assert result == ''
        cmd = './a.out'
        result = subprocess.check_output(shlex.split(cmd), cwd=curdir)[:-1]
        index = int(cfilename.split('.')[0][2:]) - 1
        if result == answers[index]:
            pass
            if DEBUG:
                print 'OK!'
        else:
            if DEBUG:
                print 'Not right!'
            wrongcfiles.append(cfilename)
    print 'c      files verified, total %s files' % len(cfiles)
    if wrongcfiles:
        print 'These file(s) need fix(es):', " ".join(wrongcfiles)

def verify_cpp(answers):
    curdir = os.path.abspath(os.path.dirname(__file__))
    curdir += '/cpp'
    cppfiles = glob.glob(curdir + '/' + '*.cpp')
    wrongcppfiles = []
    for cppfile in cppfiles:
        cppfilename = cppfile.split('/')[-1]
        if DEBUG:
            print cppfilename, ' checked:', 
        cmd = 'g++ -Wall %s' % cppfilename
        result = subprocess.check_output(shlex.split(cmd), cwd=curdir)[:-1]
        assert result == ''
        cmd = './a.out'
        result = subprocess.check_output(shlex.split(cmd), cwd=curdir)[:-1]
        index = int(cppfilename.split('.')[0][2:]) - 1
        if result == answers[index]:
            pass
            if DEBUG:
                print 'OK!'
        else:
            if DEBUG:
                print 'Not right!'
            wrongcppfiles.append(cppfilename)
    print 'cpp    files verified, total %s files' % len(cppfiles)
    if wrongcppfiles:
        print 'These file(s) need fix(es):', " ".join(wrongcppfiles)

def load_answers():
    answers = []
    for answer in open('answers.txt'):
        if answer.endswith('\n'):
            answers.append(answer[:-1])
        else:
            answers.append(answer)
    return answers

def main():
    answers = load_answers()
    threading.Thread(target=verify_python, args=(answers,)).start()
    threading.Thread(target=verify_java, args=(answers,)).start()
    threading.Thread(target=verify_c, args=(answers,)).start()
    threading.Thread(target=verify_cpp, args=(answers,)).start()

if __name__ == '__main__':
    main()
