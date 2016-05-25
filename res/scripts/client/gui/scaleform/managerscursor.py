# Embedded file name: scripts/client/gui/Scaleform/managers/Cursor.py
import GUI
import BigWorld
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui import GUI_CTRL_MODE_FLAG as _CTRL_FLAG
from gui.Scaleform.daapi.view.meta.CursorMeta import CursorMeta
from gui.Scaleform.framework.entities.View import View
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import GameEvent

class Cursor(CursorMeta, View):
    ARROW = 'arrow'
    AUTO = 'auto'
    BUTTON = 'button'
    HAND = 'hand'
    IBEAM = 'ibeam'
    ROTATE = 'rotate'
    RESIZE = 'resize'
    MOVE = 'move'
    DRAG_OPEN = 'dragopen'
    DRAG_CLOSE = 'dragclose'
    __DAAPI_ERROR = 'flashObject is Python Cursor class can`t be None!'

    def __init__(self):
        super(Cursor, self).__init__()
        self.__isActivated = False
        self.__savedMCursorPos = None
        return

    def attachCursor(self, flags = _CTRL_FLAG.GUI_ENABLED):
        if not flags & _CTRL_FLAG.CURSOR_ATTACHED:
            raise AssertionError('Flag CURSOR_ATTACHED is not defined')
            if flags & _CTRL_FLAG.CURSOR_VISIBLE > 0:
                self.show()
            else:
                self.hide()
            mcursor = self.__isActivated or GUI.mcursor()
            mcursor.visible = False
            LOG_DEBUG('Cursor is attached')
            BigWorld.setCursor(mcursor)
            self.__isActivated = True

    def detachCursor(self):
        if self.__isActivated:
            LOG_DEBUG('Cursor is detached')
            BigWorld.setCursor(None)
            self.__isActivated = False
        self.hide()
        return

    def syncCursor(self, flags = _CTRL_FLAG.GUI_ENABLED):
        if flags & _CTRL_FLAG.CURSOR_ATTACHED > 0:
            self.attachCursor(flags=flags)
        elif flags & _CTRL_FLAG.CURSOR_DETACHED > 0:
            self.detachCursor()

    def show(self):
        if self.flashObject is not None:
            self.__setSFMousePosition()
            self.flashObject.visible = True
            self.fireEvent(GameEvent(GameEvent.SHOW_CURSOR), scope=EVENT_BUS_SCOPE.GLOBAL)
        else:
            LOG_ERROR(self.__DAAPI_ERROR)
        return

    def hide(self):
        self.__restoreDeviceMousePosition()
        if self.flashObject is not None:
            self.flashObject.visible = False
            self.fireEvent(GameEvent(GameEvent.HIDE_CURSOR), scope=EVENT_BUS_SCOPE.GLOBAL)
        else:
            LOG_ERROR(self.__DAAPI_ERROR)
        return

    def setCursorForced(self, cursor):
        self.as_setCursorS(cursor)

    def _populate(self):
        super(Cursor, self)._populate()
        flags = self.app.ctrlModeFlags
        if flags & _CTRL_FLAG.CURSOR_ATTACHED > 0:
            self.attachCursor(flags=flags)
        else:
            self.detachCursor()

    def __setSFMousePosition(self):
        screenWidth, screenHeight = GUI.screenResolution()
        mouseLeft, mouseTop = GUI.mcursor().position
        self.__savedMCursorPos = (mouseLeft, mouseTop)
        self.flashObject.x = round((1.0 + mouseLeft) / 2.0 * screenWidth)
        self.flashObject.y = round(-(-1.0 + mouseTop) / 2.0 * screenHeight)

    def __restoreDeviceMousePosition(self):
        if self.__savedMCursorPos is not None:
            GUI.mcursor().position = self.__savedMCursorPos
            self.__savedMCursorPos = None
        return