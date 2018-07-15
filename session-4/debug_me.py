def main():
    phone_number = input('Please enter a phone number: ')
    country_code, number = phone_number.split('-')
    if country_code == +45:
        print(f'This is a Danish number {number}.')
    elif country_code == +49:
        print(f'This is a German number {number}.')
    else:
        print(f'I do not know this country code: {country_code}.')


if __name__ == '__main__':
    main()
