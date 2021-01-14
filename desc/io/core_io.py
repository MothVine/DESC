from abc import ABC, abstractmethod


class IO(ABC):
    """Abstract Base Class (ABC) for readers and writers."""

    def __init__(self):
        """Initalize ABC IO.

        Parameters
        ----------

        Returns
        -------

        None

        """
        self.resolve_base()

    def __del__(self):
        """Close file upon garbage colleciton or explicit deletion with del function.

        Parameters
        ----------

        Returns
        -------
        None

        """
        self.close()

    def close(self):
        """Close file if initialized with class instance.

        Parameters
        ----------

        Returns
        -------
        None

        """
        if self._close_base_:
            self.base.close()
            self._close_base_ = False
        return None

    def resolve_base(self):
        """Set base attribute.

        Base is target if target is a file instance of type given by
        _file_types_ attribute. _close_base_ is False.

        Base is a runtime-initialized file if target is a string file path.
        _close_base_ is True.

        Parameters
        ----------

        Returns
        -------
        None

        """
        if self.check_type(self.target):
            self.base = self.target
            self._close_base_ = False
        elif type(self.target) is str:
            self.base = self.open_file(self.target, self.file_mode)
            self._close_base_ = True
        else:
            raise SyntaxError(
                "file_name of type {} is not a filename or file "
                "instance.".format(type(self.target))
            )

    def resolve_where(self, where):
        """Find where 'where' points and check if it's a readable type.

        Parameters
        ----------
        where : None or file with type found in _file_types_ attribute

        Returns
        -------
        if where is None:
            base attribute
        if where is file with type foundin _file_types_
            where

        """
        if where is None:
            loc = self.base
        elif self.check_type(where):
            loc = where
        else:
            raise SyntaxError("where '{}' is not a readable type.".format(where))
        return loc

    @abstractmethod
    def open_file(self, file_name, file_mode):
        pass

    def check_type(self, obj):
        if type(obj) in self._file_types_:
            return True
        else:
            return False


class Reader(ABC):
    """ABC for all readers."""

    @abstractmethod
    def read_obj(self, obj, where=None):
        pass

    @abstractmethod
    def read_dict(self, thedict, where=None):
        pass


class Writer(ABC):
    """ABC for all writers."""

    @abstractmethod
    def write_obj(self, obj, where=None):
        pass

    @abstractmethod
    def write_dict(self, thedict, where=None):
        pass