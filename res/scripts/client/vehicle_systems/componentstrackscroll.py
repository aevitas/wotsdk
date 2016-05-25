# Embedded file name: scripts/client/vehicle_systems/components/TrackScroll.py


class TrackScrollingFilter(object):

    def __init__(self):
        self.__value = 0.0
        self.__inputValue = 0.0
        self.__Tin = 0.1
        self.__Tout = 0.05

    def setScroll(self, scroll):
        self.__inputValue = scroll

    def output(self):
        return self.__value

    def update(self, speed, dt):
        scrollDelta = self.__calcScrollDelta(speed)
        self.__value += (scrollDelta - self.__value) * (dt / self.__Tout)
        self.__inputValue += -self.__inputValue * (dt / self.__Tin)

    def __calcScrollDelta(self, vehicleSpeed):
        scrollDelta = 0.0
        scroll = self.__inputValue
        if abs(scroll) > 0.1:
            if abs(vehicleSpeed) < 0.1:
                scrollDelta = scroll
            else:
                scrollDelta = scroll - vehicleSpeed
                if scroll * vehicleSpeed > 0.0:
                    if scrollDelta * scroll < 0.0:
                        scrollDelta = 0.0
        return scrollDelta


class TrackScrollController(object):
    leftContact = property(lambda self: self.__leftContact)
    rightContact = property(lambda self: self.__rightContact)
    leftScroll = property(lambda self: self.__leftScrollFilter.output())
    rightScroll = property(lambda self: self.__rightScrollFilter.output())

    def __init__(self, appearance):
        self.__left = 0.0
        self.__right = 0.0
        self.__leftContact = False
        self.__rightContact = False
        self.__appearance = appearance
        self.__vehicle = None
        self.__externalData = False
        self.__leftScrollFilter = TrackScrollingFilter()
        self.__rightScrollFilter = TrackScrollingFilter()
        return

    def destroy(self):
        self.__appearance = None
        self.__vehicle = None
        self.__leftScrollFilter = None
        self.__rightScrollFilter = None
        return

    def setVehicle(self, vehicle):
        self.__vehicle = vehicle

    def updateExtScroll(self, left, right):
        self.__externalData = True
        self.__left = left
        self.__right = right
        self.__leftScrollFilter.setScroll(left)
        self.__rightScrollFilter.setScroll(right)

    def simulate(self, dt):
        if self.__vehicle is not None:
            vehicleSpeed = self.__vehicle.filter.speedInfo.value[2]
            self.__leftScrollFilter.update(vehicleSpeed, dt)
            self.__rightScrollFilter.update(vehicleSpeed, dt)
            updateInfo = [0.0,
             False,
             0.0,
             False]
            if self.__vehicle.filter.placingOnGround:
                self.__leftContact = self.__vehicle.filter.numLeftTrackContacts > 0
                self.__rightContact = self.__vehicle.filter.numRightTrackContacts > 0
            else:
                self.__leftContact = not self.__appearance.fashion.isFlyingLeft
                self.__rightContact = not self.__appearance.fashion.isFlyingRight
            if self.__appearance.engineMode[0] > 1:
                if not self.__externalData:
                    if not self.__leftContact:
                        updateInfo[0] = 4.0 if self.__appearance.engineMode[1] == 1 else -4.0
                        updateInfo[1] = True
                    if not self.__rightContact:
                        updateInfo[2] = 4.0 if self.__appearance.engineMode[1] == 1 else -4.0
                        updateInfo[3] = True
                else:
                    updateInfo = [self.__left,
                     True,
                     self.__right,
                     True]
            else:
                updateInfo[1] = True
                updateInfo[3] = True
        self.__vehicle.filter.setTracksSpeed(updateInfo[0], updateInfo[1], updateInfo[2], updateInfo[3])
        return