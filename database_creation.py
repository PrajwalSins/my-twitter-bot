import pymongo
from pymongo import MongoClient

client = MongoClient()
database = client['programming_terms']
terms = database['programming_related_terms']

numeric=['%1', '%1', '\1', '.net', '/n', '/r' ,'/t', '1gl','2gl','3gl','4gl','5gl']
a=['algorithm','abend','absolute','acess','address','acm','action','analysis','actionscript','activex','ada','add','advanced','aggregation','agile','alert','algol','allocate','altair','ambient','aqp','api','applet','argument','arithometic','array','asp','ascii','aspi','assembler','assembly','associative','autohockey','automata','automated','automation','agreement','associativity','algebra']
b=['boolean','backoff','book','backend','bracket','backface','background','backpropagation','batch','bean','bcpl','beanshell','binary','bit','bitwise','block','bind','bom','bool','bracket','branch','brooks','browse','bug','bugfairy','build','bytecode','business','bin']
c=['coding','culling','connectivity','carlo','cycle','collection','computer','c','c+','c#','camelcase','cc','captured','chaos','character','char','code','class','classpath','closure','clr','cobol','cocoa','codepage','command','comment','common','compiler','complementarity','concatenation','commutative','concat','concurrency','conditional','constructor','constant','content','control','cpan','cpl','crapplet','cs','csat','css','curly','cvs','cywgin','curry','chi','chaining','compressor','condition','counter','calculus']
d=['development','driven','data','dart','debug','dead','datalog','debugger','debugging','declaration','declarative','declare','decompiler','diagram','darkbasic','dde','decrement','deductive','database','die','diff','direct','discrete','dissembler','div','django','dml','delimiter','dense','dereference','developer','dom','do','dreagon','dribbleware','dump','dword','dylan','dynamic','disclosure','descriptor','definition']
e=['element','encoding','evaluation','editor','expression','editor','exe','eclipse','ecmascript','eight','ellipsis','else','elseif','embedded','encapsulation','endian','endless','eof','epoch','eq','equal','error','esac','escape','eval','event','exec','exception','exponential','exists','environment','extraction','engineering']
f=['file','flow','for','foreach','f','f#','flag','fifth','first','flat','forth','fortran','framework','frontend','full','floating','function','fuzz','functional','four','framework']
g=['gateway','generation','gang','garbage','gaussian','gcc','ge','general','genetic','github','glitch','glob','glue','go','gotogigo','gpl','grasshopper','gt','gtk','gw','grammar']
h=['handler','handling','haskell','hard','hash','heap','hello','heuristic','hex','hdml','hiew','high','html','hungranian','hwclock','hypertext']
i=['if','ide','iteration','immutable','imparitive','implicit','increment','inherent','inheritance','indireratedection','inline','input','instance','instructions','int','integer','integerated','instantiation','intellij','intermediate','interpreted','interpreter','invalid','ioccc','ipc','isapi','iteration']
j=['job','js','javascript','java','javabean','javac','javascriptcore','jbuilder','jcl','jdbc','jdk','javafx','jhtml','jscript','jvm','json','jsr','julia','jsp','jni','jre','jit','jil']
k=['karel','kit','kludge','kluge']
l=['language','loop','level','life','label','lambda','lexical','lexicon','linker','lisp','live','literal','llvm','local','logical','logo','lookup','loony','loophole','low','library','lt','lua','lut','logic']
m=['methods','manifesto','model','mitigation','matrix','markup','matalab','machine','magic','map','math','mbean','memoization','mercurial','metacharacter','metaclass','metalanguage','method','metro','middleware','mod','module','modulo','monkey','monte','multi','msdn','msvc','mumps','mutex','microsoft','memory']
n=['neural','network','notation','net','native','natural','nbsp','nda','nested','newline','nil','nim','node','nodelist','noncontiguous','nonexecutable','null','number','native']
o=['operator','occlusion','oriented','operation','optimum','object','objective','obfuscated','ocaml','octave','odbc','oop','one','onmouseover','opcode','open','opengl','operand','or','overflow','overload']
p=['programming','pointer','problem','purpose','pointer','practical','phases','package','parenthesis','pickiling','parse','pascal','pastebin','pdl','pear','perl','persistent','personaljava','php','phrase','pipe','pixel','picojava','pod','polymorphism','pop','positional','parameter','private','procedural','procedure','process','program','programable','programmer','pseudo','pseudocode','pseudolanguage','public','push','python','pythonic']
q=['queens','quotes','qi','qt','quick']
r=['refactoring','reporting','return','r','race','racket','random','rcs','rdf','react','real','recompile','recursion','recursive','regex','regular','reia','rlational','religion','rem','remark','repeat','repl','reserved','rad','repeat','resource','revision','rom','routine','routing','rpg','ruby','run','rust']
s=['statement','studio','search','sharp','set','science','satisfiability','system','signedness','spl','sparsity','spooling','stack','standard','statement','stdin','strong','subroutine','submit','stylesheet','subscript','substring','superclass','switch','syntactic','sugar','syntax','subprogram','stimulated','single','step','smalltalk','smil','socket','software','source','sourceforge','snippet','soap','sparse','source','sequence','stack','structure','shader','seed','spahetti','safe','sandbox','scala','schema','scheme','scratch','sdk','second','section','security','segfault','separator','server','sequence','servlet','sgml','shebang','shell','sscript','shift','short']
t=['type','tracking','toch','testing','table','tag','tools','time','tal','tuple','tcl','tk','ternary','third','thread','theoritical','thunk','token','toolbox','true','transcompiler','trunk','turbo','turing']
u=['urnary','undefined','underflow','unescape','unit','unshift']
v=['violation','variable','value','var','variable','vb','vector','vhdl','vim','visual','void','virtual']
w=['world','word','waterfall','web','webgl','while','whole','wml','workspace']
x=['xml','xna','xor','xoxo','xsl','xslt']
y=['yaml']
z=['zbuffering','zombie']										
										
term_list = [
	{ 'numbers': numeric},
	{ 'a': a},
	{ 'b': b},
	{ 'c': c},
	{ 'd': d},
	{ 'e': e},
	{ 'f': f},
	{ 'g': g},
	{ 'h': h},
	{ 'i': i},
	{ 'j': j},
	{ 'k': k},
	{ 'l': l},
	{ 'm': m},
	{ 'n': n},
	{ 'o': o},
	{ 'p': p},
	{ 'q': q},
	{ 'r': r},
	{ 's': s},
	{ 't': t},
	{ 'u': u},
	{ 'v': v},
	{ 'w': w},
	{ 'x': x},
	{ 'y': y},
	{ 'z': z}
]										

data_id = terms.insert_many(term_list)
print(data_id.inserted_ids)							
										

