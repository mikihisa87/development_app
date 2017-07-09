import calendar


month = {"month_1":31, "month_2":28, "month_3":31, "month_4":30, "month_5":31, "month_6":30, 
"month_7":31, "month_8":31, "month_9":30, "month_10":31, "month_11":30, "month_12":31}

m = 0

for value in month.itervalues():
    m += value
print(m)