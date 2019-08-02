#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:03:44 2019

@author: tianmengxu
"""


def make_album(songer_name,songer_album,number_songs=''):
    song={'name':songer_name,'album':songer_album}
    if number_songs:
        song['number_songs']=number_songs
    return song
while True:
    songer_n=input('请输入歌手名：')
    
    songer_a=input('请输入专辑名，输入确认完成输入并退出：')
    if songer_a=='确认':
        break
    like111 = make_album(songer_n,songer_a)
print(like111)
    


