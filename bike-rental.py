class Bike:
    list_of_bikes = []
    rate = 0
    bill = 0
    def __init__(self,stock,bikes_requested):
        self.stock = stock

        self.bikes_requested = bikes_requested

    def price_of_bikes(self,type_of_rate):
        if type_of_rate == "hourly":
            Bike.rate = 5
        elif type_of_rate == "daily":
            Bike.rate = 20
        elif type_of_rate == "weekly":
           Bike.rate = 60

        return Bike.rate


    def get_bill(self):
        total = 0
        for item in Bike.list_of_bikes:
            total += item

        Bike.bill = total
        return Bike.bill

    def discount(self,bill,family_members, rentals):

        if family_members >= 5 and rentals >=3 or rentals <= 5:
            Bike.bill = Bike.bill * 0.70

        return Bike.bill

            







def main():
    num_family_members = int(input("How many members in your group are renting bikes?\nFamilies of 5 or greater, renting between 3 and 5 bikes get 30% off: "))
    check_if_bike_available = True
    while check_if_bike_available:
        inputStock = int(input("How many bikes would you like?: "))
        bike = Bike(25,inputStock)
        if inputStock > bike.stock:
            print("Sorry, we don't have that many bikes")
            print("The amount of available bikes is {}".format(bike.stock))
        else:

            break

    amount_bikes = 1
    i = 0
    while i < inputStock:

        rate_of_bikes = input("For bike {}, enter either hourly,weekly, or monthly to choose what type of rental you want: ".format(amount_bikes))

        how_long_customer_wants_bike = int(input("How long do you want bike {} for?: ".format(amount_bikes)))
        getBike = bike.price_of_bikes(rate_of_bikes)  * how_long_customer_wants_bike
        Bike.list_of_bikes.append(getBike)


        amount_bikes += 1

        i+=1



    get_bikes_bill = bike.discount(bike.get_bill(),num_family_members,inputStock)
    print(Bike.list_of_bikes)
    print(get_bikes_bill)


if __name__ == '__main__':
    main()