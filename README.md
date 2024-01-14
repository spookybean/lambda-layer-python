# AWS Lambda layer

An automation to create lambda layer for python dependencies using docker. Based on jinja templates to generate docker files.

## Requirements & setup

python >= 3.8

```bash
pip install jinja2
```

## Steps

1. Generate `Dockerfile` & `compose.yaml`

```bash
python main.py -v 3.10 -p linux/arm64/v8
```

2. Create `requirements.txt` for python dependencies.

Use sample file for demo or build your own and copy it in current directory

```bash
cp samples/requirements.txt .
```

3. Create lambda layer

```bash
docker compose up
```

4. `my_layer.zip` would be available under `./build` dir

## Samples

Some samples files are provided in `./samples` dir
