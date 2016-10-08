# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleModulesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleModulesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onModuleHover(self, id):
        self._printOverrideError('onModuleHover')

    def onModuleClick(self, id):
        self._printOverrideError('onModuleClick')

    def onResetBtnBtnClick(self):
        self._printOverrideError('onResetBtnBtnClick')

    def onCompareBtnClick(self):
        self._printOverrideError('onCompareBtnClick')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by VehicleModulesWindowInitDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setItemS(self, nation, raw):
        if self._isDAAPIInited():
            return self.flashObject.as_setItem(nation, raw)

    def as_setNodesStatesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNodesStates(data)

    def as_setStateS(self, stateText, stateEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(stateText, stateEnabled)

    def as_setAttentionVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAttentionVisible(value)