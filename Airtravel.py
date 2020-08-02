class Flight:
    """Model arund Flights"""
    # def __init__(self, param1, param2) - NOT Constructor
    # self = this
    dic = {}
    def __init__(self, number, airplane):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid Airline code {}".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route No {}".format(number))

        self._number = number
        self._airplane = airplane

        NRows, Seats = self._airplane.seatingPlan()
        for seat in Seats:
            for row in NRows:
                self.dic[seat+str(row)] = None


    def getFlightNo(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def get_aircraft_model(self):
        return self._airplane.getModel()

    def allocate_seat(self, seatNo, name):
        from pprint import pprint as pp
        #pp(self.dic)

        if (seatNo not in self.dic.keys()):
            raise ValueError("This seat no does NOT exist {}".format(seatNo))

        if (self.dic[seatNo] == None):
            self.dic[seatNo] = name
            return seatNo
        else:
            raise ValueError( "Please choose another seat {}".format(seatNo))



class Airplane:
    def __init__(self, registationNum, model_num, nRows, nSeatsEachRow):
        self._registationNum = registationNum
        self._model_num = model_num

        if (nRows<1):
            raise ValueError("No. of rows can not be less than 1: {}".format(nRows))
        self._nRows = nRows

        if (nSeatsEachRow<1):
            raise ValueError( "No. of seats per row can not be less than 1: {}".format(nSeatsEachRow))
        self._nSeatsEachRow = nSeatsEachRow

    def getRegistrationNum(self):
        return self._registationNum

    def getModel(self):
        return self._model_num

    def seatingPlan(self):
        return range(1, self._nRows+1), "ABCDEFGHJ"[:self._nSeatsEachRow]


class Passenger:
    def __init__(self, fullname, email):
        self._fullname = fullname
        self._email = email

    def get_name(self):
        return self._fullname

if (__name__ == "__main__"):
    f = Flight( "SE106", Airplane( "GE-UT", "Airbus A320", 30, 6 ) )
    print( f.allocate_seat( "C14", Passenger( "dev", "dnigam@gmail.com" ).get_name() ) )
    print( "." * 50 )
    print( f.allocate_seat( "C15", Passenger( "devp", "dp@gmail.com" ).get_name() ) )
    print( "." * 50 )
    try:
        print( f.allocate_seat( "Z14", Passenger( "deva", "dn@gmail.com" ).get_name() ) )
    except ValueError as e:
        print(e)
    print( "." * 50 )
    try:
        print( f.allocate_seat( "C14", Passenger( "devp1", "dp1@gmail.com" ).get_name() ) )
    except ValueError as e:
        print(e)







