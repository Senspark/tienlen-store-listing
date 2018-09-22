#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "python ../../../store-listing-toolkit/populate-v3.py metadata -platform iOS -prj-path . -sheet 1Dee0sr3A3P_ipYWOUCtrWaX-Onrx4-8DxOUOnbCs_5M -customized-metadata-path ../src/itunes/metadata"
print cmd
os.system(cmd)
