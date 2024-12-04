############################################################
# Train.py                                                 #
# This class is used to simulate the behaviors of a train. #
############################################################
class Train:
    def __init__(self, start_time, size):
        """
        Constructor for the Train class. Set up fields for this
        train.

        :param start_time: The start time of this train.
        :param size:       The maximum size of this train.
        """
        self.start_time = start_time
        self.size = size
        self.passengers = []

    def check_departure(self, s):
        """
        Decides the passengers that will leave at the given station.

        :param s: The currently arrived station.
        """
        for passenger in self.passengers:
            if passenger.dest == s.name:
                self.passengers.remove(passenger)

    def take_from(self, s, time):
        """
        Decides the passengers to take from the given station and
        returns the total waiting time for these passengers, the
        worst case waiting time and the amount of passengers.

        :param s: The currently arrived station.
        :param time: The global time when this method is called.
        :return : (1) The sum of waiting time;
                  (2) The worst case waiting time.
                  (3) The amount of passengers that leaves s.
        """
        empty_seats = self.size - len(self.passengers)
        return s.train_arrival(empty_seats, time)