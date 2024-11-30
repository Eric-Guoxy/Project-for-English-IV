import queue
import random

from IPython.utils.tokenutil import token_at_cursor

from Passenger import Passenger
global clock


##############################################################
# Station.py                                                 #
# This class is used to simulate the behaviors of a station. #
##############################################################
class Station:
    def __init__(self, name):
        """
        Used to keep records of all the passengers that are waiting
        to get on the train.

        :param name: The name of this station.
        """
        self.name = name
        self.passengers = queue.Queue()
        stations = ["", "", "", "", ""]
        self.later_stations = stations[stations.index(name):]

    def generate_passenger(self, p, time):
        """
        The core logic of a station, generate a passenger at every
        new global clock time. The model chosen for generating new
        passengers is a Poisson process with parameter lambda. We
        can adjust this parameter to simulate different arrival rate
        (passenger flow) at different periods in a day.
        The way that we simulate the Poisson process is using the
        binomial process with small-time gap.

        :param p:    The probability for generating a new passenger
                     (also the parameter of the binomial process).
        :param time: The global time when this method is called.
        """
        rand = random.random()
        if rand < p:
            new_passenger = Passenger.__init__(time, random.choice(self.later_stations))
            self.passengers.put(new_passenger)

    def train_arrival(self, n):
        """
        Simulate the behavior of a train arrival and push out the designated
        amount of passengers.

        :param n: The amount of passengers to push off queue.
        :return : (1) The overall waiting time.
                  (2) The worst case waiting time.
                  (3) The amount of passengers that gets on the train.
        """
        total_wait = 0
        worst_wait = -1
        amount = 0
        while amount < n and not self.passengers.empty():
            passenger = self.passengers.get()
            waiting_time = passenger.waiting_time(clock)
            total_wait += waiting_time
            if waiting_time > worst_wait:
                worst_wait = waiting_time
            amount += 1
        return total_wait, worst_wait, amount