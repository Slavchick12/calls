"""Calls functions."""

from phones.models import Audio, Connection, Numbers
from phones.utils.functions.files import get_phone_numbers
from pyVoIP import SIP
from pyVoIP.VoIP import VoIPPhone

from calls.logging.logger import logger

PARAMS_NONE = 'Connection or files are not exists.'


def make_calls(connection: Connection, numbers_file: Numbers, audio_file: Audio) -> None:
    """Make calls with the specified parameters.

    Parameters:
        connection: parameters for create phone connection
        numbers_file: file with phone numbers list
        audio_file: audio file to play

    Raises:
        ValueError: if one or more parameters is None
    """
    logger.error(PARAMS_NONE)
    if not connection or not numbers_file or not audio_file:
        logger.error(PARAMS_NONE)
        raise ValueError(PARAMS_NONE)

    phone = VoIPPhone(
        server=connection.server,
        port=connection.port,
        username=connection.username,
        password=connection.password,
        myIP=connection.local_ip,
    )
    numbers = get_phone_numbers(numbers_file)

    try:
        phone.start()
    except SIP.InvalidAccountInfoError as account_error:
        logger.error(f'Connection error: {account_error}')

    for number in numbers:
        try:
            call = phone.call(number)
        except SIP.SIPParseError as parse_error:
            logger.error(f'Couldn t call the number: {number}. {parse_error}')
            continue

        # play_audio(audio_file.audio_file.name)  # function to play audio file
        call.hangup()

    phone.stop()
