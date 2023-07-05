from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files(tmp_path):
    file1_path = tmp_path / "file1.txt"
    file1_path.touch()
    file1_path.write_text("Hello World")

    file2_path = tmp_path / "file2.txt"
    file2_path.touch()
    file2_path.write_text("Hello Mars")

    file3_path = tmp_path / "file3.txt"
    file3_path.touch()
    file3_path.write_text("Hello World")

    context = {
        "all_files": [str(file1_path), str(file2_path), str(file3_path)],
    }
    expected = [(str(file1_path), str(file3_path))]
    find_duplicate_files_test = find_duplicate_files(context)
    assert find_duplicate_files_test == expected


def test_find_duplicate_files_no_duplicates(tmp_path):
    file1_path = tmp_path / "file1.txt"
    file1_path.touch()
    file1_path.write_text("Hello World")

    file2_path = tmp_path / "file2.txt"
    file2_path.touch()
    file2_path.write_text("Hello Venus")

    file3_path = tmp_path / "file3.txt"
    file3_path.touch()
    file3_path.write_text("Hello Mars")

    context = {
        "all_files": [file1_path, file2_path, file3_path],
    }
    find_duplicate_files_test = find_duplicate_files(context)
    assert len(find_duplicate_files_test) == 0


def test_find_duplicate_files_empty_list():
    context = {
        "all_files": [
            ".gitignore",
            "src/app.py",
            "src/__init__.py",
        ],
    }
    with pytest.raises(ValueError):
        find_duplicate_files(context)
