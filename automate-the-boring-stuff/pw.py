# pw.py - An insecure password locker program
import pyperclip
import sys

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAiVH5G8v01if1MLZF3sdt',
             'luggage': '12345',
             'slack': 'lakbacloalo29olebdo'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}')
