# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationProfileWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class StaticFormationProfileWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def actionBtnClickHandler(self, action):
        self._printOverrideError('actionBtnClickHandler')

    def onClickHyperLink(self, value):
        self._printOverrideError('onClickHyperLink')

    def as_setWindowSizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowSize(width, height)

    def as_setDataS(self, data):
        """
        :param data: Represented by StaticFormationProfileWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setFormationEmblemS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setFormationEmblem(value)

    def as_updateFormationInfoS(self, data):
        """
        :param data: Represented by StaticFormationProfileEmblemVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFormationInfo(data)

    def as_updateActionButtonS(self, data):
        """
        :param data: Represented by StaticFormationProfileButtonInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateActionButton(data)

    def as_showViewS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_showView(idx)