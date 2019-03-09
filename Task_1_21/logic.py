# -*- coding: utf-8 -*-

# logic module


def itemexist(item, list):
	for i in list:
		if i == item:
			return True
	return False


def createlist(list1, list2):
	if (list1 is None) or (list2 is None):
		raise Exception("One of the lists is empty")
	newlist = []
	# fli - first list item
	# sli - second list item
	for fli in list1:
		if (fli == 0) or (abs(fli) == 1):
			continue
		for sli in list2:
			if ((sli != 0) and (abs(sli) != 1)) and (fli % sli == 0) and (abs(fli) != abs(sli)):
				if not itemexist(fli, newlist):
					newlist.append(fli)
	return newlist
