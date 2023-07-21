"""Get data from files."""

from phones.models import Numbers


def get_phone_numbers(numbers_file: Numbers) -> list:
    """Get phone numbers from file.

    Parameters:
        numbers_file: file with phone numbers

    Returns:
        List of phone numbers
    """
    filename = numbers_file.numbers_file.name

    with open(f'calls/media/{filename}', 'r') as txt:  # Hardcode
        return txt.read().split(', ')  # If the format in file meets the requirements: [<num1>, <num2>, ..., <numN>]
