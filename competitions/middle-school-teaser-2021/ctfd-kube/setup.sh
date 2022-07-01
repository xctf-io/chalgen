helm install -n challenges -f mariadb-config.yaml mariadb bitnami/mariadb
helm install -n challenges redis bitnami/redis
