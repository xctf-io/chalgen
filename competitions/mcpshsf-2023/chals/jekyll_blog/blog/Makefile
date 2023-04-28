build:
	@docker build . -t jekyll-blog-302390121 -q

run: build
	@docker run -p 8081:80 jekyll-blog-302390121

clean:
	@docker rm -f -v jekyll-blog-302390121

generate-img:
	@docker run -d --name jekyll-blog-302390121 jekyll-blog-302390121:latest
	@docker export jekyll-blog-302390121 -o vm.tar.gz
	@docker rm jekyll-blog-302390121
	@docker rmi jekyll-blog-302390121