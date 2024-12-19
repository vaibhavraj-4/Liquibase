FROM openjdk:21-jdk-slim

WORKDIR /app

COPY liquibase-core.jar /app/
COPY liquibase-commercial.jar /app/
COPY db.changelog.xml /app/
COPY liquibase.properties /app/

RUN apt-get update && apt-get install -y default-mysql-client
RUN 
ENV LIQUIBASE_HOME=/app

ENTRYPOINT ["java", "-cp", "liquibase-core.jar:liquibase-commercial.jar:.", "liquibase.integration.commandline.LiquibaseLauncher"]
