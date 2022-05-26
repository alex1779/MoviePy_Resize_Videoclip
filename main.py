#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:24:11 2021

@author: rafa
"""

import argparse
import moviepy.editor as mp

# Concatenate Videoclips
parser = argparse.ArgumentParser(description='Concatenate Videoclips')
parser.add_argument('-i', '--input_path',
                    help='Please specify folder input', required=True)
parser.add_argument('-o', '--path_video_out',
                    help='Please specify full path video out', required=True)
parser.add_argument('-height', '--height', help='Please specify height for video', required=True)


opt = parser.parse_args()
pathIn = opt.input_path
pathOut = opt.path_video_out
height = int(opt.height)

clip = mp.VideoFileClip(pathIn)
clip_resized = clip.resize(height=height) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
clip_resized.write_videofile(pathOut)