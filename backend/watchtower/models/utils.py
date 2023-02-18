from pydantic import BaseModel
import base64


def secret_to_model(secret: dict, model: type[BaseModel]):
    model_data = {}
    # For each value in the data section, decode it
    #
    for key, value in secret.data.items():
        model_data[key] = base64.b64decode(value)
    model_data["name"] = secret.metadata.name
    return model(**model_data)
