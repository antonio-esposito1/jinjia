#!/usr/bin/env python3.9

if __name__ == "__main__":
 
 intdict = {
     "GigabitEthernet0/1": "Server port number one",
     "GigabitEthernet0/2": "Server port number two",
     "GigabitEthernet0/3": "Server port number three"
 }
 from jinja2 import Environment, FileSystemLoader
 ENV = Environment(loader=FileSystemLoader('.'))
 template = ENV.get_template("for-loop-if-else_variables_dictionary.j2")
 print(template.render(interface_dict=intdict))
