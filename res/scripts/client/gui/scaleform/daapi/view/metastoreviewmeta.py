# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreViewMeta.py
from gui.Scaleform.framework.entities.View import View

class StoreViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def onClose(self):
        """
        :return :
        """
        self._printOverrideError('onClose')

    def onTabChange(self, tabId):
        """
        :param tabId:
        :return :
        """
        self._printOverrideError('onTabChange')

    def as_showStorePageS(self, viewAlias):
        """
        :param viewAlias:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showStorePage(viewAlias)

    def as_initS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)