import json

class Database:
    def __init__(self, name, indent, port, line_number, parent):
        self.name = name
        self.indent = indent
        self.port = port
        self.line_number = line_number
        self.parent = None

    def pa

class Cluster:
    def __init__(self, cluster_line_number):
        self.cluster_line_number = cluster_line_number
        self.cluster_members = None

filepath = 'input.txt'  
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       if line
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
