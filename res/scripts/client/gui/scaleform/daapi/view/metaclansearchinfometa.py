# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanSearchInfoMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanSearchInfoMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def sendRequest(self):
        """
        :return :
        """
        self._printOverrideError('sendRequest')

    def openClanProfile(self):
        """
        :return :
        """
        self._printOverrideError('openClanProfile')

    def requestData(self, clanId):
        """
        :param clanId:
        :return :
        """
        self._printOverrideError('requestData')

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setStateDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStateData(data)

    def as_setEmblemS(self, emblem):
        """
        :param emblem:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setEmblem(emblem)

    def as_setWaitingVisibleS(self, visible):
        """
        :param visible:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitingVisible(visible)

    def as_setDummyS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)

    def as_setDummyVisibleS(self, visible):
        """
        :param visible:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)