#!/bin/bash

name='collection_5eplay.py'


pid=`ps -ef |grep $name|awk -F" " '{print $2}'|sort |head -n 1`


start(){
    nohup ./collection_5eplay.py >> ./5eplay.log 2>&1 &
    echo "start $name"
}

stop(){
    kill $pid
    echo "kill $name"
}

case "$1" in
start)
    start
    ;;
stop)
    stop
    ;;
*)
    echo "Usage:$0{start|stop}"
    exit 1
esac
