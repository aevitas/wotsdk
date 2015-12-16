# Embedded file name: scripts/client/Vivox/__init__.py
from ResponseHandler import ResponseHandler
import BigWorld

def getResponseHandler():
    if not globals().has_key('__handler'):
        globals()['__handler'] = ResponseHandler()
        BigWorld.VOIP.setHandler(__handler.channelsMgr)
    return __handler