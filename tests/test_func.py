from utils.func import get_executed_operations,get_operation_date, hiden_card_number

def test_get_executed_operations():
    assert get_executed_operations([{"id": 422035015, "state": "EXECUTED"}]) ==[{"id": 422035015, "state": "EXECUTED"}]
    assert get_executed_operations([{"id": 422035015, "state": "CANCELED"}]) ==[]


def test_get_operation_date():
    operation1 = {"date": "2023-05-20"}
    operation2 = {"date": "2023-05-22"}
    operation3 = {"date": "2023-05-21"}

    assert get_operation_date(operation1) == "2023-05-20"
    assert get_operation_date(operation2) == "2023-05-22"
    assert get_operation_date(operation3) == "2023-05-21"


def test_hiden_card_number():
    card_number1 = " "
    card_number2 = "MasterCard 9876543210987654"
    card_number3 = "Счет 11112222333344445555"

    assert hiden_card_number(card_number1) == " "
    assert hiden_card_number(card_number2) == "MasterCard 9876 54** **** 7654"
    assert hiden_card_number(card_number3) == "Счет **5555"
