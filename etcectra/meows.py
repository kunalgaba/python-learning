class Cat:
    # : int is a type hint for python
    MEOWS: int = 3

    # -> None is a type hint for return type
    def meow(self) -> None:
        # This is doc string and how functions should be documented
        """
        Says meow n times.

        :param self: Instance of the class
        :type self: Cat type
        :raise Type Error: if MEOWS is not int
        :rtype: None
        """
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()
