# coding:utf-8
import calendar

#期間を定義
min = 1
hour = min * 60
day = hour * 24
week = day * 7
#month_a = calendar.monthrange(input(),input())
month_1 = 31
month_2 = 28
month_3 = 31
month_4 = 30
month_5 = 31
month_6 = 30
month_7 = 31
month_8 = 31
month_9 = 30
month_10 = 31
month_11 = 30
month_12 = 31
year = day * 365

'''
#入力カラムを定義

#必須項目
morning_time = (input(),input())
commuter_time = (input(),input())
work_time = (input(),input())
lunch_time = (input(),input())
bath_time = (input(),input())
dinner_time = (input(),input())

#任意項目
over_time = (input(),input())
break_time = (input(),input())
drinking_time = (input(),input())
paid_vacation = (input(),input())
'''
'''
def calculate(summary):
    x = 0
    hour = 0
    minuts = 0
    while x < 10:
        x += 1
        summaryH = summary[x-1][0]
        summaryM = summary[x-1][1]
        hour += summaryH
        hour_minuts = hour * 60
        minuts += summaryM  
        total_time = hour_minuts + minuts
    print(total_time)
        
summary = morning_time,commuter_time,work_time,lunch_time,bath_time\
        ,dinner_time,over_time,break_time,drinking_time,paid_vacation
calculate(summary)
'''

#月単位で計算する場合
month = {"month_1":31, "month_2":28, "month_3":31, "month_4":30, "month_5":31, "month_6":30, 
"month_7":31, "month_8":31, "month_9":30, "month_10":31, "month_11":30, "month_12":31}

m = 0
for value in month.itervalues():
    m += value
    
Hour = 0   
Minuts = 0
total = {"morining_time":(input(),input()),"commuter_time":(input(),input()),"work_time":(input(),input()),"lunch_time":(input(),input())
        ,"bath_time":(input(),input()),"dinner_time":(input(),input()),"over_time":(input(),input())
        ,"break_time":(input(),input()),"drinking_time":(input(),input()),"paid_vacation":(input(),input())
        }
for H,M in total.values():
    Hour += H
    Hour_Minuts = Hour * 60
    Minuts += M
    Total_Time = Hour_Minuts + Minuts
print(Total_Time)