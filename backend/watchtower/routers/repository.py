from fastapi import APIRouter
from watchtower.kube.utils import get_kube_client

router = APIRouter(
    prefix="/repository",
    tags=["repository"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_repositories():
    client = get_kube_client()
    #result = client.list_namespaced_secret(namespace="watchtower",label_selector="watchtower/secret-type=repository")
    result = client.list_namespaced_secret(namespace="watchtower", label_selector="watchtower/secret-type=repository",field_selector="metadata.name=test-secret-2")
    print(result)
    return {}