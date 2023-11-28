build:
	@docker build  --platform linux/amd64 . -t jekyll-blog-8792530897949 -q

run: build
	@docker run -p 8081:80 jekyll-blog-8792530897949

clean:
	@docker rm -f -v jekyll-blog-8792530897949

generate-img:
	docker run -d --name jekyll-blog-8792530897949 jekyll-blog-8792530897949:latest
	docker export jekyll-blog-8792530897949 -o vm.tar.gz
	docker stop jekyll-blog-8792530897949