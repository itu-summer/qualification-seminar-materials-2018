import stat_codes
import openpyxl


def country_codes_data(filename, column_number):
    """Read country code data from a given Excel file,
    in which entire columns contain country codes and
    the first row is a header row without values.

    :param filename: str
        Path to the Excel (.xslx) file containing a row
        with country codes
    :param column_number: int
        The index number of the column containing the
        country codes.
    :return: list
        A list of country code numbers.
    """
    wb = openpyxl.load_workbook(filename)
    sheet = wb.get_sheet_by_name("Sheet1")
    
    list_of_columns = list(sheet.columns)
    column_of_interest = list_of_columns[column_number]
    cells_of_interest = column_of_interest[1:]

    country_codes = []

    for cell_object in cells_of_interest:
        country_codes.append(cell_object.value)

    country_codes_unique = set(country_codes)
    country_codes_sorted = sorted(country_codes_unique)
    return country_codes_sorted


def translate_code_to_text(code):
    stat_code_text = stat_codes.COUNTRY_CODES[str(code)]
    return stat_code_text


def translate_many_codes_to_text(codes):
    """Translate many country into human-readable strings with the help of the
    `stat_codes` module

    :param codes: list
        A list of numerical country codes.
    :return: list
        A list of strings with human readable country codes.
    """
    codes_text = []

    for code in codes:
        stat_code_text = translate_code_to_text(str(code))
        codes_text.append(stat_code_text)

    return codes_text


def filter_for_not_living_in_cph(codes_1, codes_2):
    """Removes all elements from codes_1 which do not appear in codes_2.

    :param codes_1: list
        For example a list of numerical values.
    :param codes_2: list
        For example a list of numerical values.
    :return: set
        A set of elements, which appear in codes_1 but not in codes_2.
    """
    codes_1 = set(codes_1)
    codes_2 = set(codes_2)
    # See documentation on set difference here:
    # https://www.programiz.com/python-programming/set
    return codes_1.difference(codes_2)


def filter_for_not_living_in_cph_alternative(codes_1, codes_2):
    # An alternative implementation for the set difference is as in the 
    # following:
    filtered_codes = []
    for element in codes_1:
        if not element in codes_2:
            filtered_codes.append(element)

    return filtered_codes


def main():
    cph_person_codes = country_codes_data('befkbhalderstatkode_small.xlsx', 3)
    complete_codes = country_codes_data('country_codes.xlsx', 0)
    cph_person_codes = set(cph_person_codes)
    complete_codes = set(complete_codes)

    print('-----------------')
    print('Persons from the following countries live in Copenhagen:')
    print(translate_many_codes_to_text(cph_person_codes))

    not_living_in_cph = filter_for_not_living_in_cph(complete_codes,
                                                     cph_person_codes)

    print('-----------------')
    print('Persons from the following countries do not live in Copenhagen:')
    print(translate_many_codes_to_text(not_living_in_cph))


if __name__ == "__main__":
    main()
