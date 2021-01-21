import unittest
import pytest
import os
import pathlib
import h5py
import shutil

from desc.io import InputReader
from desc.io import hdf5Writer, hdf5Reader
from desc.utils import equals


def test_vmec_input(tmpdir_factory):
    input_path = "./tests/inputs/input.DSHAPE"
    tmpdir = tmpdir_factory.mktemp("desc_inputs")
    tmp_path = tmpdir.join("input.DSHAPE")
    shutil.copyfile(input_path, tmp_path)
    ir = InputReader(cl_args=[str(tmp_path)])
    vmec_inputs = ir.inputs
    vmec_inputs[0].pop("output_path")
    path = tmpdir.join("desc_from_vmec")
    ir.write_desc_input(path)
    ir2 = InputReader(cl_args=[str(path)])
    desc_inputs = ir2.inputs
    desc_inputs[0].pop("output_path")
    eq = [equals(in1, in2) for in1, in2 in zip(vmec_inputs, desc_inputs)]
    assert all(eq)


class TestInputReader(unittest.TestCase):
    def setUp(self):
        self.argv0 = []
        self.argv1 = ["nonexistant_input_file"]
        self.argv2 = ["./tests/inputs/MIN_INPUT"]

    def test_no_input_file(self):
        with self.assertRaises(NameError):
            InputReader(cl_args=self.argv0)

    def test_nonexistant_input_file(self):
        with self.assertRaises(FileNotFoundError):
            InputReader(cl_args=self.argv1)

    def test_min_input(self):
        ir = InputReader(cl_args=self.argv2)
        # self.assertEqual(ir.args.prog, 'DESC', 'Program is incorrect.')
        self.assertEqual(
            ir.args.input_file[0], self.argv2[0], "Input file name does not match"
        )
        # self.assertEqual(ir.output_path, self.argv2[0] + '.output',
        #        'Default output file does not match.')
        self.assertEqual(
            ir.input_path,
            str(pathlib.Path("./" + self.argv2[0]).resolve()),
            "Path to input file is incorrect.",
        )
        # Test defaults
        self.assertFalse(ir.args.plot, "plot is not default False")
        self.assertFalse(ir.args.quiet, "quiet is not default False")
        self.assertEqual(ir.args.verbose, 1, "verbose is not default 1")
        # self.assertEqual(ir.args.vmec_path, '', "vmec path is not default ''")
        # self.assertFalse(ir.args.gpuID, 'gpu argument was given')
        self.assertFalse(ir.args.numpy, "numpy is not default False")
        self.assertEqual(
            os.environ["DESC_USE_NUMPY"],
            "",
            "numpy environment " "variable incorrect with default argument",
        )
        self.assertFalse(ir.args.version, "version is not default False")
        self.assertEqual(
            len(ir.inputs[0]),
            26,
            "number of inputs does not match " "number expected in MIN_INPUT",
        )
        # test equality of arguments

    def test_np_environ(self):
        argv = self.argv2 + ["--numpy"]
        InputReader(cl_args=argv)
        self.assertEqual(
            os.environ["DESC_USE_NUMPY"],
            "True",
            "numpy " "environment variable incorrect on use",
        )

    def test_quiet_verbose(self):
        ir = InputReader(self.argv2)
        self.assertEqual(
            ir.inputs[0]["verbose"],
            1,
            "value of inputs['verbose'] " "incorrect on no arguments",
        )
        argv = self.argv2 + ["-v"]
        ir = InputReader(argv)
        self.assertEqual(
            ir.inputs[0]["verbose"],
            2,
            "value of inputs['verbose'] " "incorrect on verbose argument",
        )
        argv = self.argv2 + ["-vv"]
        ir = InputReader(argv)
        self.assertEqual(
            ir.inputs[0]["verbose"],
            3,
            "value of inputs['verbose'] " "incorrect on double verbose argument",
        )
        argv = self.argv2 + ["-q"]
        ir = InputReader(argv)
        self.assertEqual(
            ir.inputs[0]["verbose"],
            0,
            "value of inputs['verbose'] " "incorrect on quiet argument",
        )

    def test_vmec_to_desc_input(self):
        pass


class MockObject:
    def __init__(self):
        self._io_attrs_ = ["a", "b", "c"]


