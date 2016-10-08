# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanSearchInfoMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanSearchInfoMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def sendRequest(self):
        self._printOverrideError('sendRequest')

    def openClanProfile(self):
        self._printOverrideError('openClanProfile')

    def requestData(self, clanId):
        self._printOverrideError('requestData')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by ClanSearchInfoInitDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanSearchInfoDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setStateDataS(self, data):
        """
        :param data: Represented by ClanSearchInfoStateDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStateData(data)

    def as_setEmblemS(self, emblem):
        if self._isDAAPIInited():
            return self.flashObject.as_setEmblem(emblem)

    def as_setWaitingVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitingVisible(visible)

    def as_setDummyS(self, data):
        """
        :param data: Represented by DummyVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)

    def as_setDummyVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)