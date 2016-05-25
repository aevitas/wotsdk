# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/BaseManageContactViewMeta.py
from messenger.gui.Scaleform.view.BaseContactView import BaseContactView

class BaseManageContactViewMeta(BaseContactView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseContactView
    null
    """

    def checkText(self, txt):
        """
        :param txt:
        :return :
        """
        self._printOverrideError('checkText')

    def as_setLabelS(self, msg):
        """
        :param msg:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setLabel(msg)

    def as_setInputTextS(self, msg):
        """
        :param msg:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInputText(msg)