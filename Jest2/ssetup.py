#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from setuptools import setup
OPTIONS = dict(py2app=dict(argv_emulation=True,
				includes=['Jalapeno'
				# ,
				# 'Jalapeno.lib*.*',
				# 'Jalapeno.utils*.*',
				# 'Jalapeno.views*.*',
				# 'Jalapeno.GUI*.*'],
				],
				packages=['markdown',
						'flask',
						'pygments',
						'markupsafe',
						'flask_flatpages',
						'flask_frozen','Jalapeno',
				'Jalapeno.lib',
				'Jalapeno.utils',
				'Jalapeno.views',
				'Jalapeno.GUI' ]))
data_files=['Jalapeno/Sites','Jalapeno/theme']
setup(
	app=['Jaloc'],
	name='Jalapeno',
	version='0.1.3',
	author='Chenghao Qian',
	author_email='qch.jacob.jm@gmail.com',
	data_files=data_files,
	include_package_data=True,

	scripts=['Jalapeno/Jaloc','Jalapeno/Jalo'],
	url='https://github.com/ChenghaoQ/Jalapeno',
	license='GPL',
	description='Static Site Generator based on Flask',
	keywords= ['Flask','Blog','site Generator','static site'],
	options=OPTIONS,
	setup_requires=['py2app']
)
