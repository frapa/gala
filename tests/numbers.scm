;; These are tests for the 'number' non-terminal
(number ; <- This is the non-terminal's name

 ;; Following the name are pairs of input string and expected output. The
 ;; output is either the keyword 'pass', the keyword 'fail' or an AST. The AST
 ;; specifies the structure of the expected tree, the names of the nodes and
 ;; the individual characters. If you don't want to specify the whole tree,
 ;; just use the wild-card symbol '*' for the portion of the tree you want to
 ;; skip.

 "123" ; <- This is the input
 (decimal *) ; <- This is the expected output

 "0" ; 
 (decimal *) ;

 "98.678" ; 
 (decimal *) ;

 "98.654e3" ; 
 (decimal *) ;

 "01234" ; 
 (octal *) ;

 "0b101" ; 
 (binary *) ;

 "0x10fe" ; 
 (hex *) ;

 "0x10fA" ; 
 (hex *) ;

 ;; Invalid 
 "12s3" ;
  fail ;

 "012s3" ;
  fail ;

 "0b12s3" ;
  fail ;

 "0x12s3" ;
  fail ;

 "012368" ;
  fail ;

 "0b2" ;
  fail ;

 "0x12368g" ;
  fail ;

 "01236.213" ;
  fail ;
  
 "0b101.101" ;
  fail ;

 "0x123d6.21d3" ;
  fail ;

 "01236.213e5" ;
  fail ;

 "0b11.10e11" ;
  fail ;

 "0xd36.21f3e5c" ;
  fail ;
)
