"""
Created on 24 fevr. 2014

@author: ericvergnaud
"""

import inspect
import string

def extractTokenNames(lexerType):
    mod = inspect.getmodule(lexerType)
    mbs = inspect.getmembers(mod)
    names = [None] * len(mbs)
    for mb in mbs:
        if isinstance(mb[1],int) and mb[1]<len(names) and string.upper(mb[0])==mb[0]:
            names[mb[1]] = mb[0]
    return names


def getFullText(ctx):
    start = ctx.start
    stop = ctx.stop
    if start is None or stop is None or start.start < 0 or stop.stop < 0:
        return ctx.getText()
    return start.getInputStream().getText(start.start, stop.stop)
