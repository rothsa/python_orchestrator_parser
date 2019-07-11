import json
import pytest

class Database:
    def __init__(self, line):
        self.line = line
        
    def test_name():
        pass

    def test_indent():
        pass

    def test_port():
        pass

    def test_self_line_number():
        pass

    def test_parent_line_number():
        pass   

    def test_cluster_line_number():
        pass

class Topology():
    def __init__(self, file):
        self.file = file

    def test_read():
        filepath = 'input.txt'  
        with open(filepath) as fp:  
            line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1

    def test_format():
        pass

    def test_output():
        pass

