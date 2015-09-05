# Embedded file name: scripts/client/FMOD.py
enabled = True
try:
    from _FMOD import *
except ImportError:
    print 'WARNING: FMOD support is not enabled.'
    from _FMODStubs import *
    enabled = False

if enabled:
    import BigWorld
    BigWorld.getSound = getSound
    BigWorld.getSoundBanks = getSoundBanks
    BigWorld.playSound = playSound
    BigWorld.setDefaultSoundProject = setDefaultSoundProject
    BigWorld.loadSoundBankIntoMemory = loadSoundBankIntoMemory
    BigWorld.loadSoundBank = loadEventProject
    BigWorld.loadSoundGroup = loadSoundGroup
    BigWorld.reloadSoundBank = reloadEventProject
    BigWorld.unloadSoundBankFromMemory = unloadSoundBankFromMemory
    BigWorld.unloadSoundBank = unloadEventProject
    BigWorld.unloadSoundGroup = unloadSoundGroup
    BigWorld.setMasterVolume = setMasterVolume
    del BigWorld