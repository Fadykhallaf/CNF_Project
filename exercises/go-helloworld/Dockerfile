FROM golang:1.16-alpine

LABEL maintainer="Fady Khallaf"

WORKDIR /app

RUN go mod init GO-HELLOWORLD

COPY . /app

RUN go build -o /helloworld

EXPOSE 6111

CMD [ "/helloworld" ]