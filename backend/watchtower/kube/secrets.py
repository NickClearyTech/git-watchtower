import base64

from pydantic import BaseModel

from kubernetes.client import V1Secret, V1ObjectMeta


# A list of fields which may be in some models, but should not be in the k8s secret
# Things like status are not declarative
FIELDS_NOT_IN_SECRET = {"name", "status"}


def secret_to_model(secret: V1Secret, model: type[BaseModel]) -> BaseModel:
    model_data = {}
    # For each value in the data section, decode it
    for key, value in secret.data.items():
        model_data[key] = base64.b64decode(value)
    model_data["name"] = secret.metadata.name
    print(model_data)
    return model(**model_data)


def model_to_secret(secret: BaseModel) -> V1Secret:
    dict_secret = secret.dict(exclude=FIELDS_NOT_IN_SECRET)
    for key, value in dict_secret.items():
        dict_secret[key] = base64.b64encode(value)
    return V1Secret(
        data=dict_secret,
        metadata=V1ObjectMeta(
            name=secret.name,
            labels={"watchtower/secret-type": secret.watchtower_secret_type},
        ),
    )


def create_or_update_secret(secret: V1Secret) -> V1Secret:
    """
    A helper function that will create or update a kubernetes secret
    :param secret:
    :return:
    """