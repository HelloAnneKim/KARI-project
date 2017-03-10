# Anne Kim
# Tidor Lab Spring 2017
# 03/10/2017
# Return the atom coordinates of the specified substrate

# Useful PyMol Scripting Resource: https://pymolwiki.org/index.php/Simple_Scripting
# select resn AC6
# iterate_state 1, sele, print x,y,z

from pymol import cmd, stored

def substrateCoord(substrate):
	print "Printing coordinates of substrate " + substrate + " ..."
	stored.sel = []
	cmd.select(substrate, "resn")
	cmd.iterate_state(1, selector.process(sele), "stored.sel.append([x,y,z])")
	print stored.sel
	print "All coordinates printed."

# The extend command makes this runnable as a command, from PyMOL.
cmd.extend("substrateCoord", substrateCoord)
