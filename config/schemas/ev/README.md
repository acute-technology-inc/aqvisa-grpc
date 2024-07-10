# Electrical Validation Schema

This is the JSON schema used by Electical Validation, which follows json schema draft 2020-12.

## Schema Structure

```
.
├── common
│   └── advance.json
├── examples
│   └── sample_config.json
└── i2c
│   ├── channel.json
│   ├── decode.json
│   ├── trigger.json
│   └── validation.json
└── i2s
...
└── ev.schema.json
```

This main schema is the `ev.schema.json` file. It includes the subschemas from `common` and all directory named after the protocol name.

For example, the configuration regarding `I2C` is in the [`i2c/`](https://github.com/acute-technology-inc/aqvisa-grpc/tree/main/config/schemas/ev/i2c) directory.

There is also a directory called [`examples`](https://github.com/acute-technology-inc/aqvisa-grpc/tree/main/config/schemas/ev/examples), which includes sample input JSON configuration file for Electrical Validation.

## Reference

JSON schema 2020-12: https://json-schema.org/draft/2020-12/release-notes
