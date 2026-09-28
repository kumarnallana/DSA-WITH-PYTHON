first = {"name": "Sasi", "age": 21}
second = {"age": 22, "city": "Hyderabad", "role": "software Developer"}


def merge_dicts(first: dict, second: dict) -> dict:

    combined_dict: dict[str, int | str] = {
        **first,
        **second,
    }

    return combined_dict


print(merge_dicts(first, second))
