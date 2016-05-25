# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehiclePreview/ModulesPanel.py
from debug_utils import LOG_ERROR
from CurrentVehicle import g_currentPreviewVehicle
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.daapi.view.meta.ModulesPanelMeta import ModulesPanelMeta
from gui.shared.gui_items import GUI_ITEM_TYPE_INDICES, GUI_ITEM_TYPE_NAMES
from gui.shared.utils import EXTRA_MODULE_INFO, CLIP_ICON_PATH
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.shared import g_itemsCache
from items import ITEM_TYPE_NAMES, ITEM_TYPES
from gui.shared import event_dispatcher as shared_events
_MODULE_SLOTS = (GUI_ITEM_TYPE_NAMES[ITEM_TYPES.vehicleChassis],
 GUI_ITEM_TYPE_NAMES[ITEM_TYPES.vehicleTurret],
 GUI_ITEM_TYPE_NAMES[ITEM_TYPES.vehicleGun],
 GUI_ITEM_TYPE_NAMES[ITEM_TYPES.vehicleEngine],
 GUI_ITEM_TYPE_NAMES[ITEM_TYPES.vehicleRadio])

class ModulesPanel(ModulesPanelMeta):

    def _populate(self):
        super(ModulesPanel, self)._populate()
        g_currentPreviewVehicle.onComponentInstalled += self.update
        g_currentPreviewVehicle.onChanged += self.update
        self.update()

    def _dispose(self):
        g_currentPreviewVehicle.onComponentInstalled -= self.update
        g_currentPreviewVehicle.onChanged -= self.update
        super(ModulesPanel, self)._dispose()

    def update(self, *args):
        self._update()

    def showModuleInfo(self, moduleId):
        if moduleId is None:
            return LOG_ERROR('There is error while attempting to show module info window: ', moduleId)
        else:
            shared_events.showModuleInfo(moduleId, g_currentPreviewVehicle.item.descriptor)
            return

    def setVehicleModule(self, newId, slotIdx, oldId, isRemove):
        g_currentPreviewVehicle.installComponent(int(newId))

    def _update(self):
        if g_currentPreviewVehicle.isPresent():
            self.as_setModulesEnabledS(True)
            vehicle = g_currentPreviewVehicle.item
            self.as_setVehicleHasTurretS(vehicle.hasTurrets)
            devices = []
            itemsGetter = g_itemsCache.items.getItems
            for slotType in _MODULE_SLOTS:
                if slotType == ITEM_TYPE_NAMES[ITEM_TYPES.vehicleTurret] and not vehicle.hasTurrets:
                    tooltipType = ''
                else:
                    tooltipType = TOOLTIPS_CONSTANTS.PREVIEW_MODULE
                data = itemsGetter(GUI_ITEM_TYPE_INDICES[slotType], REQ_CRITERIA.VEHICLE.SUITABLE([vehicle], [GUI_ITEM_TYPE_INDICES[slotType]])).values()
                data.sort(reverse=True)
                dataProvider = []
                selectedIndex = -1
                for idx, module in enumerate(data):
                    isFit, installReason = module.mayInstall(vehicle)
                    target = _getPreviewModuleTarget(module, vehicle)
                    isSelected = target == FITTING_TYPES.TARGET_CURRENT
                    if isSelected:
                        selectedIndex = idx
                    moduleData = {'id': module.intCD,
                     'type': slotType,
                     'name': module.userName,
                     'desc': module.getShortInfo(),
                     'target': target,
                     'moduleLabel': module.getGUIEmblemID(),
                     'icon': module.level,
                     'showPrice': False,
                     'removable': True,
                     'isSelected': isSelected,
                     'status': _getStatus(installReason),
                     'disabled': not isFit,
                     'tooltipType': tooltipType}
                    if slotType == ITEM_TYPE_NAMES[ITEM_TYPES.vehicleGun]:
                        if module.isClipGun(vehicle.descriptor):
                            moduleData[EXTRA_MODULE_INFO] = CLIP_ICON_PATH
                    dataProvider.append(moduleData)

                _addDevice(devices, dataProvider, slotType, selectedIndex, tooltipType)

            self.as_setDataS({'devices': devices})


def _getPreviewModuleTarget(module, vehicle):
    if module.getTarget(vehicle) == FITTING_TYPES.TARGET_CURRENT:
        return FITTING_TYPES.TARGET_CURRENT
    return FITTING_TYPES.TARGET_OTHER


def _addDevice(seq, dp, slotType, selectedIndex, tooltipType):
    seq.append({'slotType': slotType,
     'slotIndex': 0,
     'selectedIndex': selectedIndex,
     'availableDevices': dp,
     'tooltipType': tooltipType})


def _getStatus(reason):
    if reason is not None:
        return '#menu:moduleFits/' + reason.replace(' ', '_')
    else:
        return ''