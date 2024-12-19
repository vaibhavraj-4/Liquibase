    # Base image
    FROM openjdk:8-jdk-slim

    # Install Liquibase and dependencies
    RUN apt-get update && \
        apt-get install -y wget unzip && \
        wget https://github.com/liquibase/liquibase/releases/download/v4.23.2/liquibase-4.23.2.tar.gz && \
        tar -zxvf liquibase-4.23.2.tar.gz && \
        mv liquibase /opt/liquibase && \
        rm liquibase-4.23.2.tar.gz
        
    # Install MySQL JDBC Driver
    COPY mysql-connector-j-9.0.0.jar /automate_liquibase/mysql-connector-j-9.0.0.jar

    RUN ls -l /opt/liquibase

    # Set environment variables
    ENV PATH="/opt/liquibase:$PATH"
    



    # Copy Liquibase changelog and properties file to the image
    COPY db.changelog.xml /automate_liquibase/db.changelog.xml
    COPY liquibase.properties /automate_liquibase/liquibase.properties

    # Run Liquibase update when the container starts
    CMD ["liquibase", "--defaultsFile=/automate_liquibase/liquibase.properties", "update"]