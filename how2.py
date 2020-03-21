import re
import datetime
filename_weibo = '2523185197.txt'
filename_myarg = 'myargs.txt'
line_num = 0
with open(filename_myarg,encoding='utf-8') as f_obj:
    for line in f_obj:
        pattern = re.compile(r'(day=)(\d+)')
        m = pattern.match(line) 
        day = int (m.group(2))
with open(filename_weibo,encoding='utf-8') as f_obj:
    for line in f_obj:
        line_num = line_num +1
sent_num = 10
line_num_start = line_num - 3*(day-1)*sent_num
line_num_end = line_num_start - 3*sent_num+1
line_num = 0
sent_text=""
i = 1
with open(filename_weibo,encoding='utf-8') as f_obj:
    for line in f_obj:
        line_num = line_num +1
        if line_num >= line_num_end and line_num<=line_num_start:
            if line_num%3==0:
                line = "第%s条微博\n"%str(i)
                i+=1
            sent_text = sent_text + line
        if line_num > line_num_start:
            break
today=datetime.date.today()
filename_sent_text = str(today)+".txt"
with open(filename_sent_text,'w',encoding='utf-8') as fh:
    fh.write("柏浪涛的刑法观\n")
    fh.write("Day=%d\n"%day)
    fh.write("Make By Howbin\n")
    fh.write(str(today)+"\n")
    fh.write(sent_text)