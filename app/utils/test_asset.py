import os
from flask import url_for
current_path = os.getcwd()



def tree(current_path,current_dir=''):
	L={}
	content = os.listdir(current_path)
	for each in content:
		each_path = current_path+os.sep+each
		print(each_path)
		if each[0]=='.' or 'img' in each:
			continue
		elif os.path.isdir(each_path):
			L[each]=tree(each_path,each)
		else:
			#L[each.split('.',1)[0]] = current_dir+os.sep+each
			L[each.split('.',1)[0]] = url_for('static',filename=current_dir+os.sep+each)
	return L




class MGR(object):

	def __init__(self):
		pass
	def tree(current_path,current_dir=''):
		L={}
		content = os.listdir(current_path)
		print(content)
		for each in content:
			each_path = current_path+os.sep+each
			print(each_path)
			if each[0]=='.' or 'img' in each:
				continue
			elif os.path.isdir(each_path):
				L[each]=self.tree(each_path,each)
			else:
				#L[each.split('.',1)[0]] = current_dir+os.sep+each
				
		return L
	def url_dict(self):
		pass	




