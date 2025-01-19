#New project
def describe_city(city, country='Uae'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Abudhabi')
describe_city('reykjavik', 'iceland')
describe_city('Al ain')