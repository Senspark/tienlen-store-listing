#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "python ../../../store-listing-toolkit/populate-v3.py metadata -platform iOS -prj-path . -sheet 15WJ6dtUsROCkjmMaNj-BMp7CjOiFjB4B7MPD5hoHzq8 -customized-metadata-path ../src/itunes/metadata"
print cmd
os.system(cmd)
