build:
	@docker build . -t static_site-8739167597827 -q

run: build
	@docker run -p 8080:80 static_site-8739167597827

clean:
	@docker rm -f -v static_site-8739167597827

generate-img:
	@docker run -d --name static_site-8739167597827 static_site-8739167597827:latest
	@docker export static_site-8739167597827 -o vm.tar.gz
	@docker rm static_site-8739167597827
	@docker rmi static_site-8739167597827