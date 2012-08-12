#!/usr/bin/python
import api
import pprint

# Get the data
profileURL = "http://us.battle.net/api/d3/profile/Freakinweird-1921/"
profileData = api.call(url=profileURL, last_modified = '1970-01-01 00:00:00', return_type = "JSON")

# Print it out
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(profileData)


