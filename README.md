# Crumby

A password searching tool in description attribute of user accounts in an Active Directory.

## Installation

`pip install requirements.txt`

## Usage

Options :
- -s SERVER, --server SERVER : Server adress
- -a AUTH, --auth AUTH : Name and password (separated by :) of the account we want to connect to
- -d DOMAIN, --domain DOMAIN : The domain name

Example :
`python3 crumby.py -s 192.168.0.40 -a morgan.chloris:morgan123 -d cs.org`
