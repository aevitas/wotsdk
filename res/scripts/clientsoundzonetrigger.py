# Embedded file name: scripts/client/SoundZoneTrigger.py
import BigWorld
import Math

class SoundZoneTrigger(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        import bwpydevd
        bwpydevd.startDebug()
        width = self.Size[0]
        height = self.Size[0]
        position = Math.Vector2(self.position.x, self.position.z) - self.Size
        alpha = self.direction.z

    def destroy(self):
        pass