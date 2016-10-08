# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBaseScorePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutBaseScorePanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_initS(self, maxValue, warningValue):
        if self._isDAAPIInited():
            return self.flashObject.as_init(maxValue, warningValue)

    def as_playScoreHighlightAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playScoreHighlightAnim()

    def as_stopScoreHighlightAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_stopScoreHighlightAnim()