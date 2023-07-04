from pro_filer.actions.main_actions import show_disk_usage  # NOQA

mock_context = {
    "all_files": ["pro_filer/actions/alpha_actions.py"],
}

mock_context_empty = {
    "all_files": [],
}


def test_show_disk_usage(capsys):
    show_disk_usage(mock_context)
    captured = capsys.readouterr()
    assert (
        captured.out == "'pro_filer/actions/alpha_actions.py' uses 2.29 KB\n"
    )


def test_show_disk_usage_empty(capsys):
    show_disk_usage(mock_context_empty)
    captured = capsys.readouterr()
    assert captured.out == "Total disk usage: 0.00 KB\n"
