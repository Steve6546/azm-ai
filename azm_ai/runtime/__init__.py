from typing import Type

from azm_ai.runtime.base import Runtime
from azm_ai.runtime.impl.daytona.daytona_runtime import DaytonaRuntime
from azm_ai.runtime.impl.docker.docker_runtime import (
    DockerRuntime,
)
from azm_ai.runtime.impl.e2b.e2b_runtime import E2BRuntime
from azm_ai.runtime.impl.local.local_runtime import LocalRuntime
from azm_ai.runtime.impl.modal.modal_runtime import ModalRuntime
from azm_ai.runtime.impl.remote.remote_runtime import RemoteRuntime
from azm_ai.runtime.impl.runloop.runloop_runtime import RunloopRuntime
from azm_ai.utils.import_utils import get_impl

# mypy: disable-error-code="type-abstract"
_DEFAULT_RUNTIME_CLASSES: dict[str, Type[Runtime]] = {
    'eventstream': DockerRuntime,
    'docker': DockerRuntime,
    'e2b': E2BRuntime,
    'remote': RemoteRuntime,
    'modal': ModalRuntime,
    'runloop': RunloopRuntime,
    'local': LocalRuntime,
    'daytona': DaytonaRuntime,
}


def get_runtime_cls(name: str) -> Type[Runtime]:
    """
    If name is one of the predefined runtime names (e.g. 'docker'), return its class.
    Otherwise attempt to resolve name as subclass of Runtime and return it.
    Raise on invalid selections.
    """
    if name in _DEFAULT_RUNTIME_CLASSES:
        return _DEFAULT_RUNTIME_CLASSES[name]
    try:
        return get_impl(Runtime, name)
    except Exception as e:
        known_keys = _DEFAULT_RUNTIME_CLASSES.keys()
        raise ValueError(
            f'Runtime {name} not supported, known are: {known_keys}'
        ) from e


__all__ = [
    'Runtime',
    'E2BRuntime',
    'RemoteRuntime',
    'ModalRuntime',
    'RunloopRuntime',
    'DockerRuntime',
    'DaytonaRuntime',
    'get_runtime_cls',
]
