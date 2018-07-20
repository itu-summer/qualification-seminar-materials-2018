# Assignment for Session 6

The purpose of this assignment is to generate some statistics about Copenhagen's citizens. On the way you will repeat/learn:

  * How to read Excel files.
  * Create functions in Python.
  * Use `for` loops to iterate over elements of a list.
  * Lookup elements in dictionaries.
  * Use `set`s in Python together with some of their functionality.

We will use two datasets. One `befkbhalderstatkode_small.xlsx`, which contains statistics about Copenhagen's population corresponding to the year 2015. This dataset was created from the data available at [http://data.kk.dk/dataset/befolkningen-efter-ar-bydel-alder-og-statsborgerskab](http://data.kk.dk/dataset/befolkningen-efter-ar-bydel-alder-og-statsborgerskab), where you can also find a more in depth description of the given data.  

The second dataset comes originally from Danmarks Statistik and maps country codes to countries of origin, see [http://www.dst.dk/da/Statistik/dokumentation/Times/forebyggelsesregistret/statkode.aspx](http://www.dst.dk/da/Statistik/dokumentation/Times/forebyggelsesregistret/statkode.aspx).


## Reading Excel Files

  * Inspect the code in the file `read_excel_files.py`.
  * It contains two functions `country_codes_in_kbh_data` and `country_codes_in_stats_data`, which both read two Excel files, `befkbhalderstatkode_small.xlsx` and `country_codes.xlsx` respectively. 
  * Open both `.xlsx` files with one of the programs _Excel_, _OpenOffice_, _GoogleSpreadheets_, etc. to inspect their contents.
  * Set a breakpoint on line `5` in `read_excel_files.py` and use the debugger to step through the execution of this program.
  * Try to understand what is going on by observing the values of variables.

Observe that the program in `read_excel_files.py` is quite unpractical. We read two files via the two functions `country_codes_in_kbh_data` and `country_codes_in_stats_data` respectively. However, the two functions are almost the same. Compare them line by line, i.e., compare line 5 to line 22, line 6 to line 23, line 7 to line 24, ..., and finally line 18 to line 35.

  * On a sheet of paper note down the differences per line.
  * _Reflection:_ How can you reduce code duplication?


## Creating a New Function

Create a function `country_codes_data` in `country_codes_stats.py`, which unifies the two earlier functions `country_codes_in_kbh_data` and `country_codes_in_stats_data` into one and captures variability via two arguments.

That is, the function definition will look something like the following, see file `country_codes_stats.py`:

```python
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
    
    # TODO: Implement me!
    pass
```

## Filtering for Unique Elements and Sorting

Observe that the list of `country_codes`, which is returned from `befkbhalderstatkode_small.xlsx` contains many duplicates. 

  1. Modify the function `country_codes_data(filename, column_number)` so that it returns a list of unique country codes. That is, it does not contain duplicates!
    - _Hint:_ remember a basic Python data structure, which can hold collections of elements, where each element is unique.
  * Modify the function `country_codes_data(filename, column_number)` even further, so that it returns a sorted list of unique country codes.
    - _Hint:_ use the function `sorted` to return a sorted list.
    - _Hint:_ In case you are in doubt, open the interactive Python interpreter with `$ ipython` and read the documentation of the `sorted` function via `sorted?`.


## Dictionary Lookup


Create a new function `translate_code_to_text` in your `country_codes_stats.py` module, which allows you to translate a numerical country code into an explanatory string. For example, the following code should print `'Belgien'`.


```python
descriptive_string = translate_code_to_text(5126)
print(descriptive_string)
```

  - _Hint:_ Obviously, your function gets a single argument for the country code.
  - _Hint:_ Make use of the module `stats_code.py`, which contains a variable with a dictionary `COUNTRY_CODES`. That is, after importing the module, you can lookup the description of a country code via something like the following:
  
  ```python
belgien_code = stat_codes.COUNTRY_CODES['5126']
print(belgien_code)
```
  which should print `'Belgien'`


## Many Dictionary Lookups

Create a new function `translate_many_codes_to_text` in your `country_codes_stats.py` module, which allows you to translate many numerical country codes, i.e., a list of them into a list of explanatory strings.  

That is, the function definition should look similar to the following:

```python
def translate_many_codes_to_text(codes):
    """Translate many country into human-readable strings with the help of the
    `stat_codes` module

    :param codes: list
        A list of numerical country codes.
    :return: list
        A list of strings with human readable country codes.
    """
    
    pass
```


  - _Hint:_ This function should contain a loop, which calls the function `translate_code_to_text`, see assignment "Dictionary Lookup" above, for each element in the list of country codes.
  - _Hint:_ Remember that you can create an empty list, for example, via: `codes_text = []`
  - _Hint:_ You can append a single element to a list with help of the `append` method. For example, the following code will print `['A', 'B', 'C', 'NEW THING']`
  ```python
codes_text = ['A', 'B', 'C']
codes_text.append('NEW THING')
print(codes_text)
```

After implementation call the function `translate_many_codes_to_text` on the data which you get from reading the `befkbhalderstatkode_small.xlsx` file with `country_codes_data`.

That is, something similar to the following:

```print
cph_person_codes = country_codes_data('befkbhalderstatkode_small.xlsx', 3)

print('Persons from the following countries live in Copenhagen:')
print(translate_many_codes_to_text(cph_person_codes))
```

should print something similar to:

```
Persons from the following countries live in Copenhagen:
['Sverige', 'Albanien', 'Belgien', 'Bulgarien', 'Tjekkoslovakiet', 'Frankrig', 'Grækenland', 'Nederlandene', 'Irland', 'Italien', 'Serbien og Montenegro', 'Jugoslavien', 'Malta', 'Polen', 'Portugal', 'Rumænien', 'San Marino', 'Schweiz', 'Sovjetunionen', 'Spanien', 'Storbritannien', 'Tyrkiet', 'Ungarn', 'Tyskland', 'Østrig', 'Rusland', 'Ukraine', 'Hviderusland', 'Armenien', 'Aserbajdsjan', 'Moldova', 'Algeriet', 'Usbekistan', 'Angola', 'Kasakhstan', 'Turkmenistan', 'Botswana', 'Kirgisistan', 'Tadsjikistan', 'Georgien', 'Burundi', 'Etiopien', 'Comorerne', 'Eritrea', 'Gambia', 'Ghana', 'Guinea-Bissau', 'Guinea', 'Kap Verde', 'Kenya', 'Lesotho', 'Liberia', 'Libyen', 'Kroatien', 'Mozambique', 'Slovenien', 'Madagaskar', 'Mali', 'Marokko', 'Mauritius', 'Nigeria', 'Namibia', 'Bosnien-Hercegovina', 'Makedonien', 'Serbien', 'Jugoslavien, Forbundsrepublikken', 'Montenegro', 'Kosovo', 'Sierra Leone', 'Sudan', 'Swaziland', 'Sydafrika', 'Tjekkiet', 'Tanzania', 'Slovakiet', 'Tunesien', 'Uganda', 'Egypten', 'Cameroun', 'Congo, Demokratiske Republik', 'Congo, Republikken', 'Benin', 'Elfenbenskysten', 'Gabon', 'Mauretanien', 'Niger', 'Rwanda', 'Senegal', 'Somalia', 'Tchad', 'Togo', 'Burkina Faso', 'Zimbabwe', 'Zambia', 'Malawi', 'Seychellerne', 'Afrika uoplyst', 'Argentina', 'Bahamas', 'Bolivia', 'Barbados', 'Brasilien', 'Guyana', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominikanske Republik', 'Ecuador', 'Guatemala', 'Grenada', 'Haiti', 'Dominica', 'Skt. Lucia', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'El Salvador', 'Trinidad og Tobago', 'Uruguay', 'USA', 'Venezuela', 'Yemen', 'Forenede Arabiske Emirater', 'Afghanistan', 'Bhutan', 'Bangladesh', 'Brunei', 'Myanmar', 'Cambodja', 'Sri Lanka', 'Cypern', 'Taiwan', 'Indien', 'Indonesien', 'Irak', 'Iran', 'Israel', 'Japan', 'Jordan', 'Kina', 'Kuwait', 'Laos', 'Libanon', 'Maldiverne', 'Malaysia', 'Mongoliet', 'Oman', 'Nepal', 'Nordkorea', 'Pakistan', 'Filippinerne', 'Saudi-Arabien', 'Singapore', 'Sydkorea', 'Syrien', 'Mellemøsten uoplyst', 'Vietnam (2)', 'Land ukendt (1)', 'Thailand', 'Qatar', 'Asien uoplyst', 'Australien', 'Tonga', 'Fiji', 'Uoplyst (2)', 'New Zealand', 'Samoa', 'Djibouti', 'Belize', 'Estland', 'Letland', 'Litauen', 'Danmark', 'Udlandet uoplyst', 'Statsløs', 'Finland', 'Island, ligeret dansk', 'Island', 'Liechtenstein', 'Luxembourg', 'Norge', 'Kongelig']
```

## Filtering Elements from a List which Appear in Another

Next to reporting from which countries Copenhagen's citizens are coming from, we want to know from which countries there is no representative registered in the city.

That is, after reading the country_codes from the Excel files:

```python
cph_person_codes = country_codes_data('befkbhalderstatkode_small.xlsx', 3)
complete_codes = country_codes_data('country_codes.xlsx', 0)
```

you have two variables, where `cph_person_codes` contains a list of country codes from which people are registered in Copenhagen and `complete_codes` is a list of all country code numbers.

Consequently, we would like to find all those numbers that appear in `complete_codes` but not in `cph_person_codes` to find all those country codes for which we have no representative in the city.


Create a function `filter_for_not_living_in_cph`, which takes two lists as arguments and returns a list with elements appearing in the first but not the second. That is,


```python
def filter_for_not_living_in_cph(codes_1, codes_2):
    """Removes all elements from codes_1 which do not appear in codes_2.

    :param codes_1: list
        For example a list of numerical values.
    :param codes_2: list
        For example a list of numerical values.
    :return: list
        A set of elements, which appear in codes_1 but not in codes_2.
    """
```

  * _Hint:_ Either use a `for` loop over `complete_codes` and keep only those elements in a list, which is not in `cph_person_codes`.
  * _Hint:_ Alternatively, read the section on _Set Difference_ here https://www.programiz.com/python-programming/set and see how you can use that for such a filtering task.


------------------------




# A Test Case for Checking your Solution

To check if your implementation (or parts of it) works correctly, you might want to run the test case `test_country_codes_stats.py` against your `country_codes_stats.py` module. You can do so by running it with `pytest` from the command-line.

```bash
$ pytest test_country_codes_stats.py
```