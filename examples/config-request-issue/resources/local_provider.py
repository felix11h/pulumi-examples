from typing import Any, Optional
from uuid import uuid4

import pulumi
from pulumi import ResourceOptions, dynamic


class ConfigRequestTestProvider(dynamic.ResourceProvider):

    def create(self, inputs: Any):
        print("Local provider reports: ", pulumi.Config("example").require(key="value"))
        return dynamic.CreateResult(id_=uuid4().hex, outs={})


class ConfigRequestTest(dynamic.Resource):
    def __init__(self, name: str, opts: Optional[ResourceOptions] = None):

        super().__init__(
            ConfigRequestTestProvider(),
            name,
            {},
            opts=opts,
        )
