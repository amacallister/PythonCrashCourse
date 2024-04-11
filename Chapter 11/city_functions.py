def get_formatted_name(city, country, population=0):
    """
    Accept two parameters: acity name and a country name
    Return a single string of the form City, Country
    """
    if population:
        formatted_str = f"{city}, {country} - Population {population}"
    else:
        formatted_str = f"{city}, {country}"
    return formatted_str.title()