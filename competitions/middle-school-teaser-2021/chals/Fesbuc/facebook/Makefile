build:
	@docker build . -t facebook-django-8748560610269 -q

run: build
	@docker run -p 8081:8000 facebook-django-8748560610269

clean:
	@docker rm -f -v facebook-django-8748560610269

generate-img:
	@docker run -d --name facebook-django-8748560610269 facebook-django-8748560610269:latest
	@docker export facebook-django-8748560610269 -o vm.tar.gz
	@docker rm facebook-django-8748560610269
	@docker rmi facebook-django-8748560610269