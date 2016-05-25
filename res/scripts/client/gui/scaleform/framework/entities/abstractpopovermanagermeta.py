# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/PopoverManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class PopoverManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def requestShowPopover(self, alias, data):
        """
        :param alias:
        :param data:
        :return :
        """
        self._printOverrideError('requestShowPopover')

    def requestHidePopover(self):
        """
        :return :
        """
        self._printOverrideError('requestHidePopover')

    def as_onPopoverDestroyS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onPopoverDestroy()