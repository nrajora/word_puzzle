from itertools import islice,zip_longest
from datetime import * 
import random
import os, sys

# Sample dictionary with words and multiple comma-separated meanings
word_dict = {
'Affluent':'rich,prosperous,wealthy,thriving',
'Destitute':'poor,penniless,needy',
'Naïve':'simple,innocent,inexperienced,novice,beginner,trainee,apprentice',
'Leer':'stare,ogle',
'Jeer':'mock,taunt,ridicule,insult,scorn',
'Tarmac':'tar,pitch,runway',
'Alter':'change,modify,amend',
'Flume':'torrent,waterfall',
'Sew':'stich,embroidery,seam,hem',
'Rover':'traveller,vagrant,vagabond,nomad,wanderer,tramp',
'Perm':'curl,wave,fizz',
'Pottery':'clay,ceramics,earthenware,china,dishes,plates,porcelain',
'Downpour':'rainstorm,deluge,heavy,shower',
'Torrent':'gush,flood,surge,deluge',
'Reap':'grow,acquire,procure,cultivate',
'Rapid':'fast,speed,hasty,hurried,swift',
'Rattle':'bang,clatter,din,clamour',
'Cuddle':'embrace,clasp,hold,fondle,snuggle',
'Arena':'stadium,pitch,ground',
'Apex':'summit,peak,top,zenith,pinnacle',
'Idle':'motionless,stationary,indolent,sluggish,lazy',
'Idol':'star,celebrity,hero',
'Tendon':'muscle,ligament,cartilage',
'Fault':'error,responsibility,liability,blunder',
'Tremor':'shake,turbulence,tremble,quake,shock',
'Steeple':'tower,highest,point,of,the,church',
'Vicar':'priest,monk,preacher,minister,parson',
'Generous':'lavish,plenty,substantial,liberal,spendthrift',
'Selfish':'self-centred,egoistic,greedy',
'Moor':'grasslands,hill,upland,moorland,heath,hillock,lea',
'Witty':'funny,clever,droll,amusing,humorous,lively',
'Umpire':'referee,mediator',
'Jockey':'rider,equestrian',
'Bloom':'blossom,flower,flourish,thrive,grow,develop',
'Restore':'repair,fix,rebuild',
'Fare':'cost,fee,price,tariff,toll',
'Habit':'custom,routine,practice,tradition,pattern',
'Drudge':'slave,toil,worker,labour,slog',
'Dodge':'avoid,escape,duck,evade,elude',
'Perform':'act,play',
'Dome':'vault,cupola,roof,ceiling',
'Trawl':'scan,rummage,seek,probe,investigate,hunt,search,scrutinising',
'Shaft':'tube,channel,trough',
'Thrust':'shove,push,prod,plunge,stab,insertion',
'Fraction':'part,fragment,piece,portion,segment,element',
'Accelerate':'hurry,hasten,quicken,rush',
'Tepid':'lukewarm',
'Elaborate':'extravagant,ornate,decorative,elegant',
'Hostile':'unfriendly,antagonistic,aggressive',
'Thaw':'defrost,melt,liquify,soften',
'Trim':'prune,crop,cut,clip',
'Stain':'tinge,dye,colour,tint,pigment',
'Smear':'mark,blotch,stain,insult,slur',
'Deter':'stop,discourage,prevent,frighten',
'Inferno':'fire,blaze,furnace,firestorm',
'Hank':'coil,reel,length,bundle,ball',
'Strand':'thread,element,component,part,filament,fibre',
'Recent':'modern,fresh,latest,current,novel',
'Latter':'end,final,concluding,later',
'Former':'previous,past,ex,last,prior',
'Pursue':'chase,hunt,trail,track,tail,shadow,follow',
'Fragile':'delicate,flimsy,brittle,breakable,frail,puny',
'Aroma':'smell,fragrance,perfume,scent,whiff,odour',
'Blurt':'cry,utter,announce,revel,divulge',
'Chant':'sing,tune,hymn,mantra,recite,repeat',
'Limb':'branch,bough,appendage',
'Grit':'gravel,shingle,sand,dirt,pebbles,stones',
'Wind':'gale,gust,breeze',
'Tempest':'storm,hurricane,cyclone,gale',
'Meadows':'fields,pastures,paddocks,(where-horses-are-trained),leas',
'Bleach':'whiten,lighten,decolourize,blanch',
'Rural':'countryside,rustic,pastoral',
'Urban':'city,town,borough',
'Fend':'defend',
'Feign':'fake,pretend,assume,sham',
'Dawdle':'linger,delay,loiter,plod',
'Punctual':'prompt,on,time',
'Defer':'accept,submit,comply,bow,down',
'Amiable':'friendly,sociable,affable,likable',
'Bland':'tasteless,mild,plain,flavourless',
'Weary':'tired,fatigue,drained,drowsy,knackered,worn,out',
'Dreary':'dull,boring,monotonous,tedious,lifeless,routine,mundane',
'Deck':'surface,floor',
'Scum':'dirt,crust,layer,froth',
'Litter':'disorder,confusion,mess,clutter,rubbish',
'Shield':'protection,armour,defence,buffer',
'Tamper':'interfere,meddle,fiddle,interrupt',
'Sear':'burn,scorch,singe,char',
'Amendment':'alter,modify,change,correct',
'Parched':'thirsty,gasping,dehydrated',
'Preserve':'conserve,jam,sustain',
'Lent':'borrowed,rented,hired,loaned',
'Mound':'hill,mount,dune,hillock',
'Bough':'branch,limb,spur',
'Heed':'notice,attention,note,regard',
'Bashful':'shy,reserved,timid,meek,mild',
'Paramount':'important,dominant,utmost,significant',
'Capsized':'overturned,tipped,sank',
'Shrub':'bush,plant,climber',
'Craft':'skill,expertise,ability',
'Crafty':'sly,wily,cunning,devious,shrewd,astute,canny',
'Gullible':'trusting,naïve,innocent',
'Docile':'mild,passive,quite,meek,obedient,pliant,tame',
'Lounge':'living-room,family-room,sitting-room',
'Foil':'stop,frustrate,hinder,outwit',
'Bellow':'shout,roar,yell,bawl,holler,row',
'Hurl':'throw,fling,toss,chuck,launch',
'Haul':'tow,drag,pull,lug,heave',
'Fringe':'border,outlying,frontier',
'Descent':'decline,decrease',
'Peach':'fruit,colour,beauty,wow',
'Launch':'presentation,introduction,take-off,departure',
'Uprising':'rebel,rising,revolt,unrest,disturbance',
'Affable':'jovial,sociable,genial,friendly,amicable',
'Charitable':'generous,giving,liberal',
'Mandatory':'obligatory,compulsory,required,necessary,essential',
'Clarity':'clearness,lucid,transparency',
'Dormant':'inactive,sleeping,resting',
'Pristine':'clean,immaculate,unspoiled,perfect,spotless',
'Converse':'reverse,inverse,contrary,opposing,opposite',
'Poach':'rob,steal,thieve',
'Crude':'basic,unpolished,amateur,simple,rough,unfinished,unskilful,rookie',
'Intermediate':'middle,midway,mean,in-between',
'Tactful':'sensitive,thoughtful,considerate,discreet,diplomatic',
'Futile':'useless,pointless,fruitless,vain,wasted',
'Adore':'love,worship,esteem,respect,admire',
'Adorn':'decorate,garnish,ornament',
'Detest':'hate,loathe,despise,abor',
'Vague':'unclear,faint,ambiguous,imprecise,indefinite',
'Dolly':'model,puppet,toy,figure',
'Spectator':'viewer,watcher,observer,witness',
'Ladle':'spoon,scoop,dipper,server',
'Suit':'outfit,costume,uniform,ensemble',
'Rind':'peel,skin,husk,crust,coat',
'Urn':'pot,container,vessel,pitcher,jug',
'Warren':'den,hole,earth,habitat,burrow,lair',
'Seldom':'rarely,infrequently,occasionally,hardly',
'Concur':'agree,correspond,harmonize,coincide',
'Conceal':'misplace,hidden',
'Truce':'make,peace,lull',
'Dainty':'delicate,elegant,graceful,exquisite,refined,petite',
'Estimate':'guess,crock',
'Bash':'party,celebration,gala',
'Perceive':'observe,notice,remark,distinguish,recognise',
'Arrogant':'big-headed,superior,conceited,proud',
'Animated':'active,lively,energetic,vigorous,vibrant,dynamic,spirited',
'Tentative':'hesitant,cautious,uncertain,unsure',
'Reject':'discard,castoff,rebuff',
'Swagger':'boastfulness,boasting,bragging,arrogance',
'Moral':'ethical,good,right,honest,honourable,just,virtuous',
'Corrupt':'dishonest,crooked,unethical,immoral',
'Daunt':'scare,frighten,overwhelm,discourage,deter',
'Safari':'expedition,voyage,trip,excursions,outing,journey',
'Menace':'risk,danger,threat,peril,hazard,dangerous',
'Wreckage':'debris,ruin,wreck,rubble,remains',
'Freight':'cargo,load,goods,stuff',
'Crease':'wrinkle,crinkle,rumple,crumple',
'Saunter':'sprint,stroll,walk,ramble,amble,meander',
'Rowdy':'noisy,unruly,loud,disorderly,boisterous,raucous,disruptive',
'Audible':'easy,to,hear,distinct,clear,loud',
'Conspire':'plot,scheme,plan',
'Frivolous':'not-serious,playful,frolicsome,perky,silly,flippant',
'Lenient':'kind,forgiving,mild,moderate,tolerant,easy-going',
'Rectify':'amend,correct,alter',
'Droop':'sag,wilt,bow,flop,sink,slouch',
'Hoard':'store,pile,mass,reserve,stockpile,stash',
'Vigilant':'watchful,attentive,alert,wary,cautious,observant,heedful,aware',
'Retain':'recall,recollect,remember,hold,preserve',
'Opponent':'enemy,foe,rival,challenger,adversary',
'Valour':'courage,bravery,spirit,nerve,fearless,boldness,gallantry,heroic,pluck',
'Decline':'decay,lessen,drop,deteriorate,decrease',
'Elevator':'going-up,machine-or-shaft,muscle-that-raises-body-part',
'Earnest':'serious,grave,sober,genuine,solemn',
'Terminate':'end,conclude,sack,axe,fire,dismiss',
'Gather':'assemble,congregate,collect',
'Scarcity':'shortage,lack,dearth,scanty,meagre',
'Agile':'swift,nimble,alert,responsive,lively',
'Supple':'soft,flexible,mobile,elastic',
'Retreat':'recoil,withdraw,evacuate,flee',
'Protrude':'stick-out,jut-out,overhang,bulge,swell,obtrude',
'Wail':'howl,moan,scream,cry,yelp,whine',
'Lisp':'speech,difficulty,slutter',
'Treasured':'cherished,beloved,precious,dear,expensive,beloved',
'Thrifty':'miserly,careful,frugal,economical,cheap',
'Glory':'brilliance,beauty,wonder,splendour',
'Malady':'ailment,illness,sickness,disorder,condition',
'Ancestor':'forefather,descendents,forebear,predecessor',
'Pantry':'food,storage,storeroom,larder',
'Serious':'grave,solemn,sombre,grim,sober',
'Satisfied':'content,pleased,proud,satiate,convinced,happy',
'Negligent':'carless,thoughtless',
'Souvenir':'memento,keepsake',
'Donation':'offering,gift,present,contribution',
'Tranquillity':'harmony,serene,calm,sanctuary,refugee',
'Hoax':'trick,joke,jest,prank,cheat,fraud,bluff',
'Persuade':'coax,entice,cause,lead',
'Vigorous':'energetic,dynamic,active,robust',
'Altitude':'height,lofty,elevation',
'Strike':'hit,pound,punch,slap,spank,ignite,affect,agree,discover,lower,takedown',
'Replicate':'copy,mimic,imitate,duplicate',
'Trivial':'unimportant,small,penalty,fine,petty',
'Opaque':'unclear,cloudy,muddy,misty,smoky,dense',
'Scurry':'scramble,dash,hurry,fast',
'Detour':'diversion,deviation',
'Jealous':'envious,bitter,green-eyed,resentful',
'Diminish':'lessen,contract',
'Infectious':'contagious,catching,transmittable',
'Warrior':'solider,trooper,fighter',
'Speckled':'dotted,freckled',
'Inlet':'creek,bay,cove',
'Heave':'throw,hurl,toss',
'Perimeter':'edge,rim,border,boundary,circumference',
'Athletic':'sporty,healthy,agile,nimble,energetic',
'Spry':'lively,agile,nimble,active,brisk',
'Indolent':'lazy,lethargic,idle,sluggish',
'Insolent':'rude,impudent,disrespectful',
'Legible':'readable,clear,understandable',
'Elevate':'raise,lift,uplift,hoist,upraise',
'Diligent':'hardworking,industrious,assiduous',
'Ale':'beer,drink,alcohol',
'Log':'diary,journal,calendar,logbook,record',
'Grumpy':'irritable,bad-tempered,cranky,sullen',
'Miffed':'annoyed,riled,upset,hurt,fed-up,resentful',
'Bid':'offer,utter,invite',
'Moat':'a-deep-wide-ditch',
'Lance':'a-long-pointed-rod-used-as-weapon',
'Shallow':'superficial,not-deep',
'Еmu':'a-type-of-bird-like-ostrich',
'Ire':'anger,rage,fury,wrath,temper',
'Blotted-out':'blocked-out,disappear,e.g.the-grey-clouds-blotted-out-the-sun',
'Merry':'gleeful,joyful,cheerful,excited',
'Scruting':'insepection,examine,look-closely',
'Clad':'dressed(people),covered(things)',
'Perch':'for-bird-means-sit-rest-or-alight,for-person-means-sit-on-something,for-building-means-be-situated-or-located',
'Dilapidated':'broken-down,shabby,ramshackle,battered,rickety,worn-out,in-need-of',
'Burgenoing':'growing,increasing,expanding',
'Unease':'anxious,stressed,uncomfortable',
'Solemnly':'seriously',
'Gay':'cheerful,jolly,homosexual,bright',
'Abide':'obey,follow,accept',
'Remorse':'regret,guilt,disappoint',
'Wretch':'villain,criminal,unhappy-person',
'Doom':'death,destruction',
'Relentles':'merciless,pitiless',
'Emboldened':'enconrage-by-something',
'Din':'loud,noise,clang,clamour,clatter,del',
'Dame':'an-elderly-or-mature-woman',
'Rack':'storm',
'To-exult':'to-rejoice,be-delighted,be-euphoric',
'Keel':'the-underside-of-a-ship',
'Squand':'to,waste,misuse,to-spend-foolishly',
'Grim':'dingy,dull,very-serious',
'Flora-and-fauna':'plants-and-animals',
'Dwindling':'gradually-decrease-in-size-or-amount-or-strength',
'Inadvertently':'unintentionally,accidently,by-mistake',
'Habitat':'home,natural-environment,abode',
'Deduce':'infer,guess,surmise,calculate,draw,conclusion',
'Satchel':'a-bag-with-a-long-strap.',
'Rifled':'search-quickly-through-something.',
'Contemplated':',thinking,deep-thought,remembering-past',
'Vicked':'cut,scratch',
'Intimidating':'frightening,overawe,threatening,forced',
'Sprawling':',spreading-out-over-a-larger-area',
'Inquisitive':'curious,interested,intrusive,concerned',
'Bustling':'crowded,swarming,hectic,lively',
'Winding':',curvy,twisting,loop',
'Haggle':',bargain,negotiate',
'Array':'range,types,variety',
'Enchant':'attractive,captivate,enthral,charm,interested',
'Culinary':'cooking-skills',
'Overlooking':'have-a-view-from-above,balcony-overlooking-the-river',
'Ceremonial':'ritual,events,religions',
'Encounter':'meet,come-across,run-into,stumble-upon,bump-into,meet-by-chance',
'Sycamore':'type-of-tree',
'Trees':'elm,ash,oak,fir,sycamore,leak',
'Nestles':'location,situated,placed',
'Obscure':'unclear',
'Petty':'trivial,small,negligible,insignificant',
'Stems':'origin,start,root',
'Quirks':'peculiarity',
'Glut':'too-many,too-much,excess,abundant,surplus',
'Boasts':'gloats,show-off,brag',
'Amples':'lots-of,many,plenty',
'Bespoke':'custom-made,made-to-order,bespoke-place-or-thing,made-for-you',
'Accolade':'awarded,recognition,honour',
'Imminent':'happening-soon,about-to-happen,close,near,forthcoming,on-the-way',
'Renowned':'famous,illustrious,prominent,great',
'Vanquish':'to-conquer,to-overcome',
'Rean':'to-widen,to-criticize',
'State':'government,politics',
'Futurstic':'ahead-of-time,in-future',
'Marred':'spoiled,ruin,disfigure',
'Irate':'angry,furious,fuming,enraged',
'Unruly':'rowdy,noisy,wild,disobedient',
'Chaotic':'turmoil,disorderly,confused,chaos,disarray,messy',
'Subsidise':'reduce,less,decrease',
'Vociferous':'vocal,frank,candid,open,direct,eager,vehement',
'Inevitably':'unavoidable,assured,certain,fated,sure,necessary',
'Intellectual':'intelligence,mental,cerebral,cognitive,rational,conceptual',
'Revenue':'income,takings,receipts,profit,earnings,returns',
'Income-tax':'tax-levied-on-income',
'Gusto':'with-enjoyment',
'Shabby':'scruffy,dingy,wornout',
'Agape':'wide-open-mouth-in-surprise-or-wonder',
'Seek':'sought,look-for,pursue,go-after,attemp,task-for',
'Squander':'to-waste',
'Victor':'victorious,triumphant,succeseful'
}

