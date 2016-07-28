# Embedded file name: scripts/client/messenger/proto/xmpp/xmpp_string_utils.py
from external_strings_utils import unicode_from_utf8
from messenger.proto.xmpp.errors import ClientContactError, ClientIntLimitError, ClientChannelError
from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT, CONTACT_ERROR_ID, LIMIT_ERROR_ID, CHANNEL_LIMIT, CHANNEL_ERROR_ID
from messenger.proto.xmpp.xmpp_string_grep import ResourcePrep
from messenger.proto.xmpp.xmpp_string_grep import XmppStringPrepError

def validateRosterItemGroup(name):
    if not name:
        return ('', ClientContactError(CONTACT_ERROR_ID.GROUP_EMPTY))
    try:
        name = ResourcePrep.prepare(name)
    except XmppStringPrepError:
        return ('', ClientContactError(CONTACT_ERROR_ID.GROUP_INVALID_NAME, name))

    length = len(name)
    if CONTACT_LIMIT.GROUP_MIN_LENGTH > length or CONTACT_LIMIT.GROUP_MAX_LENGTH < length:
        return (name.encode('utf-8'), ClientIntLimitError(LIMIT_ERROR_ID.GROUP_INVALID_LENGTH, CONTACT_LIMIT.GROUP_MAX_LENGTH, CONTACT_LIMIT.GROUP_MIN_LENGTH))
    else:
        return (name.encode('utf-8'), None)


def validateContactNote(note):
    if not note:
        return ('', ClientContactError(CONTACT_ERROR_ID.NOTE_EMPTY))
    elif len(unicode_from_utf8(note)[0]) not in range(CONTACT_LIMIT.NOTE_MIN_CHARS_COUNT, CONTACT_LIMIT.NOTE_MAX_CHARS_COUNT + 1):
        return (note, ClientIntLimitError(LIMIT_ERROR_ID.NOTE_INVALID_LENGTH, CONTACT_LIMIT.NOTE_MIN_CHARS_COUNT, CONTACT_LIMIT.NOTE_MAX_CHARS_COUNT))
    else:
        return (note, None)


def validateUserRoomName(name):
    if not name:
        return ('', ClientChannelError(CHANNEL_ERROR_ID.NAME_EMPTY))
    try:
        name = ResourcePrep.prepare(name)
    except XmppStringPrepError:
        return ('', ClientChannelError(CHANNEL_ERROR_ID.NAME_INVALID, name))

    length = len(name)
    if CHANNEL_LIMIT.NAME_MIN_CHARS_COUNT > length or CHANNEL_LIMIT.NAME_MAX_CHARS_COUNT < length:
        return (name.encode('utf-8'), ClientIntLimitError(LIMIT_ERROR_ID.CHANNEL_INVALID_LENGTH, CHANNEL_LIMIT.NAME_MAX_CHARS_COUNT, CHANNEL_LIMIT.NAME_MIN_CHARS_COUNT))
    else:
        return (name.encode('utf-8'), None)


def validateUserRoomPwd(password, isRetype = False):
    if not password:
        if isRetype:
            errorID = CHANNEL_ERROR_ID.PASSWORD_EMPTY
        else:
            errorID = CHANNEL_ERROR_ID.RETYPE_EMPTY
        return ('', ClientChannelError(errorID))
    try:
        password = ResourcePrep.prepare(password)
    except XmppStringPrepError:
        if isRetype:
            errorID = CHANNEL_ERROR_ID.PASSWORD_INVALID
        else:
            errorID = CHANNEL_ERROR_ID.RETYPE_INVALID
        return ('', ClientChannelError(errorID))

    length = len(password)
    if CHANNEL_LIMIT.NAME_MIN_CHARS_COUNT > length or CHANNEL_LIMIT.NAME_MAX_CHARS_COUNT < length:
        return ('', ClientIntLimitError(LIMIT_ERROR_ID.CHANNEL_INVALID_LENGTH, CHANNEL_LIMIT.NAME_MAX_CHARS_COUNT, CHANNEL_LIMIT.NAME_MIN_CHARS_COUNT))
    else:
        return (password.encode('utf-8'), None)


def validateUserRoomPwdPair(password, retype):
    password, error = validateUserRoomPwd(password, isRetype=False)
    if error is not None:
        return ('', error)
    retype, error = validateUserRoomPwd(retype, isRetype=True)
    if error is not None:
        return ('', error)
    elif password != retype:
        return ('', ClientChannelError(CHANNEL_ERROR_ID.PASSWORDS_NOT_EQUALS))
    else:
        return (password, None)