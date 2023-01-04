# First party
from abstracts.validators import APIValidator


class TempModelValidator:
    """TempModelValidator."""

    def validate_apartment_number(self, number: int) -> None:
        if number == 13:
            raise APIValidator(
                f'This apartment number is invalid: {number}',
                'error',
                '400'
            )

    def validate_firstname(self, firstname: str) -> None:
        if not firstname[0].islower():
            raise APIValidator(
                'The name is invalid (first lowercase letter)',
                'error',
                '400'
            )
