from unittest.mock import patch

from azm_ai.core.config import AppConfig


# Mock StaticFiles
class MockStaticFiles:
    def __init__(self, *args, **kwargs):
        pass


# Patch necessary components before importing from listen
with (
    patch('fastapi.staticfiles.StaticFiles', MockStaticFiles),
):
    from azm_ai.server.file_config import (
        is_extension_allowed,
        load_file_upload_config,
    )


def test_load_file_upload_config():
    config = AppConfig(
        file_uploads_max_file_size_mb=10,
        file_uploads_restrict_file_types=True,
        file_uploads_allowed_extensions=['.txt', '.pdf'],
    )
    max_size, restrict_types, allowed_extensions = load_file_upload_config(config)

    assert max_size == 10
    assert restrict_types is True
    assert set(allowed_extensions) == {'.txt', '.pdf'}


def test_load_file_upload_config_invalid_max_size():
    config = AppConfig(
        file_uploads_max_file_size_mb=-5,
        file_uploads_restrict_file_types=False,
        file_uploads_allowed_extensions=[],
    )
    with patch('azm_ai.server.shared.config', config):
        max_size, restrict_types, allowed_extensions = load_file_upload_config()

        assert max_size == 0  # Should default to 0 when invalid
        assert restrict_types is False
        assert allowed_extensions == ['.*']  # Should default to '.*' when empty


def test_is_extension_allowed():
    with (
        patch('azm_ai.server.file_config.RESTRICT_FILE_TYPES', True),
        patch('azm_ai.server.file_config.ALLOWED_EXTENSIONS', ['.txt', '.pdf']),
    ):
        assert is_extension_allowed('file.txt')
        assert is_extension_allowed('file.pdf')
        assert not is_extension_allowed('file.doc')
        assert not is_extension_allowed('file')


def test_is_extension_allowed_no_restrictions():
    with patch('azm_ai.server.file_config.RESTRICT_FILE_TYPES', False):
        assert is_extension_allowed('file.txt')
        assert is_extension_allowed('file.pdf')
        assert is_extension_allowed('file.doc')
        assert is_extension_allowed('file')


def test_is_extension_allowed_wildcard():
    with (
        patch('azm_ai.server.file_config.RESTRICT_FILE_TYPES', True),
        patch('azm_ai.server.file_config.ALLOWED_EXTENSIONS', ['.*']),
    ):
        assert is_extension_allowed('file.txt')
        assert is_extension_allowed('file.pdf')
        assert is_extension_allowed('file.doc')
        assert is_extension_allowed('file')
