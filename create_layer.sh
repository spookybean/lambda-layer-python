#!/usr/bin/env bash

PACKAGE_PATH="packages/python/lib/${PYTHON_VERSION}/site-packages"
FILENAME=my_layer.zip

echo "Downloading packages"
cat requirements.txt

mkdir -p "${PACKAGE_PATH}" build

pip install -r requirements.txt --target "${PACKAGE_PATH}" > /dev/null 2>&1

cd packages/

zip -r9 "${FILENAME}" . > /dev/null 2>&1

mv "${FILENAME}" ../build &&\
cd -

echo "Created ${FILENAME}"
