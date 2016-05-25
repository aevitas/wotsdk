# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortRoomMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class FortRoomMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    null
    """

    def showChangeDivisionWindow(self):
        """
        :return :
        """
        self._printOverrideError('showChangeDivisionWindow')

    def as_showLegionariesCountS(self, isShow, msg, tooltip):
        """
        :param isShow:
        :param msg:
        :param tooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showLegionariesCount(isShow, msg, tooltip)

    def as_showLegionariesToolTipS(self, isShow):
        """
        :param isShow:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showLegionariesToolTip(isShow)

    def as_showOrdersBgS(self, isShow):
        """
        :param isShow:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showOrdersBg(isShow)

    def as_setChangeDivisionButtonEnabledS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setChangeDivisionButtonEnabled(value)