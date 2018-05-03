#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 13:56:48 2018

@author: Hank
"""

import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\Hank\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Hank\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("DodgeGame_V2.py")]

cx_Freeze.setup(
        version="22.99",
        name = "Dodge Game v2.0",
        options={"build_exe":{"packages":["pygame"],
                              "include_files":["C:\smash.wav","C:\winwin2.wav"]}},
        executables = executables
                              
                             
                              
        )
