#!/usr/bin/env python

""" 
Module containing different utils
"""

def print_json(j, prefix=''):
    """ Pretty printing of JSON objects """
    for key, value in j.items():
        if isinstance (value, dict):
            print '%s%s' % (prefix, key)
            print_json(value, prefix+'  ')
        else:
            print '%s%s:%s' % (prefix, key, value)
