# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationMainViewMeta.py
from gui.Scaleform.framework.entities.View import View

class CustomizationMainViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def showBuyWindow(self):
        self._printOverrideError('showBuyWindow')

    def closeWindow(self):
        self._printOverrideError('closeWindow')

    def installCustomizationElement(self, id):
        self._printOverrideError('installCustomizationElement')

    def goToTask(self, id):
        self._printOverrideError('goToTask')

    def removeFromShoppingBasket(self, slotId, groupId, id):
        self._printOverrideError('removeFromShoppingBasket')

    def changeCarouselFilter(self):
        self._printOverrideError('changeCarouselFilter')

    def setDurationType(self, id):
        self._printOverrideError('setDurationType')

    def showPurchased(self, value):
        self._printOverrideError('showPurchased')

    def removeSlot(self, groupId, id):
        self._printOverrideError('removeSlot')

    def revertSlot(self, groupId, id):
        self._printOverrideError('revertSlot')

    def showGroup(self, groupId, id):
        self._printOverrideError('showGroup')

    def backToSelectorGroup(self):
        self._printOverrideError('backToSelectorGroup')

    def as_showBuyingPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showBuyingPanel()

    def as_hideBuyingPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBuyingPanel()

    def as_setHeaderDataS(self, data):
        """
        :param data: Represented by CustomizationHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)

    def as_setBonusPanelDataS(self, data):
        """
        :param data: Represented by CustomizationTotalBonusPanelVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBonusPanelData(data)

    def as_setCarouselDataS(self, data):
        """
        :param data: Represented by CarouselDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselData(data)

    def as_setCarouselInitS(self, data):
        """
        :param data: Represented by CarouselInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselInit(data)

    def as_setCarouselFilterDataS(self, data):
        """
        :param data: Represented by CustomizationCarouselFilterVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilterData(data)

    def as_setBottomPanelHeaderS(self, data):
        """
        :param data: Represented by BottomPanelVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelHeader(data)

    def as_setSlotsPanelDataS(self, data):
        """
        :param data: Represented by CustomizationSlotsPanelVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSlotsPanelData(data)

    def as_showSelectorItemS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectorItem(id)

    def as_showSelectorGroupS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectorGroup()

    def as_updateSlotS(self, data):
        """
        :param data: Represented by CustomizationSlotUpdateVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateSlot(data)

    def as_setBottomPanelInitDataS(self, data):
        """
        :param data: Represented by CustomizationBottomPanelInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelInitData(data)