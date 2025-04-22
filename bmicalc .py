def bmi_calc(weight, height):
    return weight / height ** 2

def health_stat():
    if bmi < 18.5:
        return "Underweight, too low"
    elif bmi < 18.5 <= 24.9 :
        return "Normal Health Stat"
    elif  bmi < 25 <= 29.9:
        return "Overweight"
    else:
        return "Obese, Work out!!"


while True : 
        print("..BMI HEALTH CHECK..") 
        select = input("choose '1' to calculate or 'E' to exit:  ")
        if select == '1': 
            weight = float(input("Input your weight(kg): "))
            height = float(input("Input your height(m): "))

            bmi = bmi_calc(weight, height)
            health = health_stat()

            print(f"BMI = {bmi:.2f} ")
            print(f"Health Status = {health}")
        elif select == 'E':
            print("Exiting")
        else:
            print("GoodBye!!")


