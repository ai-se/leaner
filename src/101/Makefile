#  __   ___ ___ ___  ___  __  
# |__) |__   |   |  |__  |__) 
# |__) |___  |   |  |___ |  \.     
#                           
#  __   __   __   ___         
# /  ` /  \ |  \ |__          
# \__, \__/ |__/ |___.         

Wiki=../../../leaner.wiki
pys=$(subst .py,.md,$(shell ls *.py;))
mds=$(Wiki)/$(subst .md ,.md $(Wiki)/,$(pys))

.PHONY: all typo commit update status giting timm publish tests test

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
  BEGIN           { First = 1      
                    In = 1}         
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

export testsawk
export p2md

all: publish typo

typo: publish gitting
	- git status
	- git commit -am "stuff"
	- git push origin master

commit: publish gitting
	- git status
	- git commit -a
	- git push origin master

update:; - git pull origin master
status:; - git status

gitting:
	@git config --global credential.helper cache
	@git config credential.helper 'cache --timeout=3600'

timm:
	@git config user.name "Tim Menzies" 
	@git config user.email "tim.menzies@gmail.com"

publish: $(mds) wikiCommits
	
wikiCommits:
	cp -p wiki/* $(Wiki)
	$(shell bash $(Wiki)/commits $(Wiki)  ;)

tests: 
	@$(foreach f,$(shell ls *eg.py), python $f;)

tmp :
	mkdir tmp

tmp/p2md.awk: tmp  
	 @echo "$$p2md" > $@
tmp/tests.awk: tmp
	 @echo "$$testsawk" > $@

$(Wiki)/%.md: %.py tmp/p2md.awk
	@awk -f tmp/p2md.awk $< > $@;
	@echo making $@

test: tmp/tests.awk
	@$(MAKE) tests | awk -f $<
