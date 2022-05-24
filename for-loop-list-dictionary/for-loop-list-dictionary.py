#!/usr/bin/env python3.9

if __name__ == "__main__":
 
 intdict = {
     "GigabitEthernet0/1": "Server port number one",
     "GigabitEthernet0/2": "Server port number two",
     "GigabitEthernet0/3": "Server port number three"
 }

 interfaces = [
     {
         "name": "GigabitEthernet0/1",
         "desc": "uplink port",
         "uplink": True
     },
     {
         "name": "GigabitEthernet0/2",
         "desc": "Server port number two",
         "vlan": 10
     },
     {
         "name": "GigabitEthernet0/3",
         "desc": "Server port number three",
         "vlan": 10
     }

 ]
 from jinja2 import Environment, FileSystemLoader
 ENV = Environment(loader=FileSystemLoader('.'))
 template = ENV.get_template("for-loop-list-dictionary.j2")
 print(template.render(interface_list=interfaces))
