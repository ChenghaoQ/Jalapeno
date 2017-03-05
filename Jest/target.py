        def target(tar,dirs,key='',relative=True):
                '''
                        find and return a specific file dict by name under root path
                        target: specific dir name
                        url:
                                True: url_for with relative path
                                False: relative path
                                None: Nothing change
                '''
                
		hold = dirs
                for k,v in dirs.items():
                        if isinstance(v,dict):
                                hold = target(tar,key=k,dirs=v)
                                if hold:return hold 
                        elif relative:
                                dirs[k]=dirs[k].split(tar+os.sep,1)[-1]
                        else:
                                pass
                                #relative = dirs[k].split(target+os.sep,1)[-1]
                                #dirs[k] = url_for('static',filename=relative)
                return dirs if key == tar else None
