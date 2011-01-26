#!/usr/bin/env python

from URPM import *

urpm = URPM()

urpm.parse_hdlist("/var/cache/urpmi/rpms/media_info/hdlist.cz")

urpm.load()
for p in urpm.pkgs:
    print p.get_tag("nvra")

db = DB()
db.load()

for p in db.pkgs:
    print p.get_tag("nvra")

