import pulumi

from resources.random_output import RandomOutput, InputReader

random_output = RandomOutput("test_random")

# the Output[str] property is not directly accessible
print("print(random_output.property)  # outside of resources")
print(">>>", random_output.property)  # <pulumi.output.Output object at 0x7fdd381ed310>

# however, used as input to another resource, output can be printed correctly
i1 = InputReader(
    resource_name="test_input_01",
    input_str=random_output.property,
    comment="print(random_output.property)  # from within InputReader",
)


# str manipulations on the Output[str] do not work in a straightforward manner
i2 = InputReader(
    resource_name="test_input_02",
    input_str=f"modified-{random_output.property}",
    comment="print(f\"modified-{random_output.property}\")  # from within InputReader",
    opts=pulumi.ResourceOptions(depends_on=[i1]),
)

# to manipulate Output[str] use for example .apply
# (there are also other ways, see https://www.pulumi.com/docs/intro/concepts/inputs-outputs/)
i3 = InputReader(
    resource_name="test_input_03",
    input_str=random_output.property.apply(lambda prop: f"modified-{prop}"),
    comment="print(random_output.property.apply(lambda prop: f\"modified-{prop}\"))  # from with InputReader",
    opts=pulumi.ResourceOptions(depends_on=[i1, i2]),
)






