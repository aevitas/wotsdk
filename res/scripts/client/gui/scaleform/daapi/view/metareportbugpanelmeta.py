# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReportBugPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ReportBugPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def reportBug(self):
        """
        :return :
        """
        self._printOverrideError('reportBug')

    def as_setHyperLinkS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHyperLink(value)