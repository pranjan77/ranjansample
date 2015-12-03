FROM kbase/sdkbase:latest
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

# RUN apt-get update

# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work

WORKDIR /kb/module

RUN make

# ranjansample

RUN echo "hello ranjansample" >> /kb/module/work/dockerspit.txt

# /ranjansample

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
