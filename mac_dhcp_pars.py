#!/usr/bin/env python3

import textfsm
from textfsm import clitable
from pprint import pprint

with open("mac_dhcp_data.txt") as f, open('eltex2348p_dhcp_mactab.template') as tmpl:
   fsm = textfsm.TextFSM(tmpl)
   result = fsm.ParseText(f.read())
   print(fsm.header)
   pprint(result)
