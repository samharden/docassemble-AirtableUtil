from docassemble.base.util import get_config, DAObject, DAList, log
## Assuming you've added your airtable creds into the Config YAML:
at_api_key = get_config('AIRTABLE API KEY')
at_base_lmm = get_config('AT BASE LMM')

## Need to install package airtable-python-wrapper for this ##
import airtable
from airtable import Airtable
import json
import requests
## Insert your table name in place of 'Table Name':


def get_fields_from_intake(table_name):
  intake_table = Airtable(at_base_lmm, table_name, api_key=at_api_key)
  show_this = {}
  key_list = []
  intake_obj = DAObject('intake_obj')
  for rec in intake_table.get_all(max_records=1):
    log("HEEEEYYYYYYYYY")
    log(rec)
    for field in rec['fields']:
      key_list.append(str(field))
  log(key_list)
  for mf in key_list:
    # set field type based on name of field
    if 'Email' in mf:
      dt = 'email'
    elif 'Date' in mf:
      dt = 'date'
    elif 'Attachment' in mf:
      dt = 'file'
    else: 
      dt = ''
    show_this[str(mf)] = {'question': str(mf), 'label': str(mf), 'dt': dt }
  return show_this

def send_to_table(answer_dict, table_name):
  intake_table = Airtable(at_base_lmm, table_name, api_key=at_api_key)
  send_dict = {}
  for key, value in answer_dict.iteritems():
    if 'Attachment' in key:
      log(value)
      send_dict[key] = value['elements']['fullpath']
    else:
      send_dict[key] = str(value)
    
  intake_table.insert(send_dict)

  