;; These are tests for the 'Grammar' non-terminal
(string ; <- This is the non-terminal's name

 ;; Following the name are pairs of input string and expected output. The
 ;; output is either the keyword 'pass', the keyword 'fail' or an AST. The AST
 ;; specifies the structure of the expected tree, the names of the nodes and
 ;; the individual characters. If you don't want to specify the whole tree,
 ;; just use the wild-card symbol '*' for the portion of the tree you want to
 ;; skip.

 "''" ; <- This is the input
 (string *) ; <- This is the expected output

 "\"\"" ;
 (string *) ;

 "'ciao come va?'" ;
 (string *) ;

 "\"ciao come va?\"" ;
 (string *) ;

 "'\"bello\"'" ;
 (string *) ;

 "\"che c'é?\"" ;
 (string *) ;

 "'che c'é?'" ;
 fail ;

 "'che c\\\'é?'" ;
 (string *) ;

 "\"questa è una virgoletta: \"\"" ;
 fail ;

 "\"questa è una virgoletta: \\\"\"" ;
 (string *) ;

 "'\\'" ;
 fail ;

 "'\\\\'" ;
 (string *) ;

 "'\x62fd'" ;
 (string *) ;
)
