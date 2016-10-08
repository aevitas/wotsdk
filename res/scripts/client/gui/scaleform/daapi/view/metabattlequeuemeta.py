# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleQueueMeta.py
from gui.Scaleform.framework.entities.View import View

class BattleQueueMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def startClick(self):
        self._printOverrideError('startClick')

    def exitClick(self):
        self._printOverrideError('exitClick')

    def onEscape(self):
        self._printOverrideError('onEscape')

    def as_setTimerS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(text)

    def as_setTypeInfoS(self, data):
        """
        :param data: Represented by BattleQueueTypeInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTypeInfo(data)

    def as_setPlayersS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayers(text)

    def as_setListByTypeS(self, data):
        """
        :param data: Represented by BattleQueueListDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setListByType(data)

    def as_showStartS(self, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_showStart(vis)

    def as_showExitS(self, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_showExit(vis)