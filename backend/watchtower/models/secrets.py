from pydantic import BaseModel, AnyUrl, validator, ValidationError, Field


class Repository(BaseModel):
    name: str
    url: AnyUrl

    username: str | None
    password: str | None = Field(exclude=True)

    @validator("url")
    def url_must_end_in_git(cls, v):
        if not v.endswith(".git"):
            raise ValidationError("Must end in .git")
        return v
