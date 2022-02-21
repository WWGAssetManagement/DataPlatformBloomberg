@ECHO ON 
title indexdata Start

cd C:\Users\w4\PycharmProjects\BloombergDataPlatform

set path="C:\ProgramData\Anaconda3"
set path="C:\ProgramData\Anaconda3\Library"
set path="C:\ProgramData\Anaconda3\Scripts"

call activate base 
python index_data_schedulers.py

cmd.exe 
