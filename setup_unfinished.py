#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from distutils.core import setup

setup(
	name='Jalapeno',
	version='0.0.1',
	author='Chenghao Qian',
	author_email='qch.jacob.jm@gmail.com',
	packages=['Jalapeno',
				'Jalepeno.lib',
				'Jalapeno.utils',
				'Jalapeno.views',
				'Jalapeno.configuration'],
	scripts=['Todooo/TODO'],
	package_data={'Todooo':['data/*.dat','data/usr/*/*.dat']},
	url='https://github.com/ChenghaoQ/Jalapeno',
	license='',
	description='Not yet not yet'
)