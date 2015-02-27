## Begin config

WikiName=  leaner.wiki#
WikiDir =  ../../..#
Wiki    =  $(WikiDir)/$(WikiName)
WikiGit =  https://github.com/ai-se/leaner.wiki.git#
Me      =  Tim Menzies#
MyEmail =  tim.menzies@gmail.com#
MyHeader1= [Home](Home) [[home.png]] | [Data](Data) [[data.png]] | Leaner Data Mining |#
MyHeader2= | --- | --- | --- |#

## End config
## (everything from here down should be generic)

#################################################

pys  = $(subst .py,.md,$(shell ls *.py;))#
mds  = $(Wiki)/$(subst .md ,.md $(Wiki)/,$(pys))#

.PHONY: all typo commit update status giting reset \
        timm save dirs publish tests test wikiCommits

define commits
HERE=$${1:-$$PWD}
cd $$HERE
git config --global credential.helper cache
git config credential.helper 'cache --timeout=3600'
git config user.name "$(Me)"
git config user.email "$(MyEmail)"
git add *
git commit -am "stuff"
git push origin master
endef 

define testsawk
  BEGIN       { yes=no=0       }	
              { m="."          }	
  /True/      { yes += gsub("True","") ; m = "+" } 
  /False/     { no  += gsub("False",""); m = "X" } 
              { printf m       } 
  ! (NR % 50) { print ""}
  END         { print "\ntests passed",yes,"failed",no }
endef

define p2md
  BEGIN           {
         print ""
         print "$(MyHeader1)"  
         print "$(MyHeader2)"
         print ""
         First = 1      
         In = 1
  }         
  /^"""</,/^>"""/ {  next } 
  /^"""/          {  In = 1 - In       
                     if (In)            
                       print "````python"
                     else          
                       if (First)   
                         First = 0   
                       else     
                         print "````"  
                     next }       
  ! First { print $$0 }       
  END     { if (In) print "````"  }
endef

export commits
export testsawk
export p2md

all: publish typo

typo: publish gitting
	git status
	git commit -am "stuff"
	git push origin master

commit: publish gitting save

save:
	@- git status
	@- git commit -a
	@- git push origin master

update:; @- git pull origin master
status:; @- git status

gitting:
	@git config --global credential.helper cache
	@git config credential.helper 'cache --timeout=3600'

timm:
	@git config user.name "$(Me)" 
	@git config user.email "$(MyEmail)"

reset:
	cd $(WikiDir); rm -rf $(WikiName); git clone $(WikiGit)

publish: $(mds) wikiCommits 

wikiCommits: tmp/commits
	rsync -u  wiki/* $(Wiki) # cause cp -u not in Mac/OS
	bash tmp/commits $(Wiki) 

tests: 
	@$(foreach f,$(shell ls *eg.py), python $f;)


tmp     : 
	@echo "/tmp" > .gitignore
	@- mkdir -p $@

tmp/p2md.awk  : tmp ; echo "$$p2md" > $@
tmp/tests.awk : tmp ; @echo "$$testsawk" > $@
tmp/commits   : tmp ; @echo "$$commits" > $@

$(Wiki)/%.md: %.py tmp/p2md.awk
	@awk -f tmp/p2md.awk $< > $@;

test: tmp/tests.awk
	@$(MAKE) tests | awk -f $<
