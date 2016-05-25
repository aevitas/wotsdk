# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DismissTankmanDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class DismissTankmanDialogMeta(SimpleDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleDialog
    null
    """

    def as_tankManS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_tankMan(value)