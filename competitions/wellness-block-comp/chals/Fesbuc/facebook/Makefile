build:
	@docker build . -t facebook-django-8751957575317

run: build
	@docker run -p 8081:8000 facebook-django-8751957575317

clean:
	@docker rm -f -v facebook-django-8751957575317

generate-img:
	@docker run -d --name facebook-django-8751957575317 facebook-django-8751957575317:latest
	@docker export facebook-django-8751957575317 -o vm.tar.gz
	@docker rm facebook-django-8751957575317
	@docker rmi facebook-django-8751957575317