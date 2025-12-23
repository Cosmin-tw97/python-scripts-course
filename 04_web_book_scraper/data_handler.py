import csv


def save_to_csv(data: list, filename: str) -> None:
    """
    Saves a list of dictionaries into a CSV file.
    :param data: The list of dictionaries.
    :param filename: The name of the file to save to.
    :return: None
    """
    if not data:
        return

    headers = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Successfully saved {len(data)} items to {filename}")