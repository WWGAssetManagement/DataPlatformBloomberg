@ECHO ON 
title indexdata Start

cd C:\Users\w4\PycharmProjects\BloombergDataPlatform

call activate base 
python index_data_schedulers.py

cmd.exe 
