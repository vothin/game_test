# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: global_path.py
    @time: 2019/12/12 11:25
    @desc:
'''
# ********************************************************

import os, sys

BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BIR)


