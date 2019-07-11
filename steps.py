import logging
import collections
import json
import re
import sys
import os 


class Databases():
    
        #Read in the data
        #Initialize the DBs
    def __init__(self):
        #self.logger = logging.getLogger(__name__)
        #self.logger.setLevel(logging.DEBUG)
        #self.logger.addHandler(logging.StreamHandler(sys.stdout))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = ("{}/input.txt").format(dir_path)
        #self.logger.info(path)
        self.file = open(path, "r").readlines()
        self.database_collection = collections.OrderedDict()
        self.formatted_collection = collections.OrderedDict()
    
    def data_present(self):
        i=0
        for line in self.file:
            i+=1
        return i
    
    #Split the data by space into a dict including instance name, and index value, number of spaces"
    def split_data(self): 
        i=0
        for line in self.file:
            i+=1
            name = self.database_name(line)
            spaces = self.database_spaces(line)
            self.database_collection[i] = {"spaces": spaces, "name": name}
        return self.database_collection

    def database_name(self, line):
        name = re.search(r'db\d+:\d+', line).group()
        return name

    def database_spaces(self, line):
        spaces = re.search(r'^\s+', line)
        if spaces:
            spaces_count = spaces.group().count(" ")
            return spaces_count
        
    #Iterate through the dict and output an array of nested dicts with the same hierarchy and order of the initial orchestrator output
    def output_dict(self):
        data = self.split_data()
        for k, v in data.items():
            if v["spaces"] is None:
                formatted_dict["instance: {}").format(v["name"])] = [] 
            else 
                data[k-1]
            return (json.dumps(string, indent=4)
    
    #Write to output file
    def write_output_file(self):
        output_file = open("output.txt","w+")
        output_file.write(self.output_dict())
