# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AbstractRallyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class AbstractRallyWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def canGoBack(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canGoBack')

    def onBrowseRallies(self):
        """
        :return :
        """
        self._printOverrideError('onBrowseRallies')

    def onBrowseStaticsRallies(self):
        """
        :return :
        """
        self._printOverrideError('onBrowseStaticsRallies')

    def onCreateRally(self):
        """
        :return :
        """
        self._printOverrideError('onCreateRally')

    def onJoinRally(self, rallyId, slotIndex, peripheryId):
        """
        :param rallyId:
        :param slotIndex:
        :param peripheryId:
        :return :
        """
        self._printOverrideError('onJoinRally')

    def as_loadViewS(self, flashAlias, pyAlias):
        """
        :param flashAlias:
        :param pyAlias:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(flashAlias, pyAlias)

    def as_enableWndCloseBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableWndCloseBtn(value)