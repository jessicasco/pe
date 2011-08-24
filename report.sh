#!/bin/bash

main() {
    report="<table border='1'>"
    report="$report
        <tr>
            <th>&nbsp;</th>
            <th>Python</th>
            <th>Java</th>
            <th>Cpp</th>
            <th>C</th>
        </tr>"

    cd python
    num=`ls -l *.py | wc -l`
    cd ..

    for i in `seq 1 $num`
    do
        report="$report <tr>"
        report="$report <td>$i</td>"

        cd python
        fname=`printf "PE%03d.py" $i`
        timeout=`( time python $fname )  2>&1 1>/dev/null`
        timeout=`echo $timeout | awk '{ print $1 "\t" $2 "<br>" $3 "\t" $4 "<br>" $5 "\t" $6 "<br>" }'`
        report="$report <td>$timeout</td>"
        cd ..

        cd java
        fname=`printf "PE%03d.java" $i`
        javac $fname
        timeout=`( time java ${fname%.java} )  2>&1 1>/dev/null`
        timeout=`echo $timeout | awk '{ print $1 "\t" $2 "<br>" $3 "\t" $4 "<br>" $5 "\t" $6 "<br>" }'`
        report="$report <td>$timeout</td>"
        cd ..

        cd cpp
        fname=`printf "PE%03d.cpp" $i`
        g++ -Wall -lm $fname
        timeout=`( time ./a.out )  2>&1 1>/dev/null`
        timeout=`echo $timeout | awk '{ print $1 "\t" $2 "<br>" $3 "\t" $4 "<br>" $5 "\t" $6 "<br>" }'`
        report="$report <td>$timeout</td>"
        cd ..

        cd c
        fname=`printf "PE%03d.c" $i`
        gcc -Wall -lm -std=c99 $fname
        timeout=`( time ./a.out )  2>&1 1>/dev/null`
        timeout=`echo $timeout | awk '{ print $1 "\t" $2 "<br>" $3 "\t" $4 "<br>" $5 "\t" $6 "<br>" }'`
        report="$report <td>$timeout</td>"
        cd ..

        report="$report </tr>"
    done

    report="$report </table>"
    echo "$report" > report.html
}
main
