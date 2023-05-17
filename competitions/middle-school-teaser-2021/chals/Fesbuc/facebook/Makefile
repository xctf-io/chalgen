build:
	@docker build . -t facebook-django-314927041 -q

run: build
	@docker run -p 8081:8000 facebook-django-314927041

clean:
	@docker rm -f -v facebook-django-314927041

generate-img:
	@docker run -d --name facebook-django-314927041 facebook-django-314927041:latest
	@docker export facebook-django-314927041 -o vm.tar.gz
	@docker rm facebook-django-314927041
	@docker rmi facebook-django-314927041