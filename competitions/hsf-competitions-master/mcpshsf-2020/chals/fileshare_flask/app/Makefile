build:
	docker build . -t fileshare-flask-8781557909559

run: build
	docker run -p 8081:8000 fileshare-flask-8781557909559

clean:
	docker rm -f -v fileshare-flask-8781557909559

generate-img:
	docker run -d --name fileshare-flask-8781557909559 fileshare-flask-8781557909559:latest
	docker export fileshare-flask-8781557909559 -o vm.tar.gz
	docker stop fileshare-flask-8781557909559