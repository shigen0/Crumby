from ldap3 import Server, Connection, ALL

def connection(host,auth,domain):   
    server = Server(host, use_ssl=False, get_info=ALL)
    ids = auth.split(':')
    username = ids[0]
    password = ids[1]
    return Connection(server, username+"@"+domain, password, auto_bind=True),server