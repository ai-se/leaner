url="https://github.com/ai-se/leaner"
py=$(shell cd src; ls *.py)
md=doc/$(subst .md ,.md doc/,$(subst .py,.md,$(py)))
tests=$(shell cd src; ls *eg.py)

make=cd src; $(MAKE) --no-print-directory

all: publish commit

test:
	@$(make)  test

tests:
	@$(make)  tests

typo: publish
	- git status
	- git commit -am "stuff"
	- git push origin master

commit: publish
	- git status
	- git commit -a
	- git push origin master

update:
	- git pull origin master

status:
	- git status

doc/%.md : src/%.py
	@bash etc/py2md $<  "$(url)" > $@
	git add $@

README.md : etc/readmeHeader etc/readmeFooter  $(md) etc/toc1.awk
	@cat etc/readmeHeader > $@
	@$(foreach f,$(py), awk -f etc/toc1.awk src/$f >> $@;)
	@cat etc/readmeFooter  >> $@
	git add $@

publish: $(md) README.md 
