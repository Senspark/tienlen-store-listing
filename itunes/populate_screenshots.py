#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "python ../../../store-listing-toolkit/populate-v2.py screenshots -platform iOS -prj-path . -screenshots-path ../src/itunes/screenshots -customized-screenshots-path ../src/itunes/screenshots-overriden"
print cmd
os.system(cmd)
