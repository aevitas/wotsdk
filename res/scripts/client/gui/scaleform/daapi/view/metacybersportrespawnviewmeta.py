# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportRespawnViewMeta.py
from gui.Scaleform.framework.entities.View import View

class CyberSportRespawnViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def as_setMapBGS(self, imgsource):
        """
        :param imgsource:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMapBG(imgsource)

    def as_changeAutoSearchStateS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchState(value)

    def as_hideAutoSearchS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideAutoSearch()