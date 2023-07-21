"""Reformat objects module."""

from uuid import UUID


def get_uuid_from_string(uuid: str) -> UUID | None:
    """Get UUID object from string.

    Parameters:
        uuid: string uuid

    Returns:
        UUID object or None if format error
    """
    try:
        return UUID(uuid)
    except ValueError:
        return None


def get_user_numbers_path(numbers, filename: str) -> str:
    """Get path to user numbers folder.

    Parameters:
        numbers: numbers object
        filename: filename

    Returns:
        Path to folder
    """
    username = numbers.user.username
    return f'{username}/numbers/{filename}'


def get_user_audio_path(audio, filename: str) -> str:
    """Get path to user audio folder.

    Parameters:
        audio: audio object
        filename: filename

    Returns:
        Path to folder
    """
    username = audio.user.username
    return f'{username}/audio/{filename}'
