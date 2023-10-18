print("더치페이 계산기를 실행합니다.")
bill_amount = float(input("영수증에 나온 총 금액을 입력해주세요.:\n₩ "))
while bill_amount < 0:
    bill_amount = float(input("{!} Please input correct bill amount:\n₩ "))
print("Bill amount ₩", f"{bill_amount} confirmed.")

num_people = float(input("Please input how many people will pay for the bill:\n"))
while num_people < 0 or (num_people % 1) > 0 or num_people == 0:
    if (num_people % 1) > 0:
        num_people = float(
            input(
                "{!} The number of people can not have a decimal point or comma.\nPlease input correct number of people to split the bill:\n$ "
            )
        )
    elif num_people < 0 or num_people == 0:
        num_people = float(
            input("{!} Please input correct number of people to split the bill:\n$ ")
        )

print(int(num_people), "people split. Confirmed.")


tip = float(input("How many tip would you like to give?\n(%) "))
while tip < 0:
    tip = input("Please input valid percentage\n(%) ")
print(f"{tip}% of tip. Confirmed.")

calculation = round(((bill_amount + (bill_amount * tip / 100)) / num_people), 1)
print(f"Each person's portion is:\n$ {calculation}")

