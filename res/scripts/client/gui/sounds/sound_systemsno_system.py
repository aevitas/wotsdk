# Embedded file name: scripts/client/gui/sounds/sound_systems/no_system.py
from gui.sounds.abstract import SoundSystemAbstract
from gui.sounds.sound_constants import SoundSystems

class NoSoundSystem(SoundSystemAbstract):

    def getID(self):
        return SoundSystems.UNKNOWN