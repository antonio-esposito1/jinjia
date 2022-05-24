#!/usr/bin/env python3.9

if __name__ == "__main__":
 
 
 from jinja2 import Environment, FileSystemLoader
 import yaml

 ENV = Environment(loader=FileSystemLoader('.'))

 def get_interface_speed(interface_name):
     if 'gigabit' in interface_name.lower():
         return 1000
     if 'fast' in interface_name.lower():
         return 100

 ENV.filters['get_interface_speed'] = get_interface_speed
 template = ENV.get_template("for-loop-list-dictionary.j2")
 
 with open("data.yml") as f:
     interfaces = yaml.load(f)
     print(template.render(interface_list=interfaces))
