;; These are tests for the 'number' non-terminal
(comment ; <- This is the non-terminal's name

 ;; Following the name are pairs of input string and expected output. The
 ;; output is either the keyword 'pass', the keyword 'fail' or an AST. The AST
 ;; specifies the structure of the expected tree, the names of the nodes and
 ;; the individual characters. If you don't want to specify the whole tree,
 ;; just use the wild-card symbol '*' for the portion of the tree you want to
 ;; skip.

 "test" ; <- This is the input
 fail ; <- This is the expected output

 "// sasd" ;
 pass ;

 "/* sasd */" ;
 pass ;
)
