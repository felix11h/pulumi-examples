import os
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4

import pulumi
from pulumi import Input, Output
from pulumi.dynamic import CreateResult, Resource, ResourceProvider


class LocalFileResourceProvider(ResourceProvider):

    def create(self, props: Any) -> CreateResult:
        Path(props["path"]).write_text(props["content"])
        return CreateResult(id_=uuid4().hex, outs=props)

    def delete(self, _id: str, _props: Any) -> None:
        # assert _props["key"] == "ABC123"
        os.remove(_props["path"])


class LocalFile(Resource):
    content: Output[str]
    path: Output[str]

    def __init__(
        self,
        resource_name: str,
        content: Input[str],
        path: Input[str],
        opts: Optional[pulumi.ResourceOptions] = None,
    ):
        super().__init__(
            LocalFileResourceProvider(),
            name=resource_name,
            props={"content": content, "path": path},
            # props={"content": content, "path": path, "key": "ABC123"},
            opts=opts,
        )
