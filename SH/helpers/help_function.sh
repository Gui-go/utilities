#!/bin/bash

test_shadow(){
if [ -e /etc/shadow ];
then
    echo "/etc/shadow exists"
else
    echo "/etc/shadow does not exists"
fi
}

test_passwd(){
if [ -e /etc/passwd ];
then
    echo "/etc/passwd exists"
else
    echo "/etc/passwd does not exists"
fi
}

test_shadow
test_passwd