# python/tools/tools.py
from xsections import xsecs

## ___________________________________________________________
def getXsec(sample):
    if sample in xsecs:
        return xsecs[sample]
    else:
        print 'No cross section info for {0}.'.format(sample)
        return 0.

