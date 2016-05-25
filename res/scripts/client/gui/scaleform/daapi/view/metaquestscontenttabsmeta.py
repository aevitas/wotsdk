# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsContentTabsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsContentTabsMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onSelectTab(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('onSelectTab')

    def as_selectTabS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_selectTab(index)

    def as_setTabsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTabs(data)