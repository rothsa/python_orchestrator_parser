from ..steps import Databases

import pytest
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))
databases = Databases()

def test_data_present():
    lines = databases.data_present()
    logger.info(lines)
    assert lines >= 1 

def test_split_data():
    assert databases.split_data()

def test_database_name():
    line = '+ db061:3306[0s,ok,5.6.34-79.1-log,rw,STATEMENT,>>,P-GTID]\n'
    assert databases.database_name(line) is not None

def test_database_spaces():
    line = ' + db061:3306[0s,ok,5.6.34-79.1-log,rw,STATEMENT,>>,P-GTID]\n'
    assert databases.database_spaces(line) is 1

def test_output_dict():
    pass
    #    assert databases.output_dict() 

def test_write_output_file():
    pass
    assert databases.write_output_file()
