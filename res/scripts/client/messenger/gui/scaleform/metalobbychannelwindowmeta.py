# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/LobbyChannelWindowMeta.py
from messenger.gui.Scaleform.view.lobby.SimpleChannelWindow import SimpleChannelWindow

class LobbyChannelWindowMeta(SimpleChannelWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleChannelWindow
    """

    def as_getMembersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMembersDP()

    def as_hideMembersListS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideMembersList()