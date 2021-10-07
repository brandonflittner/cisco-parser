import re
from ciscoconfparse import CiscoConfParse

def run():
    parse = CiscoConfParse('sw-config.txt', syntax='ios')
    for route_obj in parse.find_objects('^ip\sroute\s'):

        route_obj = route_obj.re_match_typed('^ip\sroute\s(\S+)(\S+)(\S+)')

        # Search children of all interfaces for a regex match and return
        # the value matched in regex match group 1.  If there is no match,
        # return a default value: ''
        print("{0}".format(route_obj))

run()
