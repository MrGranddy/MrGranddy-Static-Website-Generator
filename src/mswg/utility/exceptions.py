class EXTENSION_ERROR(Exception):
    def __init__(self, expected_ext, given_ext, message):

        self.message = message
        self.expected_ext = expected_ext
        self.given_ext = given_ext

        super().__init__(self.message)

    def __str__(self):
        return "%s Expected '%s' but '%s' is given." % (
            self.message,
            self.expected_ext,
            self.given_ext,
        )


class NAME_MISMATCH_ERROR(Exception):
    def __init__(self, n1, n2, message):

        self.n1 = n1
        self.n2 = n2
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return "%s Names '%s' and '%s' should be the same." % (
            self.message,
            self.n1,
            self.n2,
        )
