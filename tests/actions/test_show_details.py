from pro_filer.actions.main_actions import show_details  # NOQA

mock_context = {
    "base_path": "pro_filer/actions/alpha_actions.py",
}

mock_context_extension = {
    "base_path": "pro_filer/actions/alpha_actions",
}

mock_context_file = {
    "base_path": "/home/trybe/????",
}


def test_show_details(capsys):
    show_details(mock_context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "File name: alpha_actions.py\n\
File size in bytes: 2346\nFile type: file\nFile extension: [no extension]\n\
Last modified: 2021-08-31 15:00:00\n"
    )


def test_show_details_extension(capsys):
    show_details(mock_context_extension)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "File name: alpha_actions\n\
File size in bytes: 2346\nFile type: file\nFile extension: [no extension]\n\
Last modified: 2021-08-31 15:00:00\n"
    )


def test_show_details_file(capsys):
    show_details(mock_context_file)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"
