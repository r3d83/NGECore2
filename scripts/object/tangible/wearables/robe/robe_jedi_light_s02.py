import sys

def setup(core, object):
	return
	
def equip(core, actor, target):
	core.skillModService.addSkillMod(actor, 'constitution_modified', 145)
	core.skillModService.addSkillMod(actor, 'strength_modified', 145)
	
	return
	
def unequip(core, actor, target):
	core.skillModService.deductSkillMod(actor, 'constitution_modified', 145)
	core.skillModService.deductSkillMod(actor, 'strength_modified', 145)


	return
	