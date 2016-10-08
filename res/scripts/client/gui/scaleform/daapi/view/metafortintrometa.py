# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntroMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyIntroView import BaseRallyIntroView

class FortIntroMeta(BaseRallyIntroView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyIntroView
    """

    def as_setIntroDataS(self, data):
        """
        :param data: Represented by IntroViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setIntroData(data)