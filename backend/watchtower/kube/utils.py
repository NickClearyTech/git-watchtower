import os
from kubernetes import client, config


def get_kube_client() -> client.CoreV1Api:
    """
    A helper function that returns a kubernetes api client, and loads kubeconfig based upon "ENVIRONMENT" variable
    :return: A CoreV1Api instance
    """
    # If the environment application is running in a cluster, return the in cluster config
    if os.environ.get("ENVIRONMENT", "CLUSTER").lower() == "cluster":
        config.load_incluster_config()
    else:
        config.load_kube_config(
            config_file=os.environ.get("KUBECONFIG_PATH", "/root/.kube/config")
        )
    return client.CoreV1Api()
