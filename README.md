## Pulumi examples

This repository contains standalone examples and demonstrations for defining and creating resources with Pulumi using Python. To minimise setup, the Pulumi projects operate fully locally.

#### Setup

To run any demo, first locally install the dependencies with Poetry. For example, if you want to use a Poetry virtual environment,
```sh
poetry env use python && poetry install
```

Then, to run a specific demo, navigate `examples/<demo-name>`, run
```sh
poetry run pulumi up
```

and follow the instructions to create a new stack locally. The new stack can be found in `.backend`.

---

The repository contains the following examples:

### Dynamic resource local file provider

Demonstrates the concept of dynamic resource providers by defining a resource provider that creates, reads, updates and deletes local files. See also [pulumi.com/blog/dynamic-providers](https://www.pulumi.com/blog/dynamic-providers/).


### Output conversion

Demonstrates the concept of Pulumi outputs by showing in what circumstances a Pulumi output can be converted and printed as a string. See also  [pulumi.com/docs/inputs-outputs/](https://www.pulumi.com/docs/intro/concepts/inputs-outputs/).

### Config request issue