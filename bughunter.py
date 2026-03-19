# =====================================================
# TOOL NAME  : BUG HUNTER
# AUTHOR     : Djendral (dhewa.my.id)
# VERSION    : 1.0
#
# DESCRIPTION:
# Tool sederhana untuk audit keamanan website
# (Info, Header, SQL error, XSS basic)
#
# NOTE:
# Gunakan hanya untuk website milik sendiri
# atau yang memberikan izin.
# =====================================================

import requests
import socket

def banner():
    print("""
========================================
          BUG HUNTER TOOL
========================================
Author : Djendral
Website: https://dhewa.my.id
========================================
""")

def info(target):
    print("\n[+] Info Domain")
    try:
        ip = socket.gethostbyname(target)
        print("Domain:", target)
        print("IP    :", ip)
    except:
        print("Gagal mengambil info")

def headers(target):
    print("\n[+] Security Headers")
    try:
        r = requests.get("http://" + target)
        for h in ["X-Frame-Options","Content-Security-Policy"]:
            if h in r.headers:
                print("[OK]", h)
            else:
                print("[MISSING]", h)
    except:
        print("Error cek header")

def sql_test(target):
    print("\n[+] SQL Test")
    try:
        r = requests.get("http://" + target + "/?id='")
        if "sql" in r.text.lower():
            print("[!] Possible SQL Error")
        else:
            print("[OK] Aman")
    except:
        print("Error")

def xss_test(target):
    print("\n[+] XSS Test")
    payload="<test>"
    try:
        r = requests.get("http://" + target + "/?q=" + payload)
        if payload in r.text:
            print("[!] Reflected Input")
        else:
            print("[OK] Aman")
    except:
        print("Error")

def main():
    banner()
    target = input("Masukkan domain: ")

    while True:
        print("""
MENU
1 Info Domain
2 Security Header
3 SQL Test
4 XSS Test
5 Exit
""")
        pilih = input("Pilih: ")

        if pilih == "1":
            info(target)
        elif pilih == "2":
            headers(target)
        elif pilih == "3":
            sql_test(target)
        elif pilih == "4":
            xss_test(target)
        elif pilih == "5":
            break

main()