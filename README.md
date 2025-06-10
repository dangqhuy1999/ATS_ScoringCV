# Run MySQL and ubuntu code python 


docker network create my_network


docker rm -f custom_mysql && 
docker run -d --name custom_mysql --network my_network 
-e MYSQL_ROOT_PASSWORD=rootpassword123 
-e MYSQL_DATABASE=cv 
-e MYSQL_USER=user_cv 
-e MYSQL_PASSWORD=userpass123 
-p 3306:3306 
lamianguyen99/my_custom_mysql8:v2

docker run -it --rm 
  --name ubuntu_client 
  --network my_network 
  -p 8501:8501 
  lamianguyen99/my_custom_ubuntu:v2 
  bash