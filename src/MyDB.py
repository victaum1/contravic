# myDB.py; use python3
#
# Imports
import json
# import pdb # debug
from functools import partial #functional style

def add_record(record,db):
    db.append(record)


# make query
def select(db,selector):
    rds = filter(selector,db)
    return list(rds)

def comp_2(key,dict1,dict2):
    if dict1[key]==dict2[key]:
        return True
    else:
        return False

def compare_records(dict1,dict2):
    keys=dict1.keys()
    ans=[]
    for item in keys:
        ans.append(comp_2(item,dict1,dict2))
    return all(ans)

# make selector
# Create the query to select
# Should be like '"key": value'
def where(clauses=""):
    clauses = '{'+clauses+'}'
    if is_valid_input(clauses):
        cls_map = json.loads(clauses)
    else: 
        cls_map = json.loads("{}")
    return partial(compare_records,cls_map)

