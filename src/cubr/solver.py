import kociemba

from collections import Counter


class cubeSolver():
    def __init__(self):
        pass

    def solve(self, cubeState):
        # TODO need to add validation for cubeState variable first: must be
        # list.
        self.cubeState = cubeState

        # Rough validation of cube state
        self.cubieCounts = Counter(self.cubeState)

        # TODO
        # PROBABLY the CV needs to record colours specifically (not relative
        # face references), to account for the fact that the new solver will not
        # have 'fixed' faces.
        # for the new solver, the CV would also be reponsible for figuring out
        # the correlation between colours, and the FRBDUL notation.
        # Afterwards, the colours would be converted into the correct notation.
        # HOWEVER, assuming this simplified list (as below) at this point is
        # probably okay.
        colours = {0: 'U', 1: 'R', 2: 'F', 3: 'D', 4: 'L', 5: 'B'}

        print("Cubie counts")
        print(self.cubieCounts)

        for colour in colours:
            if (self.cubieCounts[colours[colour]] != 9):
                # TODO more specific error handling here, when that can be
                # implemented.
                print("Incorrect number of colours detected")
                raise Exception

        self.cubeString = ''.join(self.cubeState)
        # Find cube solution
        try:
            self.solution = kociemba.solve(self.cubeString)
            return self.solution
        except ValueError:
            pass
            # TODO cubestate was not valid: pass on the exception
