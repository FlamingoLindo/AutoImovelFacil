"""
This module generates random credit card details, specifically for Mastercard,
using the Faker library. The details returned include the card name, the cardholder's name,
the card number, expiration date, and CVV.
"""

from faker import Faker

fake = Faker('pt_BR')


def create_card():
    """
    Generates a random Mastercard credit card with full details.

    The function uses the Faker library to generate a Mastercard credit card's
    full details, including:
    - Card type (Mastercard)
    - Cardholder's name
    - Card number
    - Expiration date
    - CVV (Card Verification Value)

    Returns:
        tuple: A tuple containing the following details:
            - str: Card type (always "Mastercard")
            - str: Cardholder's name
            - str: Card number
            - str: Expiration date (in MM/YY format)
            - str: CVV number
    """
    while True:
        card = fake.credit_card_full()
        lines = card.splitlines()

        if lines[0] == 'Mastercard':
            master_card = lines[0]
            nome = lines[1]
            codigo, exp = lines[2].split(' ', 1)
            cvv = lines[3].split('CVV: ')[1].strip()

            return master_card, nome, codigo, exp, cvv
