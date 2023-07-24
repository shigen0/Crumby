import argparse
from search import *

def crumby(host,auth,domain):
    print("""
   _____                      _           
  / ____|                    | |          
 | |     _ __ _   _ _ __ ___ | |__  _   _ 
 | |    | '__| | | | '_ ` _ \| '_ \| | | |
 | |____| |  | |_| | | | | | | |_) | |_| |
  \_____|_|   \__,_|_| |_| |_|_.__/ \__, |
                                     __/ |
                                    |___/                                       
    """)
    # Get the number and values of dumped passwords
    nbr_success,users_success = search_passwords(host,auth,domain)

    print("[*] Report")
    print("[*] Number of dumped passwords : "+str(nbr_success))
    print("[*] Accounts cracked : "+str(users_success))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Password searching tool in object descriptions')
    parser.add_argument('-s', '--server', type=str, help='Server adress', required=True)
    parser.add_argument('-a', '--auth', type=str, help='Name and password (separated by :) of the account we want to connect to',required=True)
    parser.add_argument('-d', '--domain', type=str, help='Domain name',required=True)
    args = parser.parse_args()
    crumby(args.server,args.auth,args.domain)
