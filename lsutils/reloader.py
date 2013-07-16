import sys
import imp

# Dependecy reloader for Emmet LiveStyle plugin
# The original idea is borrowed from 
# https://github.com/wbond/sublime_package_control/blob/master/package_control/reloader.py 

reload_mods = []
for mod in sys.modules:
	if mod.startswith('lsutils') and sys.modules[mod] != None:
		reload_mods.append(mod)

mods_load_order = [
	'lsutils.editor',
	'lsutils.pyv8loader',
	'lsutils.pyv8delegate',
	'lsutils.diff'
]

for mod in mods_load_order:
	if mod in reload_mods:
		imp.reload(sys.modules[mod])