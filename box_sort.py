# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/24/2023
# Description: Defines a Box class representing a box with height, width, length, and volume.
# Defines a box sort function that sorts a list of boxes by volume


class Box:
    """
    Takes parameters for height, width, length to represent a Box.
    Has a method named volume to return the volume of the Box.
    """

    def __init__(self, height, width, length):
        self._height = height
        self._width = width
        self._length = length

    def volume(self):
        """
        Uses the height, width, and length data members to find the volume of a Box object.
        Returns volume.
        """
        volume = self._height * self._width * self._length
        return volume

    def get_length(self):
        """
        Returns the length of the Box object
        """
        return self._length

    def get_width(self):
        """
        Returns the width of the Box object
        """
        return self._width

    def get_height(self):
        """
        Returns the height of the Box object
        """
        return self._height


def box_sort(sort_list):
    """
    Uses insertion sort to  sort a list of Box objects from greatest to least volume.
    :param sort_list: A list of box objects
    :return: None, sorts list through mutation
    """
    for index in range(1, len(sort_list)):  # iterates for each object but first (as list of 1 is sorted)
        value = sort_list[index]
        pos = index - 1
        while pos >= 0 and sort_list[pos].volume() < value.volume():  # compares volumes, runs when before volume is lesser
            sort_list[pos + 1] = sort_list[pos]  # slides lesser volume one space right
            pos -= 1  # decrements pos for next comparison
        sort_list[pos + 1] = value  # if before volume is greater, places value back at original position
