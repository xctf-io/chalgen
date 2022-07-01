export DATABASE_URL=${DATABASE_URL:=sqlite:///../data/database.db}
export PORT=${PORT:=3005}
export SECRET_KEY=${SECREY_KEY:=asdfasdfsadf}
foreman start
