build:
	@docker build . -t facebook-django-309864205 -q

run: build
	@docker run -p 8081:8000 facebook-django-309864205

clean:
	@docker rm -f -v facebook-django-309864205

generate-img:
	@docker run -d --name facebook-django-309864205 facebook-django-309864205:latest
	@docker export facebook-django-309864205 -o vm.tar.gz
	@docker rm facebook-django-309864205
	@docker rmi facebook-django-309864205