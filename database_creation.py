import pymongo
from pymongo import MongoClient

client = MongoClient()
database = client['programming_terms']
terms = database['programming_related_terms']

numeric=['%1', '%1', '\1', '.net', '/n', '/r' ,'/t', '1gl','2gl','3gl','4gl','5gl']
A=['algorithm','abend','absolute','acess','address','acm','action','analysis','actionscript','activex','ada','add','advanced','aggregation','agile','alert','algol','allocate','altair','ambient','aqp','api','applet','argument','arithometic','array','asp','ascii','aspi','assembler','assembly','associative','autohockey','automata','automated','automation','agreement','associativity','algebra']
B=['boolean','backoff','book','backend','bracket','backface','background','backpropagation','batch','bean','bcpl','beanshell','binary','bit','bitwise','block','bind','bom','bool','bracket','branch','brooks','browse','bug','bugfairy','build','bytecode','business','bin']
C=['coding','culling','connectivity','carlo','cycle','collection','computer','c','c+','c#','camelcase','cc','captured','chaos','character','char','code','class','classpath','closure','clr','cobol','cocoa','codepage','command','comment','common','compiler','complementarity','concatenation','commutative','concat','concurrency','conditional','constructor','constant','content','control','cpan','cpl','crapplet','cs','csat','css','curly','cvs','cywgin','curry','chi','chaining','compressor','condition','counter','calculus']
D=['development','driven','data','dart','debug','dead','datalog','debugger','debugging','declaration','declarative','declare','decompiler','diagram','darkbasic','dde','decrement','deductive','database','die','diff','direct','discrete','dissembler','div','django','dml','delimiter','dense','dereference','developer','dom','do','dreagon','dribbleware','dump','dword','dylan','dynamic','disclosure','descriptor','definition']
E=['element','encoding','evaluation','editor','expression','editor','exe','eclipse','ecmascript','eight','ellipsis','else','elseif','embedded','encapsulation','endian','endless','eof','epoch','eq','equal','error','esac','escape','eval','event','exec','exception','exponential','exists','environment','extraction','engineering']
F=['file','flow','for','foreach','f','f#','flag','fifth','first','flat','forth','fortran','framework','frontend','full','floating','function','fuzz','functional','four','framework']
G=['gateway','generation','gang','garbage','gaussian','gcc','ge','general','genetic','github','glitch','glob','glue','go','gotogigo','gpl','grasshopper','gt','gtk','gw','grammar']
H=['handler','handling','haskell','hard','hash','heap','hello','heuristic','hex','hdml','hiew','high','html','hungranian','hwclock','hypertext']
I=['if','ide','iteration','immutable','imparitive','implicit','increment','inherent','inheritance','indireratedection','inline','input','instance','instructions','int','integer','integerated','instantiation','intellij','intermediate','interpreted','interpreter','invalid','ioccc','ipc','isapi','iteration']
J=['job','js','javascript','java','javabean','javac','javascriptcore','jbuilder','jcl','jdbc','jdk','javafx','jhtml','jscript','jvm','json','jsr','julia','jsp','jni','jre','jit','jil']
K=['karel','kit','kludge','kluge']
L=['language','loop','level','life','label','lambda','lexical','lexicon','linker','lisp','live','literal','llvm','local','logical','logo','lookup','loony','loophole','low','library','lt','lua','lut','logic']
M=['methods','manifesto','model','mitigation','matrix','markup','matalab','machine','magic','map','math','mbean','memoization','mercurial','metacharacter','metaclass','metalanguage','method','metro','middleware','mod','module','modulo','monkey','monte','multi','msdn','msvc','mumps','mutex','microsoft','memory']
N=['neural','network','notation','net','native','natural','nbsp','nda','nested','newline','nil','nim','node','nodelist','noncontiguous','nonexecutable','null','number','native']
O=['operator','occlusion','oriented','operation','optimum','object','objective','obfuscated','ocaml','octave','odbc','oop','one','onmouseover','opcode','open','opengl','operand','or','overflow','overload']
P=['programming','pointer','problem','purpose','pointer','practical','phases','package','parenthesis','pickiling','parse','pascal','pastebin','pdl','pear','perl','persistent','personaljava','php','phrase','pipe','pixel','picojava','pod','polymorphism','pop','positional','parameter','private','procedural','procedure','process','program','programable','programmer','pseudo','pseudocode','pseudolanguage','public','push','python','pythonic']
Q=['queens','quotes','qi','qt','quick']
R=['refactoring','reporting','return','r','race','racket','random','rcs','rdf','react','real','recompile','recursion','recursive','regex','regular','reia','rlational','religion','rem','remark','repeat','repl','reserved','rad','repeat','resource','revision','rom','routine','routing','rpg','ruby','run','rust']
S=['statement','studio','search','sharp','set','science','satisfiability','system','signedness','spl','sparsity','spooling','stack','standard','statement','stdin','strong','subroutine','submit','stylesheet','subscript','substring','superclass','switch','syntactic','sugar','syntax','subprogram','stimulated','single','step','smalltalk','smil','socket','software','source','sourceforge','snippet','soap','sparse','source','sequence','stack','structure','shader','seed','spahetti','safe','sandbox','scala','schema','scheme','scratch','sdk','second','section','security','segfault','separator','server','sequence','servlet','sgml','shebang','shell','sscript','shift','short']
T=['type','tracking','toch','testing','table','tag','tools','time','tal','tuple','tcl','tk','ternary','third','thread','theoritical','thunk','token','toolbox','true','transcompiler','trunk','turbo','turing']
U=['urnary','undefined','underflow','unescape','unit','unshift']
V=['violation','variable','value','var','variable','vb','vector','vhdl','vim','visual','void','virtual']
W=['world','word','waterfall','web','webgl','while','whole','wml','workspace']
X=['xml','xna','xor','xoxo','xsl','xslt']
Y=['yaml']
Z=['zbuffering','zombie']										
										
term_list = [
	{ 'numbers': numeric},
	{ 'a': A},
	{ 'b': B},
	{ 'c': C},
	{ 'd': D},
	{ 'e': E},
	{ 'f': F},
	{ 'g': G},
	{ 'h': H},
	{ 'i': I},
	{ 'j': J},
	{ 'k': K},
	{ 'l': L},
	{ 'm': M},
	{ 'n': N},
	{ 'o': O},
	{ 'p': P},
	{ 'q': Q},
	{ 'r': R},
	{ 's': S},
	{ 't': T},
	{ 'u': U},
	{ 'v': V},
	{ 'w': W},
	{ 'x': X},
	{ 'y': Y},
	{ 'z': Z}
]										

data_id = terms.insert_many(term_list)
print(data_id.inserted_ids)							
										

