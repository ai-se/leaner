BEGIN   { yes=no=0       }	
        { m="."          }	
/True/  { yes++; m = "+" } 
/False/ { no++;  m = "-" } 
        { printf m       } 
END     { print "\ntests passed",yes,"failed",no }

