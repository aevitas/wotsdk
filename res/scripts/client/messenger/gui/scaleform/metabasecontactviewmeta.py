# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/BaseContactViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseContactViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onOk(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('onOk')

    def onCancel(self):
        """
        :return :
        """
        self._printOverrideError('onCancel')

    def as_updateS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)

    def as_setOkBtnEnabledS(self, isEnabled):
        """
        :param isEnabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOkBtnEnabled(isEnabled)

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_closeViewS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_closeView()