# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileBaseViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileBaseViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onHeaderButtonClick(self, actionId):
        """
        :param actionId:
        :return :
        """
        self._printOverrideError('onHeaderButtonClick')

    def as_setClanInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanInfo(data)

    def as_setHeaderStateS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderState(data)

    def as_setClanEmblemS(self, source):
        """
        :param source:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(source)

    def as_setDataS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(value)

    def as_showWaitingS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(value)

    def as_showDummyS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showDummy(data)

    def as_hideDummyS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideDummy()