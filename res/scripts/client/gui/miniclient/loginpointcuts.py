# Embedded file name: scripts/client/gui/miniclient/login/pointcuts.py
import aspects
from helpers import aop

class ShowBGWallpaper(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.login.LoginView', 'BackgroundMode', 'show$', aspects=(aspects.ShowBGWallpaper,))