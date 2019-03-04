import tweepy
import time
from googlesearch import search
import nltk
from nltk.corpus import stopwords
import pymongo
from pymongo import MongoClient
from spellchecker import SpellChecker
import pymongo
from pymongo import MongoClient

CONSUMER_KEY = 'osDCxy9STdyR9ImpAt9GQNN5c'
CONSUMER_SECRET = 'W5VxgaTzZro9aUMYTj9WMny5IBpDaZEWZ7jngw806N1ndpTLDd'
ACCESS_KEY = '1087023067589570565-lnSoT1rKcYQ8Ba4CJBjp2MX02kh5q5'
ACCESS_SECRET = 'CCzzFlPHrbNYjGgb00WsekI9ehT9fZupJNnu0OFrMNo5k'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
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


def retrieve_last_seen_id():
	f_read = open('last_seen.txt', 'r')
	last = f_read.read()
	f_read.close()
	x = int(last)
	return x

def store_last_seen_id(last_seen_id):
	s = str(last_seen_id)
	f_write = open('last_seen.txt', 'w')
	f_write.write(s)
	f_write.close()
	return

def analyze(topic):
	spell_check = SpellChecker()
	stop_words = stopwords.words('english')
	full_sentence = topic.split(" ")
	for i in range(0, len(full_sentence)):
		full_sentence[i] = spell_check.correction(full_sentence[i])
	filtered_sentence=[]
	for word in full_sentence:
		if word not in stop_words:
			filtered_sentence.append(word)
	match_percent = search_database(filtered_sentence)
	if(match_percent >= 90):
		return True
	else:
		return False
		
def search_database(filtered_sentence):
	client = MongoClient('localhost', 27017)
	database = client['programming_terms']
	terms = database['programming_related_terms']
	counter, total = 0, len(filtered_sentence)
	for word in filtered_sentence:
		character = word[0]
		querry = { character: word}
		resulting_dictionary = terms.find(querry)
		if (word in resulting_dictonary[character]) == True:
			counter +=1
	result_percent = (counter/total)*100
	return result_percent

def internet_search(topic):
	search_results = []
	for url in search(topic, tld = 'com', lang = 'en', stop = 5):
			search_results.append(url)
	text  = 'Please refer to following links:=>' + '\n1 ' + search_results[0] + '\n2 ' + search_results[1] + '\n3 ' + search_results[2] + '\n4 '+ search_results[3] + '\n5 ' + search_results[4] 
	return text

def reply_to_tweets():
	last_seen_id = retrieve_last_seen_id()
	mentions = api.mentions_timeline(last_seen_id)
	for mention in reversed(mentions):
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id)
		topic = mention.text.lower()
		validity = analyze(topic)
		if(validity == True):	
			results = internet_search(topic)  
			api.update_status('@' + mention.user.screen_name + results, mention.id)
		elif(validity == False):
			api.update_status('@' + mention.user.screen_name + "Sorry cannot find anything,Please try something else related to programming.", mention.id)	

while True:
	reply_to_tweets()
	time.sleep(15)
