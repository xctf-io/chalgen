build:
	@docker build . -t jekyll-blog-8793342933677 -q

run: build
	@docker run -p 8081:80 jekyll-blog-8793342933677

clean:
	@docker rm -f -v jekyll-blog-8793342933677

generate-img:
	@docker run -d --name jekyll-blog-8793342933677 jekyll-blog-8793342933677:latest
	@docker export jekyll-blog-8793342933677 -o vm.tar.gz
	@docker rm jekyll-blog-8793342933677
	@docker rmi jekyll-blog-8793342933677