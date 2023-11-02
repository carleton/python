# Author:  Matt Samudio
from __future__ import absolute_import
from __future__ import print_function
from os.path import expanduser
import json
import gnupg

__all__ = [
    'ArtifactJson',
    'ArtifactCredentials'
]

class ArtifactGnuPG(object):

	def __init__(self):
		self.encoding='utf-8'
		self.sDir=expanduser("~")+"/.gnupg"
		self.bRendered=False
		self.sTxt=''

	def txtRender(self):
	#	print( "%s=>>> %s" % ('DBG','ArtifactGnuPG::txtRender invoked'))
		pass

	def __str__(self):
		if not self.bRendered:
			self.txtRender()
			self.bRendered=True
		return(self.sTxt)

	def _parse(self,txt):
		return txt

	def decrypt(self,sTxt,isFilename=False):
		sRet=None
		pGPG=None
	#	If one convention fails, try the other ...
		try:
			pGPG = gnupg.GPG(homedir=self.sDir)
		except:
			pGPG = gnupg.GPG(gnupghome=self.sDir)
	#	...
		pGPG.encoding = 'utf-8'
		try:
			sDat=None
			if isFilename:
				pDat=None
			#	print( "%s=>>> opening credentials file: %s" % ('DBG',sFile))
				with open(sTxt,'r') as fIn:
					pDat = fIn.read()
				#	print( "%s=>>> raw data: %s" % ('DBG',pDat))
					try:
					#	NOTE: versions of python-gnupg prior to 3.0.3 produce
					#	an exception in another thread after the decryption
					#	is complete, which is (mostly) harmless.
					#	https://github.com/isislovecruft/python-gnupg/pull/220
						sDat = pGPG.decrypt(str(pDat),always_trust=True)
					except:
						pass
			else:
				try:
					sDat = pGPG.decrypt(sTxt,always_trust=True)
				except:
					pass
		#	Allow sub-class to parse/process ...
			sRet = self._parse(sDat)
		except Exception as pE:
			print(pE)
		return(str(sRet))

class ArtifactJson(ArtifactGnuPG):

	def __init__(self):
		super(ArtifactJson, self).__init__()
		self.sJson = {}

	def _parse(self,txt):
		self.sJson = json.loads(str(txt))
		return json.dumps(self.sJson)

	def json(self):
		return self.sJson
	
	def txtRender(self):
		self.sTxt = json.dumps(self.sJson)

class ArtifactCredentials(ArtifactJson):

	def __init__(self):
		super(ArtifactCredentials,self).__init__()
		self.sLogin=None
		self.sPassword=None
		self.sToken=None

	def _parse(self,txt):
		super(ArtifactCredentials,self)._parse(txt)
		nfo = self.json()
		self.sLogin = nfo.get('login')
		self.sPassword = nfo.get('password')
		self.sToken = nfo.get('token')

	def login(self):
		return self.sLogin

	def password(self):
		return self.sPassword

	def token(self):
		return self.sToken
