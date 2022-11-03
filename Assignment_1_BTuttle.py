"""
Weekly Pay Calculator: An employee’s total weekly pay equals the hourly wage multiplied by the total number
of regular hours plus any overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times
the hourly wage.
By Brandon Tuttle
8/23/2022

"""

def main():
    """
    calculate and display weekly pay
    :return: None
    """
    hours, rate = get_hoursworked_and_pay_rate()
    pay = calc_gross_pay(hours, rate)
    print_pay_stub(hours, rate, pay)


def get_hoursworked_and_pay_rate():
    """
    ask user to enter hours worked and hourly pay rate
    :return: hours_worked: float
    :return: hourly_pay_rate: float
    """
    hours_worked = float(input("Enter hours worked: "))
    hourly_pay_rate = float(input("Enter hourly pay rate: $"))
    return hours_worked, hourly_pay_rate


def calc_gross_pay(hours_worked, hourly_pay_rate):
    """

    :param hours_worked: float
    :param hourly_pay_rate: float
    :return: gross_pay: float
    """
    if hours_worked > 40:
        gross_pay =(40 * hourly_pay_rate)+ (hours_worked - 40) * (1.5 * hourly_pay_rate)
    else:
        gross_pay = hours_worked * hourly_pay_rate

    return gross_pay


def print_pay_stub(hours_worked, hourly_pay_rate, gross_pay):
    """

    :param hours_worked: float
    :param hourly_pay_rate: float
    :param gross_pay: float
    :return: None
    """
    print("Hours Worked: " + str(hours_worked))
    print(f"Hourly Pay Rate: ${hourly_pay_rate:.2f}")
    print(f"Gross Pay ${gross_pay:.2f}") # change to accounting format


if __name__=="__main__":
    main()
