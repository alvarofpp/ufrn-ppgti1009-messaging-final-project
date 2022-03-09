from typing import Dict


def clean_dict(data: Dict) -> Dict:
    return {key: value for key, value in data.items() if value is not None}
