build:
	@docker build . -t facebook-django-8785501671577 -q

run: build
	@docker run -p 8081:8000 facebook-django-8785501671577

clean:
	@docker rm -f -v facebook-django-8785501671577

generate-img:
	docker run -d --name facebook-django-8785501671577 facebook-django-8785501671577:latest
	docker export facebook-django-8785501671577 -o vm.tar.gz
	docker stop facebook-django-8785501671577