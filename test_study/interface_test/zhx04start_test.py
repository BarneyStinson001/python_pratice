# coding =utf-8
import zhx01config,zhx02function_for_api_test
import time

result=[]

for data in zhx01config.httpurl_date:
    sleeptime=data.get('time',0)
    if sleeptime:
        time.sleep(float(sleeptime))
    case= getattr(zhx02function_for_api_test, data['type'])(data)
    result.append(case)

for r in result :
    print(r)
