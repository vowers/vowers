# vertica

docker run --restart=always  -p 5433:5433 -d -v /home/vertica/vertica_data:/home/dbadmin/docker  jbfavre/vertica:latest

docker rmi $( docker images | grep os-dsmart )

docker rmi $(docker images -q -f dangling=true)

docker run --name q21701_postgres -v /data/postgres:/var/lib/postgresql -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres

# 移除无用镜像

docker rmi $(docker images -q -f dangling=true)
