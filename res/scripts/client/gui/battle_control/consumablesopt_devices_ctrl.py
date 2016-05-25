# Embedded file name: scripts/client/gui/battle_control/consumables/opt_devices_ctrl.py
import Event
from PlayerEvents import g_playerEvents
from constants import ARENA_PERIOD
from items import vehicles
import nations
import SoundGroups

class DevicesSound:
    _eventsMap = {6: ('camo_net_start', 'camo_net_stop'),
     4: ('stereo_trumpet_start', 'stereo_trumpet_stop')}
    _enabled = False

    @staticmethod
    def playSound(ID, isOn):
        if DevicesSound._enabled:
            events = DevicesSound._eventsMap.get(ID, None)
            if events is not None:
                SoundGroups.g_instance.playSound2D(events[0 if isOn else 1])
        return


class OptionalDevicesController(object):
    __slots__ = ('__eManager', '__optionalDevices', 'onOptionalDeviceAdded', 'onOptionalDeviceUpdated')

    def __init__(self):
        super(OptionalDevicesController, self).__init__()
        self.__eManager = Event.EventManager()
        self.onOptionalDeviceAdded = Event.Event(self.__eManager)
        self.onOptionalDeviceUpdated = Event.Event(self.__eManager)
        self.__optionalDevices = {}
        g_playerEvents.onArenaPeriodChange += self.__pe_onArenaPeriodChange

    def __repr__(self):
        return 'OptionalDevicesController({0!r:s})'.format(self.__optionalDevices)

    def clear(self, leave = True):
        if leave:
            self.__eManager.clear()
            g_playerEvents.onArenaPeriodChange -= self.__pe_onArenaPeriodChange
        for deviceID in self.__optionalDevices.keys():
            DevicesSound.playSound(deviceID, False)

        self.__optionalDevices.clear()

    def isOptionalDeviceOn(self, deviceID):
        isOn = False
        if deviceID in self.__optionalDevices:
            isOn = self.__optionalDevices[deviceID]
        return isOn

    def isOptionalDeviceOnByCD(self, intCD):
        itemID = vehicles.parseIntCompactDescr(intCD)[-1]
        return self.isOptionalDeviceOn(itemID)

    def getDescriptor(self, deviceID):
        return vehicles.g_cache.optionalDevices()[deviceID]

    def setOptionalDevice(self, deviceID, isOn):
        intCD = vehicles.makeIntCompactDescrByID('optionalDevice', nations.NONE_INDEX, deviceID)
        if deviceID in self.__optionalDevices:
            self.__optionalDevices[deviceID] = isOn
            self.onOptionalDeviceUpdated(intCD, isOn)
        else:
            self.__optionalDevices[deviceID] = isOn
            self.onOptionalDeviceAdded(intCD, self.getDescriptor(deviceID), isOn)
        DevicesSound.playSound(deviceID, isOn)

    def __pe_onArenaPeriodChange(self, period, *args):
        if period == ARENA_PERIOD.AFTERBATTLE:
            self.clear()
        DevicesSound._enabled = period == ARENA_PERIOD.BATTLE


__all__ = ('OptionalDevicesController',)