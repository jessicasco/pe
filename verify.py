#!/usr/bin/env python
import subprocess
import shlex
import glob
import os

def verify_python(answers):
    olddir = os.getcwd()
    os.chdir('python')
    pyfiles = glob.glob('*.py')
    for pyfile in pyfiles:
        cmd = 'python %s' % pyfile
        result = subprocess.check_output(shlex.split(cmd))[:-1]
        index = int(pyfile.split('/')[-1].split('.')[0][2:]) - 1
        assert result == answers[index], index
    print 'python files verified, total %s files' % len(pyfiles)
    os.chdir(olddir)

def verify_java(answers):
    olddir = os.getcwd()
    os.chdir('java')
    javafiles = glob.glob('*.java')
    for javafile in javafiles:
        cmd = 'javac %s' % javafile
        result = subprocess.check_output(shlex.split(cmd))[:-1]
        assert result == ''
        cmd = 'java %s' % javafile.split('.')[0]
        result = subprocess.check_output(shlex.split(cmd))[:-1]
        index = int(javafile.split('/')[-1].split('.')[0][2:]) - 1
        assert result == answers[index], index
    print 'java   files verified, total %s files' % len(javafiles)
    os.chdir(olddir)

def verify_c(answers):
    olddir = os.getcwd()
    os.chdir('c')
    cfiles = glob.glob('*.c')
    for cfile in cfiles:
        cmd = 'gcc -Wall -std=c99 -lm %s' % cfile
        result = subprocess.check_output(shlex.split(cmd))[:-1]
        assert result == ''
        cmd = './a.out'
        result = subprocess.check_output(shlex.split(cmd))[:-1]
        index = int(cfile.split('/')[-1].split('.')[0][2:]) - 1
        assert result == answers[index], index
    print 'c      files verified, total %s files' % len(cfiles)
    os.chdir(olddir)

def verify_cpp(answers):
    olddir = os.getcwd()
    os.chdir('cpp')
    cppfiles = glob.glob('*.cpp')
    for cppfile in cppfiles:
        cmd = 'g++ -Wall %s' % cppfile
        result = subprocess.check_output(shlex.split(cmd))[:-1]
        assert result == ''
        cmd = './a.out'
        result = subprocess.check_output(shlex.split(cmd))[:-1]
        index = int(cppfile.split('/')[-1].split('.')[0][2:]) - 1
        assert result == answers[index], index
    print 'cpp    files verified, total %s files' % len(cppfiles)
    os.chdir(olddir)

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
    verify_python(answers)
    verify_java(answers)
    verify_c(answers)
    verify_cpp(answers)

if __name__ == '__main__':
    main()
