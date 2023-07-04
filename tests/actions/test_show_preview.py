from pro_filer.actions.main_actions import show_preview  # NOQA

mock_context = {
    "all_files": [
        "src/dir1/file1.py",
        "src/dir2/file2.py",
        "src/dir3/file3.py",
        "src/dir4/file4.py",
        "src/dir5/file5.py",
    ],
    "all_dirs": [
        "src/dir1/",
        "src/dir2/",
        "src/dir3/",
        "src/dir4/",
        "src/dir5/",
    ],
}

mock_context_empty = {"all_files": [], "all_dirs": []}


def test_show_preview_not_empty_context(capsys):
    show_preview(mock_context)
    captured = capsys.readouterr()
    assert captured.out == str(
        mock_context["all_files"], mock_context["all_dirs"]
    )


def test_show_preview_empty_context(capsys):
    show_preview(mock_context_empty)
    captured = capsys.readouterr()
    assert captured.out == str(
        mock_context_empty["all_files"], mock_context_empty["all_dirs"]
    )
