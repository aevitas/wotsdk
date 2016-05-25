# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCustomizationMeta.py
from gui.Scaleform.framework.entities.View import View

class VehicleCustomizationMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def dropCurrentItemInSection(self, section, kind):
        """
        :param section:
        :param kind:
        :return :
        """
        self._printOverrideError('dropCurrentItemInSection')

    def applyCustomization(self, sections):
        """
        :param sections:
        :return :
        """
        self._printOverrideError('applyCustomization')

    def setNewItemId(self, section, itemId, kind, packageIdx):
        """
        :param section:
        :param itemId:
        :param kind:
        :param packageIdx:
        :return :
        """
        self._printOverrideError('setNewItemId')

    def getCurrentItem(self, section):
        """
        :param section:
        :return Object:
        """
        self._printOverrideError('getCurrentItem')

    def getItemCost(self, section, itemId, priceIndex):
        """
        :param section:
        :param itemId:
        :param priceIndex:
        :return Object:
        """
        self._printOverrideError('getItemCost')

    def closeWindow(self):
        """
        :return :
        """
        self._printOverrideError('closeWindow')

    def as_onServerResponsesReceivedS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onServerResponsesReceived()

    def as_onInitS(self, sections):
        """
        :param sections:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onInit(sections)

    def as_setActionsLockedS(self, locked):
        """
        :param locked:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setActionsLocked(locked)

    def as_onChangeSuccessS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onChangeSuccess()

    def as_onCurrentChangedS(self, section):
        """
        :param section:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onCurrentChanged(section)

    def as_onDropSuccessS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onDropSuccess()

    def as_onResetNewItemS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onResetNewItem()

    def as_setCreditsS(self, credits):
        """
        :param credits:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(credits)

    def as_setGoldS(self, gold):
        """
        :param gold:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(gold)

    def as_refreshDataS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_refreshData()

    def as_refreshItemsDataS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_refreshItemsData()