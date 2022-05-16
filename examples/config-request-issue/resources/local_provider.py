from typing import Any, Optional
from uuid import uuid4

import pulumi
from pulumi import ResourceOptions, dynamic


class ConfigRequestTestProvider(dynamic.ResourceProvider):

    def create(self, props: Any):
        print(props)
        return dynamic.CreateResult(id_=uuid4().hex, outs={})


class ConfigRequestTest(dynamic.Resource):

    def __init__(self, name: str, repository: pulumi.Input[str], opts: Optional[ResourceOptions] = None):
        super().__init__(
            ConfigRequestTestProvider(),
            name,
            props={"repo": repository},
            opts=opts,
        )
