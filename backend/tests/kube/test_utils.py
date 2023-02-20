import pytest

from watchtower.kube.utils import get_kube_client, KubernetesError, get_kube_namespace


@pytest.fixture
def set_env_none(monkeypatch):
    monkeypatch.delenv("ENVIRONMENT", raising=False)


@pytest.fixture
def set_namespace_none(monkeypatch):
    monkeypatch.delenv("NAMESPACE", raising=False)


@pytest.fixture
def set_namespace_watchtower(monkeypatch):
    monkeypatch.setenv("NAMESPACE", "watchtower")


@pytest.fixture
def set_namespace_somethingelse(monkeypatch):
    monkeypatch.setenv("NAMESPACE", "somethingelse")


def test_no_environment_config(set_env_none):
    # Assert that if no environment set, raise exception
    with pytest.raises(KubernetesError) as exc_info:
        get_kube_client()


def test_no_environment_namespace(set_namespace_none):
    # Validate default case of watchtower as namespace name
    assert get_kube_namespace() == "watchtower"


def test_namespace_watchtower(set_namespace_watchtower):
    # Validate that if running in watchtower namespace, namespace watchtower returned
    assert get_kube_namespace() == "watchtower"


def test_namespace_somethingelse(set_namespace_somethingelse):
    # Validate that if namespace env var is set as somethingelse, use that namespace name
    assert get_kube_namespace() == "somethingelse"
