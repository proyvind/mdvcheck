import perl

perlmod = perl.require("URPM");
class URPM(object):
    def __init__(self):
	self.urpm = perl.callm("new", "URPM")
	self.pkgs = []

    def parse_hdlist(self, path, packing=0, keep_all_tags=0):
	return perl.callm_tuple("parse_hdlist",self.urpm, path, {packing:packing, keep_all_tags:keep_all_tags})

    def __ret(self, pkg):
	self.pkgs.append(Package(pkg))

    def load(self):
	perl.callm_tuple("traverse", self.urpm, self.__ret)

class DB(object):
    def __init__(self, path=None, write=0):
	self.db = perl.callm_tuple("open", "URPM::DB", path, write)

    def __ret(self, pkg):
	self.pkgs.append(Package(pkg))

    def load(self):
	perl.callm_tuple("traverse", self.db, self.__ret)

class Package(object):
    def __init__(self, pkg):
	self.pkg = pkg

    def get_tag(self, tag):
	value = perl.callm_tuple("get_tag", self.pkg, tag)
	if len(value) == 1:
	    return value[0]
	else:
	    return value


