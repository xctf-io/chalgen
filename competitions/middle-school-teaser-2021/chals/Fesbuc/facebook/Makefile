build:
	@docker build . -t facebook-django-8776786791589 -q

run: build
	@docker run -p 8081:8000 facebook-django-8776786791589

clean:
	@docker rm -f -v facebook-django-8776786791589

generate-img:
	@docker run -d --name facebook-django-8776786791589 facebook-django-8776786791589:latest
	@docker export facebook-django-8776786791589 -o vm.tar.gz
	@docker rm facebook-django-8776786791589
	@docker rmi facebook-django-8776786791589