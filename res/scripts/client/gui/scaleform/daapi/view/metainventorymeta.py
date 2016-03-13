# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/InventoryMeta.py
from gui.Scaleform.daapi.view.lobby.store.StoreComponent import StoreComponent

class InventoryMeta(StoreComponent):

    def sellItem(self, data):
        self._printOverrideError('sellItem')