from pro_filer.actions.main_actions import show_preview  # NOQA

mock_context = {
    "all_files": [
        "src/__init__.py",
        "src/app.py",
        "src/utils/__init__.py",
        "src/utils/alpha.py",
        "src/utils/beta.py",
        "src/utils/gamma.py",
    ],
    "all_dirs": ["src", "src/utils"],
}

mock_context_empty = {"all_files": [], "all_dirs": []}


def test_show_preview_not_empty_context(capsys):
    show_preview(mock_context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Found 6 files and 2 directories\n\
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py',\
 'src/utils/alpha.py', 'src/utils/beta.py']\n\
First 5 directories: ['src', 'src/utils']\n"
    )


def test_show_preview_empty_context(capsys):
    show_preview(mock_context_empty)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"
