# Crumby

A password searching tool in description attribute of user accounts in Active Directory, with spraying functionnality.

## Installation

`pip install requirements.txt`

## Usage

Options :
- -s SERVER, --server SERVER : Server adress
- -a AUTH, --auth AUTH : Name and password (separated by :) of the account we want to connect to
- -d DOMAIN, --domain DOMAIN : The domain name
- -sp : For spraying the passwords found 

Example :
`python3 src/crumby.py -s 192.168.0.40 -a morgan.chloris:morgan123 -d cs.org -sp`

## Demonstration

![Demo gif](./crumby.gif)
