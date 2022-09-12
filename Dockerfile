FROM ubuntu:22.04 as builder
RUN apt update && apt install -y clang make
COPY cctools/cctools /build/
WORKDIR /build
RUN ./configure && make

FROM ubuntu:22.04

COPY --from=builder /build/misc/lipo /usr/bin/lipo
WORKDIR /app

ENTRYPOINT ["/usr/bin/lipo"]
