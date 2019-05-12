class SequenceFormatter:
    @staticmethod
    def format(y, x, size):
        raise NotImplementedError("Call abstract method")


class RowSequenceFmt(SequenceFormatter):
    @staticmethod
    def format(y, x, size):
        return tuple([y, x - size, size, 0])


class ColSequenceFmt(SequenceFormatter):
    @staticmethod
    def format(y, x, size):
        return tuple([x - size, y, size, 1])
