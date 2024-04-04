from linked_list import LinkedList


class Airline:
    def __init__(self):
        self.all = LinkedList()
        self.curr = None
    
    def add_flight(self, filename):
        f = open(filename)

        for x in f:
            line = x.strip("\n")
            line = line.split(",")
            self.all.insert_back({"Airline":line[0],"DepartureAirport":line[1], "ArrivalAirport":line[2], "ScheduleArrival":line[3],"ArrivalTime":line[4]})
        self.curr = self.all.get_iterator()
        


    def current_destination(self):
        return self.curr.current_value()["Airline"]

    def next_book(self):
        if not self.curr.has_next():
            self.curr = self.all.get_iterator()
            return self.curr.current_value()["Airline"]
        self.curr.next()

    def all_flight(self):
        self.itr = self.all.get_iterator()
        flight_data = []
        ptr = self.itr
        while self.itr.has_next():
            flight_data.append(ptr.current_value()["Airline"])
            ptr.next()
        flight_data.append(ptr.current_value()["Airline"])

        return flight_data


    #count the time the flight delayed
    def flight_delay(self):
        self.itr = self.all.get_iterator()
        fl_ddelay = []
        delay = 0
        ptr = self.itr
        while self.itr.has_next():
            delay = int(ptr.current_value()["ScheduleArrival"]) - int(ptr.current_value()["ArrivalTime"])
            fl_ddelay.append({"Airline":ptr.current_value()["Airline"],"Delay Time": delay})
            ptr.next()
            

        delay = int(ptr.current_value()["ScheduleArrival"]) - int(ptr.current_value()["ArrivalTime"])
        fl_ddelay.append({"Airline":ptr.current_value()["Airline"],"Delay Time": delay})

        return fl_ddelay

    def count_on_time(self):
        self.itr = self.all.get_iterator()
        fl_ddelay = []
        delay = 0
        ptr = self.itr
        while self.itr.has_next():
            delay = int(ptr.current_value()["ScheduleArrival"]) - int(ptr.current_value()["ArrivalTime"])
            if delay == 0:
                fl_ddelay.append(ptr.current_value()["Airline"])
            ptr.next()

        delay = int(ptr.current_value()["ScheduleArrival"]) - int(ptr.current_value()["ArrivalTime"])
        if delay == 0:
                fl_ddelay.append(ptr.current_value()["Airline"])

        return fl_ddelay
        
    def debug(self):
##        print(self.all.display_list())
        pass
    


a = Airline()
a.add_flight("flight.csv")
print(a.current_destination())
a.next_book()
print(a.current_destination())
##print(a.all_flight())
a.debug()
print(a.flight_delay())
print("Flights on time:",a.count_on_time())



