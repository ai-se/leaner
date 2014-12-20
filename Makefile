
url="https://github.com/ai-se/leaner/blob/master"

py=$(shell cd src; ls *.py)
md=$(subst src/,,$(subst .py,.md,$(py)))
tests=$(shell cd src; ls *eg.py)

all: publish commit

test:
	@$(MAKE) tests | gawk ' \
		BEGIN { yes=no=0} \
                {m="."} \
                /True/  {yes++; m = "+"} \
                /False/ {no++;  m = "-"} \
                {printf m} \
		END {print "\ntests passed",yes,"failed",no}'

tests:
	cd src; $(foreach f,$(tests), python $f;)

typo:
	- git status
	- git commit -am "stuff"
	- git push origin master

commit:
	- git status
	- git commit -a
	- git push origin master

update:
	- git pull origin master

status:
	- git status

./%.md : src/%.py
	@bash etc/py2md $< $(url) > $@
	git add $@

README.md : etc/readme.md etc/license.md $(md) etc/toc1.awk
	@cat $< > $@
	@printf "\n\n## Contents\n\n" >> $@
	@$(foreach f,$(py),\
		gawk -f etc/toc1.awk src/$f >> $@;)
	@cat etc/license.md  >> $@
	git add $@

publish: $(md) README.md 
