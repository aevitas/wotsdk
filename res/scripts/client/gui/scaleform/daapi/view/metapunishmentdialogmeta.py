# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PunishmentDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class PunishmentDialogMeta(SimpleDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleDialog
    null
    """

    def as_setMsgTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMsgTitle(value)