#!/bin/bash
killall vlc
cvlc http://127.0.0.1:8888/$1.m3u8
