import ConfigParser

def read(inifile):
	config = ConfigParser.RawConfigParser(allow_no_value=True)
	config.optionxform = str # this makes options case-sensitive
	config.readfp(open(inifile))
	for section in config.sections():
		print (section)
	return config