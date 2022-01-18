#!/usr/bin/env python3

import textfsm
from textfsm import clitable
from pprint import pprint

with open("mac_dhcp_data.txt") as cmd_output:

    # Initialise CliTable with the content of the 'index' file.
    cli_table = clitable.CliTable('index', '.')
    # Firstly we will use attributes to match a 'show version' command on a Cisco device.
    attributes = {'Command': 'sh ip dhcp bi', 'Vendor': 'eltex'}
    # Parse Data
    cli_table.ParseCmd(cmd_output.read(), attributes)
    print(cli_table)
