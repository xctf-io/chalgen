build:
	docker build . -t shell_server-8729873248519

run: build
	docker run -p 8080:80 shell_server-8729873248519

clean:
	docker rm -f -v shell_server-8729873248519

generate-img:
	docker run -d --name shell_server-8729873248519 shell_server-8729873248519:latest
	docker export shell_server-8729873248519 -o vm.tar.gz
	docker stop shell_server-8729873248519