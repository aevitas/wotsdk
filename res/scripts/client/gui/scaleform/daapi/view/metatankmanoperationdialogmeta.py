# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankmanOperationDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class TankmanOperationDialogMeta(SimpleDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleDialog
    """

    def as_setDataS(self, data):
        """
        :param data: Represented by TankmanOperationDialogVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)