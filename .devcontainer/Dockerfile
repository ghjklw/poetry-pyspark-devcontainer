FROM mcr.microsoft.com/devcontainers/base:bullseye

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=vscode

ARG SPARK_VERSION
ARG HADOOP_VERSION
ARG OPENJDK_VERSION
ARG PYTHON_VERSIONS

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y build-essential --no-install-recommends make \
        ca-certificates \
        ca-certificates-java \
        git \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev \
        openjdk-${OPENJDK_VERSION}-jre-headless \
        bash-completion

ENV SPARK_HOME=/usr/local/spark

# Install Spark
RUN HADOOP_MAJOR_VERSION=`echo ${HADOOP_VERSION} | cut -d. -f1` && \
    wget -qO "spark.tgz" "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MAJOR_VERSION}.tgz"; \
    tar xzf "spark.tgz" -C /usr/local --owner root --group root --no-same-owner && \
    rm "spark.tgz" && \
    ln -s "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MAJOR_VERSION}" "${SPARK_HOME}"

# Configure Spark
ENV SPARK_OPTS="--driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info"
ENV PATH="${PATH}:${SPARK_HOME}/bin"

# Install native Hadoop libraries
RUN wget -qO "hadoop.tgz" "https://www.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz"; \
    tar xzf "hadoop.tgz" -C /opt/ --owner root --group root --no-same-owner && \
    rm "hadoop.tgz"


RUN ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop; \
    mkdir /opt/hadoop-$HADOOP_VERSION/logs

ENV HADOOP_HOME="/opt/hadoop-${HADOOP_VERSION}"
ENV HADOOP_CONF_DIR=/etc/hadoop
ENV MULTIHOMED_NETWORK=1
ENV PATH="${PATH}:${HADOOP_HOME}/bin/"
ENV HADOOP_COMMON_LIB_NATIVE_DIR="${HADOOP_HOME}/lib/native"
ENV HADOOP_OPTS="${HADOOP_OPTS} -Djava.library.path=${HADOOP_HOME}/lib/native"
ENV LD_LIBRARY_PATH="${HADOOP_HOME}/lib/native"

# Python and poetry installation
USER $USER
ENV HOME="/home/$USER"

ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"

# Install PyEnv
RUN curl https://pyenv.run | bash
RUN pyenv install ${PYTHON_VERSIONS} && pyenv global ${PYTHON_VERSIONS}

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.in-project true
