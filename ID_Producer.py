class InvalidIdLength(Exception):
    """A class to represent an Exception. Attribute id_number is
    initialized.
    """
    def __init__(self, id_number):
        """Initialization class InvalidIdLength attribute. Parameter is
        id_number.
        :param id_number: The ID number.
        :type id_number: int.
        """
        # Initializing ID number attribute.
        self._id_number = int(id_number)

    def __str__(self):
        """This method overrides the built in str function, returning
        the InvalidIdLength exception message.
        :return: The exception message.
        :rtype: str.
        """
        # Return the exception message.
        return 'Function expected length 9 ID Number, and instead ' \
               'got length %s' % len(str(self._id_number))

    def get_id_number(self):
        """This method returns the ID number.
        :return: The ID number.
        :rtype: int.
        """
        # Return the ID number.
        return self._id_number


def check_id_valid(id_number):
    """This function receives a whole number, and returns whether it is
    a valid ID number or not. First, checks for 9 digits length, second-
    checks algorithm calculation. If the first described is not met,
    error InvalidIdLength is raised.
    :param id_number: The ID number for validation.
    :type id_number: int.
    :raise: InvalidIdLength: raises an Exception.
    :return: True if ID id valid, else False.
    :rtype: bool.
    """
    # If ID length is not 9, than raise InvalidIdLength exception.
    if len(str(int(id_number))) != 9:
        raise InvalidIdLength(id_number)
    # If ID length is 9.
    else:
        # Creating a list of ID even index digits, each multiplied by 2.
        evens_lst_multiply = [2 * num for num in
                              list(map(int, str(id_number)[1::2]))]
        # Creating an edited list from the multiplied evens list.
        edit_multiplied_evens_lst = [sum(map(int, str(num))) if num > 9
                                     else num for num in
                                     evens_lst_multiply]
        # If the sum of all values from not even indexed digits and
        # edited evens list is a 10 multiplication product, than return
        # True, else False.
        if (sum(map(int, str(id_number)[0::2])) + sum(
                edit_multiplied_evens_lst)) % 10 == 0:
            return True
        return False


class IDIterator:
    """A class to represent an Iterator. Attribute _id is initialized.
    """

    def __init__(self, _id):
        """Initialization of the iterator instance variable. Parameter
        is _id.
        :param _id: The initial iterator value.
        :type _id: int.
        """
        # Initializing id attribute.
        self._id = int(_id)

    def __iter__(self):
        """This method returns a reference to the iterator.
        :return: Reference to the iterator.
        :rtype: IDIterator.
        """
        # Return instance iterator.
        return self

    def __next__(self):
        """This method iterates to the next value by a defined process-
        next valid id number, and returns the current valid id number.
        If value equals 999999999 StopIteration exception is raised.
        :raise: StopIteration: raises an Exception.
        :return: Valid id number.
        :rtype: int.
        """
        # Always loop.
        while True:
            # If id reached iteration limit value, than raise an
            # exception
            if self._id == 999999999:
                raise StopIteration()
            # If id is not valid, increase id value by 1.
            if not check_id_valid(self._id):
                self._id += 1
            # If ID is valid.
            else:
                # Increase id value by 1, and return the id before
                # incrementation
                self._id += 1
                return self._id - 1


def id_generator(id_number):
    """A Generator function that receives a number and yields the next
    valid id numbers and not exceeding (or not equal) 999999999.
    :param id_number: Current ID number.
    :type id_number: int.
    :return: Yield the next valid ID number.
    :rtype: int.
    """
    # As long as ID below 999999999.
    while id_number < 999999999:
        # If ID is not a valid ID number, increase ID value by 1.
        if not check_id_valid(id_number):
            id_number += 1
        # If ID is a valid ID number.
        else:
            # Increase ID value by 1, and return the ID before
            # incrementation
            id_number += 1
            yield id_number - 1


def main():
    """This is the main function of valid ID numbers producer. Process
    performed both by an iterator class and also generator function
    methods, printing (each) the next 10 valid ID's from given start
    number. Raising and handling an exception if start number contains
    non digits chars, and also InvalidIdLength and StopIteration
    exceptions are handled (notification message).
    :raise: ValueError: raises an Exception.
    :return: None
    """
    # Start number.
    id_number = 123456780
    # Try to run.
    try:
        # If not all chars are digits, raise ValueError exception.
        if not str(id_number).isdigit():
            raise ValueError
    # If ValueError occurred, then print notification.
    except ValueError:
        print('This is not an integer')
    # If no exception raised.
    else:
        try:
            # Create an iterator object.
            id_iter = iter(IDIterator(int(id_number)))
            # Loop 10 times, and print the next iterator value.
            for i in range(10):
                print(next(id_iter))
        # If InvalidIdLength occurred, print the exception message and
        # the invalid ID number.
        except InvalidIdLength as e:
            print(e, '(Invalid:%s)' % e.get_id_number())
        # If StopIteration occurred (reached limit 999999999 value),
        # print notification.
        except StopIteration:
            print('End Iteration - reached max valid ID number.')
        # Empty line space.
        print('')
        try:
            # Create a generator object.
            id_gen = id_generator(int(id_number))
            # Loop 10 times, and print the next generator value.
            for i in range(10):
                print(next(id_gen))
        # If InvalidIdLength occurred, print the exception message and
        # the invalid ID number.
        except InvalidIdLength as e:
            print(e, '(Invalid:%s)' % e.get_id_number())
        # If StopIteration occurred (ID is greater/equal/reached
        # 999999999 value), print notification.
        except StopIteration:
            print('No valid ID values for generator to produce.')


if __name__ == "__main__":
    main()
