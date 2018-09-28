telphone=input('请输入手机号码： ')
if len(telphone)==11:
    if telphone.strip().isdigit():
        if telphone.startswith('187')or telphone.endswith('182'):
            print('中国移动！')
        if telphone.startswith('189')or telphone.endswith('130'):
            print('中国电信！')
        if telphone.startswith('166'):
            print('中国联通！')
        else:
            print('待确定！')
    else:
        print('手机号码格式错误!')

else:
    print('手机号码尾数不足！')
