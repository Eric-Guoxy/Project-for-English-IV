##############################################################
# Passenger.py                                               #
# This class is used to simulate the behavior of passengers. #
##############################################################
class Passenger:
    def __init__(self, start_time, dest):
        """
        The constructor for the Passenger class, given the start
        waiting time and the destination of the passenger,
        generate a new passenger object.

        :param start_time: The start waiting time for this passenger.
        :param dest:       The destination of this passenger.
        """
        self.start_time = start_time
        self.dest = dest

    def waiting_time(self, leave_time):
        """
        Given the time that the passenger takes the train, calculate
        the waiting time of this passenger.

        :param leave_time: The time that the passenger takes the train.
        :return:           The waiting time of this passenger.
        """
        return leave_time - self.start_time
