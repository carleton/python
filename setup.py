# Author: Matt Samudio
from setuptools import setup, find_packages
from distutils.version import StrictVersion
import sys
import os
import re

MOD = os.path.dirname(os.path.abspath(__file__))
IFN = os.path.join(MOD,'gam','__init__.py')

def pipver(minver='6.0.0'):
	bRet=True
	try:
		import pip
		if StrictVersion(pip.__version__) < StrictVersion(minver):
			sMsg="Upgrade pip, your version '{0}' is outdated. Minimum required version is '{1}':\n{2}"
			print(sMsg.format(pip.__version__, minver, 'Try: pip install --upgrade pip'))
			bRet=False
	except ImportError as e:
		sMsg="Failed to import pip, try: {0}"
		print(sMsg.format('pip3 install --upgrade pip'))
		bRet=False
	return bRet

def getver(initfile):
	with open(initfile, 'r') as fIn:
		haystack = fIn.read()
		match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", haystack, re.M)
		if not match:
			raise RuntimeError('Unable to find version string in %s.' % (initfile))
		return match.group(1)

ver = getver(IFN)
#reqs=['python-gnupg>=0.4.7']
reqs=[]

if pipver():
	setup(
		name='gam',
		version=ver,
		description='Carleton python modules',
		author='Matt Samudio',
		author_email='noreply@carleton.edu',
		url='https://github.com/carleton/python/',
		license='Apache License (2.0)',
		download_url='https://github.com/carleton/python/',
		classifiers=[
			'License :: OSI Approved :: Apache Software License',
			'Programming Language :: Python',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.4',
			"Programming Language :: Python :: 3.5",
			"Programming Language :: Python :: 3.6",
			"Programming Language :: Python :: 3.7",
			'Environment :: Console',
		],
		platforms=['Any'],
		scripts=[],
		provides=['gam'],
		packages=find_packages(),
		include_package_data=True,
		install_requires=reqs,
	#	dependency_links=links,
		zip_safe=False
	)
