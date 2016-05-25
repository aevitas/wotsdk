# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AbstractRallyViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AbstractRallyViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setPyAliasS(self, alias):
        """
        :param alias:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPyAlias(alias)

    def as_getPyAliasS(self):
        """
        :return String:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getPyAlias()