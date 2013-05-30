#/usr/bin/env python
# -*- coding:utf8 -*-


#------------------------------------------------------------------------------------------------
# Function:
#
#-----------------------------------------------------------------------------------------------

import re
import logging
import codecs

class UniPats(object):
	def __init__(self, logger):
		self.logger = logger
		self.logger.info("UniPats initialing...")
	
	def hzPat(self):
		return re.compile(ur"[\u4E00-\u9FFF]+")
	def numPat(self):
		return re.compile("[0-9]+")
	def puncDic(self, puncfile):
		ppunc = codecs.open(puncfile, 'r', encoding="utf8")
		self.puncs = {}
		for iline in ppunc:
			iline = iline.strip()
			if iline[0] == "#":
				continue
			curpunc = re.split("\t", iline)[0]
			if self.puncs.has_key(curpunc):
				continue
			else:
				self.puncs[curpunc] = None
		return self.puncs
	def alphaPat(self):
		return re.compile("[a-zA-Z]+")

		ppunc.close()

def test():
    import logging
    logger = logging.getLogger()
    pats =  UniPats(logger)
    numpat = pats.numPat()
    assert re.search(numpat, "12908").group(0) == "12908"
    hzpat = pats.hzPat()
    assert re.search(hzpat, u"中国制造").group(0) == u"中国制造"
    alphapat = pats.alphaPat()
    assert re.search(alphapat, "madeinChina").group(0) == "madeinChina"
    puncfile = "punc.txt"
    puncdic = pats.puncDic(puncfile)
    assert "." in puncdic

if __name__ == "__main__":
    test()
		
