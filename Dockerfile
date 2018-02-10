FROM mysql

ADD files/init_db files/run_db files/schema.sql /tmp/

RUN /tmp/init_db

ENTRYPOINT "/tmp/run_db"