def test_writer_given_filename(writer_test_file):
    writer = hdf5Writer(writer_test_file, "w")
    assert writer.check_type(writer.target) is False
    assert writer.check_type(writer.base) is True
    assert writer._close_base_ is True
    writer.close()
    assert writer._close_base_ is False


def test_writer_given_file(writer_test_file):
    f = h5py.File(writer_test_file, "w")
    writer = hdf5Writer(f, "w")
    assert writer.check_type(writer.target) is True
    assert writer.check_type(writer.base) is True
    assert writer._close_base_ is False
    # with self.assertWarns(RuntimeWarning):
    #    writer.close()
    assert writer._close_base_ is False
    f.close()


def test_writer_close_on_delete(writer_test_file):
    writer = hdf5Writer(writer_test_file, "w")
    with pytest.raises(OSError):
        newwriter = hdf5Writer(writer_test_file, "w")
    del writer
    newwriter = hdf5Writer(writer_test_file, "w")
    del newwriter


def test_writer_write_dict(writer_test_file):
    thedict = {"1": 1, "2": 2, "3": 3}
    writer = hdf5Writer(writer_test_file, "w")
    writer.write_dict(thedict)
    writer.write_dict(thedict, where=writer.sub("subgroup"))
    with pytest.raises(SyntaxError):
        writer.write_dict(thedict, where="not a writable type")
    writer.close()
    f = h5py.File(writer_test_file, "r")
    g = f["subgroup"]
    for key in thedict.keys():
        assert key in f.keys()
        assert key in g.keys()
    f.close()


def test_writer_write_obj(writer_test_file):
    mo = MockObject()
    writer = hdf5Writer(writer_test_file, "w")
    # writer should throw runtime warning if any save_attrs are undefined
    with pytest.warns(RuntimeWarning):
        writer.write_obj(mo)
    writer.close()
    writer = hdf5Writer(writer_test_file, "w")
    for name in mo._io_attrs_:
        setattr(mo, name, name)
    writer.write_obj(mo)
    groupname = "initial"
    writer.write_obj(mo, where=writer.sub(groupname))
    writer.close()
    f = h5py.File(writer_test_file, "r")
    for key in mo._io_attrs_:
        assert key in f.keys()
    assert groupname in f.keys()
    initial = f[groupname]
    for key in mo._io_attrs_:
        assert key in initial.keys()
    f.close()


def test_reader_given_filename(reader_test_file):
    reader = hdf5Reader(reader_test_file)
    assert reader.check_type(reader.target) is False
    assert reader.check_type(reader.base) is True
    assert reader._close_base_ is True
    reader.close()
    assert reader._close_base_ is False


def test_reader_given_file(reader_test_file):
    f = h5py.File(reader_test_file, "r")
    reader = hdf5Reader(f)
    assert reader.check_type(reader.target) is True
    assert reader.check_type(reader.base) is True
    assert reader._close_base_ is False
    assert reader._close_base_ is False
    f.close()


def test_reader_read_dict(reader_test_file):
    reader = hdf5Reader(reader_test_file)
    newdict = {}
    newsubdict = {}
    otherdict = {}
    reader.read_dict(newdict)
    reader.read_dict(newsubdict, where=reader.sub("subgroup"))
    with pytest.raises(SyntaxError):
        reader.read_dict(otherdict, where="not a readable type")
    reader.close()
    if type(newdict["a"]) is bytes:
        for key in newdict.keys():
            newdict[key] = newdict[key].decode("ascii")
        for key in newsubdict.keys():
            newsubdict[key] = newsubdict[key].decode("ascii")
    thedict = {"a": "a", "b": "b", "c": "c"}
    assert thedict == newdict
    assert thedict == newsubdict


def test_reader_read_obj(reader_test_file):
    mo = MockObject()
    reader = hdf5Reader(reader_test_file)
    reader.read_obj(mo)
    mo._io_attrs_ += "4"
    with pytest.warns(RuntimeWarning):
        reader.read_obj(mo)
    del mo._io_attrs_[-1]
    submo = MockObject()
    reader.read_obj(submo, where=reader.sub("subgroup"))
    for key in mo._io_attrs_:
        assert hasattr(mo, key)
        assert hasattr(submo, key)


def test_reader_load_configuration():
    pass


def test_reader_load_equilibrium():
    pass
