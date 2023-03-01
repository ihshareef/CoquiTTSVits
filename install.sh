#!/bin/bash

# set up python virtual environment
python3.8 -m venv vits-tts
# source the new virtual environment
source vits-tts/bin/activate

#Install the git repository
git clone git@github.com:ihshareef/CoquiTTSVits.git TTS

# install package
cd TTS
pip install -e .[all]
cd ..

CUDA_VISIBLE_DEVICES=0 python TTS/TTS/bin/train_vits.py 




