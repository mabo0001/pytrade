import tushare as ts
import tradeTime as tt
import time


#remain_time_to_trade=tt.get_remain_time_to_trade()
#print(remain_time_to_trade)
interval=60
is_fist_run=True
while True:
    #"""
    remain_time_to_trade=tt.get_remain_time_to_trade()
    if remain_time_to_trade>=interval:
        time.sleep(remain_time_to_trade)
    else:
        if is_fist_run:
            time.sleep(60-time.time()%60)
            is_fist_run=False
        else:
            print(time.ctime())
            try:
                df=ts.get_today_all()
            except:
                continue
            print(df)
            if df.empty:
                time.sleep(interval)
                continue
            df_1=df[(df.trade<df.open*0.99) & (df.changepercent>1.5) & (df.high<df.settlement*1.09)]
            print(df_1)
            print(time.ctime())
            time.sleep(interval)
    #"""
 