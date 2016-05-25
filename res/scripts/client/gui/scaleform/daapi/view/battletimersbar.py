# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/TimersBar.py
from SoundGroups import g_instance as _g_sound
from debug_utils import LOG_DEBUG
from helpers.i18n import makeString as _ms
from gui.battle_control import arena_info
from gui.battle_control.battle_constants import COUNTDOWN_STATE
from gui.battle_control.battle_period_ctrl import ITimersBar

class _SOUNDS:
    BATTLE_ENDING_SOON = 'time_buzzer_02'
    COUNTDOWN_TICKING = 'time_countdown'
    BATTLE_END = 'time_over'
    STOP_TICKING = 'time_countdown_stop'


_BATTLE_END_SOUND_TIME = 2
_STATE_TO_MESSAGE = {COUNTDOWN_STATE.WAIT: _ms('#ingame_gui:timer/waiting'),
 COUNTDOWN_STATE.START: _ms('#ingame_gui:timer/starting'),
 COUNTDOWN_STATE.STOP: _ms('#ingame_gui:timer/started')}

class TimersBar(ITimersBar):

    def __init__(self, ui = None, isEvent = False):
        super(TimersBar, self).__init__()
        arenaType = arena_info.getArenaType()
        self.__ui = ui
        self.__isTicking = False
        self.__state = COUNTDOWN_STATE.STOP
        self.__roundLength = arenaType.roundLength
        self.__endingSoonTime = arenaType.battleEndingSoonTime
        self.__endWarningIsEnabled = self.__checkEndWarningStatus()
        if isEvent or self.__endWarningIsEnabled:
            timerPath = 'eventBattleTimer.swf'
            _g_sound.playSound2D(_SOUNDS.STOP_TICKING)
        else:
            timerPath = 'BattleTimer.swf'
        self.__ui.movie.loadTimer(timerPath)

    def __del__(self):
        LOG_DEBUG('TimersBar is deleted')

    def destroy(self):
        self.__ui = None
        return

    def setTotalTime(self, level, totalTime):
        minutes, seconds = divmod(int(totalTime), 60)
        if self.__endWarningIsEnabled and self.__state == COUNTDOWN_STATE.STOP:
            if _BATTLE_END_SOUND_TIME < totalTime <= self.__endingSoonTime:
                if not self.__isTicking:
                    _g_sound.playSound2D(_SOUNDS.COUNTDOWN_TICKING)
                    self.__isTicking = True
                if totalTime == self.__endingSoonTime:
                    _g_sound.playSound2D(_SOUNDS.BATTLE_ENDING_SOON)
            elif self.__isTicking:
                _g_sound.playSound2D(_SOUNDS.STOP_TICKING)
            if totalTime == _BATTLE_END_SOUND_TIME and self.__isTicking:
                _g_sound.playSound2D(_SOUNDS.BATTLE_END)
                self.__isTicking = False
        self.__call('timerBar.setTotalTime', [level, '{:02d}'.format(minutes), '{:02d}'.format(seconds)])

    def hideTotalTime(self):
        self.__call('showBattleTimer', [False])

    def setCountdown(self, state, _, timeLeft):
        self.__state = state
        self.__call('timerBig.setTimer', [_STATE_TO_MESSAGE[state], timeLeft])

    def hideCountdown(self, state, speed):
        self.__state = state
        self.__call('timerBig.setTimer', [_STATE_TO_MESSAGE[state]])
        self.__call('timerBig.hide', [speed])

    def setWinConditionText(self, text):
        pass

    def __call(self, funcName, args = None):
        if self.__ui:
            self.__ui.call('battle.{0}'.format(funcName), args)

    def __validateEndingSoonTime(self):
        return self.__endingSoonTime > 0 and self.__endingSoonTime < self.__roundLength

    def __checkEndWarningStatus(self):
        endingSoonTimeIsValid = self.__validateEndingSoonTime()
        return arena_info.battleEndWarningEnabled() and endingSoonTimeIsValid