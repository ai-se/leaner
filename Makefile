url="https://github.com/ai-se/leaner/blob/master"

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
	@bash etc/py2md $< $(url) > $@
	git add $@

README.md : etc/readme etc/license.md $(md) etc/toc1.awk
	@cat $< > $@
	@printf "\n\n## Contents\n\n" >> $@
	@$(foreach f,$(py),\
		gawk -f etc/toc1.awk src/$f >> $@;)
	@cat etc/license.md  >> $@
	git add $@

publish: $(md) README.md 
