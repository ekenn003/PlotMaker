# python/tools/tools.py
from xsecs import xsecs

def getXsec(sample):
    if sample in xsecs:
        return xsecs[sample]
    else:
        print 'No cross section info for {0}.'.format(sample)
        return 0.

