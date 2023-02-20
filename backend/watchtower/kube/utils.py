import os
from kubernetes import client, config


class KubernetesError(Exception):
    """
    Exception thrown when unable to configure our k8s requirements, such as the client or retrieving the namespace
    """


VALID_ENVS = ["development", "cluster"]


def get_kube_client() -> client.CoreV1Api:
    """
    A helper function that returns a kubernetes api client, and loads kubeconfig based upon "ENVIRONMENT" variable
    :return: A CoreV1Api instance
    """
    # If the environment application is running in a cluster, return the in cluster config
    if (
        os.environ.get("ENVIRONMENT") is not None
        and os.environ.get("ENVIRONMENT").lower() == "cluster"
    ):
        config.load_incluster_config()
    elif (
        os.environ.get("ENVIRONMENT") is not None
        and os.environ.get("ENVIRONMENT").lower() == "development"
    ):
        config.load_kube_config(
            config_file=os.environ.get("KUBECONFIG_PATH", "/root/.kube/config")
        )
    else:
        raise KubernetesError(f"ENVIRONMENT is not one of {VALID_ENVS}")

    try:
        return client.CoreV1Api()
    except Exception as e:
        raise KubernetesError(f"Error in loading kubernetes environment: {e}")


def get_kube_namespace() -> str:
    """
    A helper function that gets the namespace to look for items in
    :return: String version of namespace name
    """
    # If the application is running in a cluster, then return that namespace
    if os.environ.get("NAMESPACE", None) is not None:
        return os.environ.get("NAMESPACE")
    elif (
        os.environ.get("ENVIRONMENT") is not None
        and os.environ.get("ENVIRONMENT").lower() == "cluster"
    ):
        return "watchtower"  # TODO: Get namespace name from pod
    return "watchtower"
