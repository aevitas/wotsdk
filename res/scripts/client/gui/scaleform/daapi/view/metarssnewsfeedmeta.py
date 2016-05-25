# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RssNewsFeedMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RssNewsFeedMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def openBrowser(self, linkToOpen):
        """
        :param linkToOpen:
        :return :
        """
        self._printOverrideError('openBrowser')

    def as_updateFeedS(self, feed):
        """
        :param feed:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFeed(feed)