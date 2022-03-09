from typing import List

from app.http.requests import BaseRequest
from pydantic import Field, validator


class StoreRequest(BaseRequest):
    name: str = Field(
        None,
        title='The name of your team',
        max_length=50,
    )
    pokemon_ids: List[int] = Field(
        None,
        title='A list with the identifiers of the pokemons chosen for your team',
        max_items=6,
        min_items=1,
    )

    @validator('name')
    def name_must_be_at_least_five_chars(cls, value: str) -> str:
        len_name = len(value)

        if len_name < 5:
            raise ValueError('The team name must be at least 5 characters long')

        return value

    @validator('pokemon_ids')
    def amount_of_pokemons(cls, value: List[int]) -> List[int]:
        len_pokemons = len(value)

        if len_pokemons == 0:
            raise ValueError('A team must have at least one pokemon')
        if len(value) > 6:
            raise ValueError('A team can have a maximum of 6 pokemons')

        return value

    class Config:
        schema_extra = {
            'example': {
                'name': 'Meliuz team',
                'pokemon_ids': [1, 2, 3, 4, 5, 6],
            },
        }
