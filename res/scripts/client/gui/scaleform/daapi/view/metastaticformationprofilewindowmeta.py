# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationProfileWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class StaticFormationProfileWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def actionBtnClickHandler(self, action):
        """
        :param action:
        :return :
        """
        self._printOverrideError('actionBtnClickHandler')

    def onClickHyperLink(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('onClickHyperLink')

    def as_setWindowSizeS(self, width, height):
        """
        :param width:
        :param height:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowSize(width, height)

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setFormationEmblemS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFormationEmblem(value)

    def as_updateFormationInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFormationInfo(data)

    def as_updateActionButtonS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateActionButton(data)

    def as_showViewS(self, idx):
        """
        :param idx:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showView(idx)