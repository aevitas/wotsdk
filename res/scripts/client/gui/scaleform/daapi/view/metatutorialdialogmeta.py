# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TutorialDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def submit(self):
        """
        :return :
        """
        self._printOverrideError('submit')

    def cancel(self):
        """
        :return :
        """
        self._printOverrideError('cancel')

    def as_setContentS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setContent(data)

    def as_updateContentS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateContent(data)