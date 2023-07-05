from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date

mock_context_file = {
    "base_path": "/home/trybe/????",
}


def test_show_details(capsys, tmp_path):
    file = tmp_path / "duranda1.py"
    file.touch()
    mock_context = {
        "base_path": str(file),
    }
    show_details(mock_context)
    captured = capsys.readouterr()
    time = date.today()
    assert (
        captured.out
        == f"File name: duranda1.py\n\
File size in bytes: 0\nFile type: file\nFile extension: .py\n\
Last modified date: {time}\n"
    )


def test_show_details_extension(capsys, tmp_path):
    file = tmp_path / "duranda1"
    file.touch()
    mock_context_extension = {
        "base_path": str(file),
    }
    show_details(mock_context_extension)
    captured = capsys.readouterr()
    time = date.today()
    assert (
        captured.out
        == f"File name: duranda1\n\
File size in bytes: 0\nFile type: file\nFile extension: [no extension]\n\
Last modified date: {time}\n"
    )


def test_show_details_file(capsys):
    show_details(mock_context_file)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"
