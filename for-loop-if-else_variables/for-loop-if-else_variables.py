#!/usr/bin/env python3.9

if __name__ == "__main__":
 intlist = [
     "GigabitEthernet0/1",
     "GigabitEthernet0/2",
     "GigabitEthernet0/3"
 ]
 from jinja2 import Environment, FileSystemLoader
 ENV = Environment(loader=FileSystemLoader('.'))
 template = ENV.get_template("for-loop-if-else_variables.j2")
 print(template.render(interface_list=intlist))
