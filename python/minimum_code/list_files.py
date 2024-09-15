'''
リストアップ後に何か後続処理を行う場合を想定
'''

import glob
import os

PATH = '/mnt/c/Users/user/hoge/Service_name_help_contents/'
files = glob.glob(os.path.join(PATH, '*.mp4'))

for f in files:
    org = os.path.basename(f)
    print(org)