# Function to clear the exhausted iterator once it is processed
def _one_pass(iters):
    i = 0
    while i<len(iters):
        try:
            yield next(iters[i])
        except StopIteration:
            del iters[i]
        else:
            i+=1

# Generator custom function to zip two lists of variable lenghts until an empty tuple is found
def zip_varlen(*iterables):
    iters = [iter(it) for it in iterables]
    while True: #broken when an empty tuple is given by _one_pass
        val = tuple(_one_pass(iters))
        if val:
            yield val
        else:
            break

def zip_discard_compr(*iterables, sentinel=object()):
    return [[entry for entry in iterable if entry is not sentinel]
            for iterable in zip_longest(*iterables, fillvalue=sentinel)]

# Function to split dictionary into chunks of 20 words
def split_dict_into_chunks(dictionary, chunk_size=20):
    items = list(dictionary.items())
    return [dict(items[i:i+chunk_size]) for i in range(0, len(items), chunk_size)]

# Function to generate and save the matching puzzle
def generate_puzzle_files(word_chunks,name=datetime.now().date()):
    try:
        os.makedirs("puzzles", exist_ok=True)  # Create folder for puzzles
        os.makedirs("answers", exist_ok=True)  # Create separate folder for answers
        for idx, chunk in enumerate(word_chunks, 1):
            words = list(set(chunk.values()))
            wordset = set()
            word_lambda = wordset.add
            meanings = [word.strip() for word in chunk.keys() if not (word in wordset or word_lambda(word))]
            #print(f'idx: {idx} -> meanings: {meanings} \n > words: {words} \n')
            random.shuffle(words)  # Shuffle meanings to make the puzzle hard
            word_dict = {chr(97 + i): word for i, word in enumerate(words)}  # Assign 'a', 'b', 'c'...
            #print(f'idx: {idx} -> chunk: {chunk}')
            print(f'idx: {idx} -> ({len(meanings)})->meanings(): {meanings}')
            print(f'idx: {idx} -> ({len(word_dict)})->word_dict): {word_dict}')
            print(f'Extracting values from word_dict: ')
            for k,v in word_dict.items():
                print(f'idx: {idx} => k,v:word_dict[k] :: {k},{v}:{word_dict[k]}')
            #print(f'Expression -> answers = meaning: [key for key, word in word_dict.items() if word in chunk[meaning]] for meaning in meanings')
            # Generate correct answer key
            correct_answers = {meaning: [key for key, word in word_dict.items() if word in chunk[meaning]] for meaning in meanings}
            #print(f'idx: {idx} -> correct_answers: {correct_answers}')
            print(f'\n\n\n\n\n\n')
            # Save puzzle in puzzles directory
            puzzle_filename = f"puzzles/puzzle_{idx}.txt"
            with open(puzzle_filename, "w", encoding="utf-8") as puzzle_file:
                puzzle_file.write("Match the synonyms numbered on the left in lower-case with it's correct meaning on the right in Capital letter:\n\n")   
                pz=1
                try:
                # Print words and their corresponding shuffled meanings side by side
                #for i, (word, key) in enumerate(zip(meanings, word_dict.keys()), 1):
                #for (word, key) in islice(zip_longest(meanings,word_dict.keys()," "),0,len(meanings),1):
                #for (word, key, value) in islice(zip_varlen(meanings,word_dict.keys(),word_dict.values()),0,len(meanings),1):
                #for (word, key) in islice(zip_longest(meanings,word_dict.keys(),'NA'),0,len(meanings)):
                    for (word, key) in islice(zip_longest(meanings,word_dict.keys()),0,len(meanings),1):
                        #print(f'in loop islice # counter->{pz}, word: {word}, key: {key}, value: {word_dict[key]}')
                        if(not key or not word_dict[key]):
                            puzzle_file.write(f"{pz}. {word:<15} \n")
                        else:
                            puzzle_file.write(f"{pz}. {word:<15} {key}) {word_dict[key]}\n")
                        pz += 1
                except ValueError as v:
                    raise RuntimeError(f'Invalid value in input it seems: Error {v}, Corrupted state pz:{pz}, word: - key: - value: were in the zip_longest loop')
                        #: ({pz}. {word} - {key} - {word_dict[key]})')
                print(f"Puzzle saved: {puzzle_filename}")

            # Save answers in answers directory
            answer_filename = f"answers/answer_{idx}.txt"
            with open(answer_filename, "w", encoding="utf-8") as answer_file:
                 answer_file.write("Answer Key:\n\n")
                 for word, keys in correct_answers.items():
                     answer_file.write(f"{word} -> {', '.join(keys)}\n")
            print(f"Answer key saved: {answer_filename}")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(f'We have a failure processing puzzle or answer files  -> Reason: {e}, exc_type: {exc_type}, fname: {fname}, exc_tb.tb_lineno: {exc_tb.tb_lineno}') 
     

def invert_dict_meaning2word(dictionary):
    op={}
    #print(f'Starting expand_dict_1word_to_1meaning -> op is: {len(op)}')
    for k,v in dictionary.items():
        #print(f'in loop -> v is: {len(v)}. splitting!')
        nv=[]
        nv = v.split(',')
        for each in nv:
            op[each]=k
        #print(f'nv is: {len(nv)}')
        #op[k]=nv 
    #print(f'op is now: {len(op)} <')
    #print(f'Returning dictionary -> {op}')
    return op 

# Split dictionary and generate puzzles
try:
    size=len(word_dict)
    #print(f'Starting Execution: wordlist is of size {size}')
    if(size > 0):
        meaning2word = invert_dict_meaning2word(word_dict)
        #print(f'oneword_onemeaning -> {oneword_onemeaning}')
        word_chunks = split_dict_into_chunks(meaning2word, 20)
        generate_puzzle_files(word_chunks)
except Exception as e:
          exc_type, exc_obj, exc_tb = sys.exc_info()
          fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
          print(f'We have a failure processing output -> Reason: {e}, exc_type: {exc_type}, fname: {fname}, exc_tb.tb_lineno: {exc_tb.tb_lineno}') 
 


