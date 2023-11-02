from os.path import expanduser
import sys
import json
import csv

__all__ = [
    'Drive'
]

class Storage(object):
	def __init__(self):
		self.sTxt=''

class Drive(Storage):
	def __init__(self):
		super(Storage,self).__init__()
		self.sJSON = {}

	def csvDumpByIdx(self,filename):
		with open(filename) as aCSV:
			rdr = csv.reader(aCSV)
			lno = 0
			for row in rdr:
				lno += 1
				line = None
				for fld in row:
					if line:
						line += ','+str(fld)
					else:
						line = str(fld)
				print('%d:%s' % (lno,line))
			aCSV.close()

	def csvDump(self,filename):
		with open(filename) as aCSV:
			rdr = csv.DictReader(aCSV)
			keys = []
			lno = 0
			for row in rdr:
				lno += 1
				line = None
				for key in row:
					if lno < 2:
						keys.append(key)
					fld = str(row[key])
					line = line+','+fld if line else fld
				if lno < 2:
					keyline=None
					for key in keys:
						keyline = keyline+','+str(key) if keyline else str(key)
					print('%d:%s' % (0,keyline))
				print('%d:%s' % (lno,line))
			aCSV.close()

	def csvCut(self,filename,fields):
		with open(filename) as aCSV:
			line = None
			for key in fields:
				line = line+','+str(key) if line else str(key)
			print('%s:%s' % (str(0).rjust(6),line))
			rdr = csv.DictReader(aCSV)
			line = None
			lno = 0
			for row in rdr:
				lno += 1
				line = None
				for key in fields:
					fld = str(row[key])
					line = line+','+fld if line else fld
				print('%s:%s' % (str(lno).rjust(6),line))
			aCSV.close()

	def gamListUsers(self):
		pass

	def gamListUserFiles(self,user):
		print('%s=>>> gam user %s print filelist id name' % ('DBG',user),file=sys.stderr)

	def gamReportUserFiles(self,user,csv='rpt.csv'):
		print('%s=>>> gam user %s show filelist allfields > %s' % ('DBG',user,csv),file=sys.stderr)

	def gamRemoveFile(self,user,fileid):
		print('%s=>>> gam user %s delete drivefile %s purge' % ('DBG',user,fileid),file=sys.stderr)

	def gamBatchRemoveFiles(self,batchcsv):
		print("%s=>>> gam csv %s gam user '~user' delete drivefile '~id' purge" % ('DBG',batchcsv),file=sys.stderr)
