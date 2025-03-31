FROM confluentinc/cp-kafka-connect:latest
USER root


RUN mkdir -p /usr/share/confluent-hub-components && \
    chmod -R 777 /usr/share/confluent-hub-components

# Install the Confluent Hub CLI
RUN curl -sL --http1.1 https://cnfl.io/cli | sh -s -- -b /usr/local/bin

# Install the JDBC connector using the Confluent Hub CLI
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:latest --component-dir /usr/share/confluent-hub-components

# Set the plugin path environment variable
ENV CONNECT_PLUGIN_PATH="/usr/share/confluent-hub-components"
