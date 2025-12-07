import pytest
from project import (
    parse,
    find_parent,
    parse_lines,
    validate_lines,
    validate_line,
    validate_block,
    calc_indent,
    find_odd_one,
    main,
)


def test_parse():
    with open("test_sample_valid.yaml") as f:
        assert (parse(f)) == "Valid YAML!"

    with open("test_sample_invalid.yaml") as f:
        assert (parse(f)) != "Valid YAML!"


def test_find_parent():
    lines = ["yaml:", "pipeline:", " branches:"]
    line = " branches:"
    assert (find_parent(lines, line, 2)) == ("pipeline:", 1)

    lines = ["yaml:", "pipeline:", " branches:"]
    line = "pipeline:"
    assert (find_parent(lines, line, 1)) == ("root", 0)

    lines = ["yaml:", "pipeline:", " branches:"]
    line = "notexist:"
    with pytest.raises(IndexError):
        find_parent(lines, line, 5)


def test_parse_lines():
    lines = ["test:", "pipelines:", " branches:"]

    d = parse_lines(lines, number=0)
    data = sorted(d, key=lambda s: s["pos"])
    assert (data[0]["line"]) == "test:"
    assert (data[1]["line"]) == "pipelines:"
    assert (data[2]["line"]) == " branches:"

    assert (data[0]["pos"]) == 0
    assert (data[1]["pos"]) == 1
    assert (data[2]["pos"]) == 2

    assert (data[0]["parentpos"]) == 0
    assert (data[1]["parentpos"]) == 0
    assert (data[2]["parentpos"]) == 1

    assert (data[0]["parent"]) == "root"
    assert (data[1]["parent"]) == "root"
    assert (data[2]["parent"]) == "pipelines:"

    assert (data[0]["indent"]) == 0
    assert (data[1]["indent"]) == 0
    assert (data[2]["indent"]) == 1

    lines.append("   test:yaml")
    d = parse_lines(lines, number=0)
    d = sorted(d, key=lambda s: s["pos"])
    assert (d[3]["line"]) == "   test:yaml"
    assert (d[3]["pos"]) == 3
    assert (d[3]["parentpos"]) == 2
    assert (d[3]["parent"]) == " branches:"
    assert (d[3]["indent"]) == 3


def test_validate_lines():
    lines = ["test:", "pipelines:", " branches:test", "    pipe:"]
    d = parse_lines(lines, number=0)
    assert (validate_lines(d)) != "Valid YAML!"

    lines = ["test:", "pipelines:", "branches:test", "pipe:"]
    d = parse_lines(lines, number=0)
    print(validate_lines(d))
    assert (validate_lines(d)) != "Valid YAML!"

    lines = ["test:", "pipelines:", " branches:", "    pipe:"]
    d = parse_lines(lines, number=0)
    print(validate_lines(d))
    assert (validate_lines(d)) == "Valid YAML!"


def test_validate_block():
    lines = ["test:", "pipelines:", " branches:test", "    pipe:"]
    d = parse_lines(lines, number=0)
    assert (validate_block(d)) != ""


def test_validate_line():
    line = {"line": 'title: "this is test', "pos": 0}
    assert (validate_line(line)) != ""

    line = {"line": "title: [this is test", "pos": 0}
    assert (validate_line(line)) != ""

    line = {"line": "tit::le", "pos": 0}
    assert (validate_line(line)) != ""

    line = {"line": "-    test:", "pos": 0}
    assert (validate_line(line)) != ""

    line = {"line": "- test: test", "pos": 0}
    assert (validate_line(line)) == ""

    line = {"line": "test: test", "pos": 0}
    assert (validate_line(line)) == ""


def test_calc_indent():
    assert (calc_indent("    test")) == 4
    assert (calc_indent("test")) == 0
    assert (calc_indent("   test test 123")) == 3


def test_find_odd_one():
    assert (find_odd_one([8, 8, 0])) == 2
    assert (find_odd_one([8, 8, 8])) == None
    assert (find_odd_one([])) == None
