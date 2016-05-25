# Embedded file name: scripts/client/gui/sounds/sound_systems/wwise_system.py
import WWISE
import SoundGroups
from debug_utils import LOG_DEBUG
from gui.sounds.abstract import SoundSystemAbstract
from gui.sounds.sound_constants import SoundSystems, HQRenderState

class WWISESoundSystem(SoundSystemAbstract):

    def getID(self):
        return SoundSystems.WWISE

    def isMSR(self):
        return WWISE.WG_isMSR()

    def setHQEnabled(self, isEnabled):
        if isEnabled:
            state = HQRenderState.HQ_FOR_ALL
        else:
            state = HQRenderState.LQ_FOR_ALL
        SoundGroups.g_instance.setLQRenderState(state)

    def enableDynamicPreset(self):
        LOG_DEBUG('ue_set_preset_high_dynamic_range has been set')
        WWISE.WW_setVolumeThreshold(-50)
        self.sendGlobalEvent('ue_set_preset_high_dynamic_range')

    def disableDynamicPreset(self):
        LOG_DEBUG('ue_set_preset_low_dynamic_range has been set')
        WWISE.WW_setVolumeThreshold(-40)
        self.sendGlobalEvent('ue_set_preset_low_dynamic_range')

    def setSoundSystem(self, value):
        LOG_DEBUG('WWISE sound system has been applied: %d' % value)
        WWISE.WW_setSoundSystem(value)

    def sendGlobalEvent(self, eventName, **params):
        WWISE.WW_eventGlobalSync(eventName)