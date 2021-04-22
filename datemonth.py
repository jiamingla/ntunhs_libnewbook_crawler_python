import datetime 
datetime_dt = datetime.datetime.today() # 獲得當地時間
dt = datetime_dt.date() # 最小日期顯示到日
print("現在是 {}年 {}月 {}日".format(dt.year, dt.month, dt.day))
