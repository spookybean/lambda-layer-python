FROM public.ecr.aws/lambda/python:3.10

WORKDIR /layer

RUN dnf update &&\
  dnf install -y zip &&\
  dnf clean all

COPY create_layer.sh .

CMD [ "create_layer.sh" ]
