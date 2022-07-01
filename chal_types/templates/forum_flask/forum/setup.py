from database import *

import os
def init_site():
	admin = add_subforum("Forum", "Announcements, bug reports, and general discussion about the forum belongs here")
	add_subforum("Announcements", "View forum announcements here",admin)
	add_subforum("Bug Reports", "Report bugs with the forum here", admin)
	add_subforum("General Discussion", "Use this subforum to post anything you want")
	add_subforum("Other", "Discuss other things here")

def add_subforum(title, description, parent=None):
	sub = Subforum(title, description)
	if parent:
		for subforum in parent.subforums:
			if subforum.title == title:
				return
		parent.subforums.append(sub)
	else:
		subforums = Subforum.query.filter(Subforum.parent_id == None).all()
		for subforum in subforums:
			if subforum.title == title:
				return
		db.session.add(sub)
	print("adding " + title)
	db.session.commit()
	return sub
"""
def interpret_site_value(subforumstr):
	segments = subforumstr.split(':')
	identifier = segments[0]
	description = segments[1]
	parents = []
	hasparents = False
	while('.' in identifier):
		hasparents = True
		dotindex = identifier.index('.')
		parents.append(identifier[0:dotindex])
		identifier = identifier[dotindex + 1:]
	if hasparents:
		directparent = subforum_from_parent_array(parents)
		if directparent is None:
			print(identifier + " could not find parents")
		else:
			add_subforum(identifier, description, directparent)
	else:
		add_subforum(identifier, description)

def subforum_from_parent_array(parents):
	subforums = Subforum.query.filter(Subforum.parent_id == None).all()
	top_parent = parents[0]
	parents = parents[1::]
	for subforum in subforums:
		if subforum.title == top_parent:
			cur = subforum
			for parent in parents:
				for child in subforum.subforums:
					if child.title == parent:
						cur = child
			return cur
	return None


def setup():
	siteconfig = open('./config/subforums', 'r')
	for value in siteconfig:
		interpret_site_value(value)
"""
