
import pytest

class NotInRange(Exception):
    def __init__(self,message='value not in range'):
        self.message = message
        super().__init__(self.message)


def test_generic():
    # alawys start these function names with "test"
    a=2
    b=4
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
        else:
            assert a!=b 