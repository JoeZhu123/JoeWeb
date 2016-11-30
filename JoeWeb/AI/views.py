from django.shortcuts import render

from django.shortcuts import render_to_response
from sqlalchemy import create_engine
import pandas as pd
import time


# Create your views here.
def AIIndex1(request):
    return render_to_response('AIIndex1.html')


def AIIndex2(request):
    con_data= create_engine('mysql://work1:123456@121.40.144.42/monitor')
    date = time.strftime('%Y%m%d', time.localtime(time.time()))
    cmd = "select * from {0} where trading_day={1} order by account".format("future_account_real", date)
    user_data = pd.read_sql(cmd, con_data)  # read table from sql

    columns_name = list(user_data.columns)
    # column name of the table
    new_user_data = list()  # user datas of the table
    for index, row in user_data.iterrows():
        new_user_data.append(list(row))

    return render_to_response("AIIndex2.html", locals())


# future strategy monitor
def AIIndex3(request):
    return render_to_response('AIIndex3.html')
