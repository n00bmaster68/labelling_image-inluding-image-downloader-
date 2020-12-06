from collections import Counter
import math

stop_words = ['s', 'edition', 'google', 'youtube', 'facebook', 'instagram', 'tweeter', 'quintessential', 'monumental', 'possible', 'cylindrical', 'grubby', 'strange', 'vengeful', 'hideous', 'thick', 'the', 'me', 'nifty', 'scaly', 'tidy', 'forthright', 'irresponsible', 'unreality', 'insidious', 'worn', 'stormy', 'clumsy', 'rude', 'broken', 'compassionate', 'shocking', 'fine', 'vast', '?', 'cuddly', 'concerned', 'productive', 'buzzing', 'warm', 'used', 'querulous', 'sudden', 'bumpy', 'ugly', 'proud', 'indelible', 'bravery', 'anger', 'unsung', 'solid', 'distinct', 'about', 'frozen', 'ill', 'victorious', 'low', 'awesome', 'distorted', 'thankful', 'those', 'fumbling', 'crisp', 'helpless', 'knobby', 'inconsequential', 'mild', 'that', 'belief', 'needn', 'peppery', 'whimsical', 'trivial', 'gain', 'adolescent', 'improbable', 'brisk', 'wiry', 'coldness', 'miserable', 'teeming', 'entire', 'idle', 'themselves', 'key', 'high', 'incompatible', 'fussy', 'kindness', 'can', 'cruel', 'mixed', 'revolving', 'friendship', 'drab', 'grave', 'you', 'known', 'yawning', 'belated', 'present', 'pertinent', 'impeccable', 'disfigured', 'lasting', 'overjoyed', 'made-up', 'self-reliant', 'capital', 'favorite', 'classic', 'wooden', 'happy-go-lucky', 'unwilling', 'wisdom', 'amazing', 'luminous', 'tubby', 've', 'impartial', 'luxurious', 'pointed', 'same', 'quixotic', 'frizzy', 'stunning', 'kind', 'sweet', 'dear', 'superior', 'frightened', 'exciting', 'expensive', 'off', 'connect', 'bad', 'own', 'agonizing', 'elegance', 'outgoing', 'sacrifice', 'unkempt', 'grown', 'barren', 'shocked', 'attached', 'between', 'spirited', 'honored', 'it', 'gargantuan', 'theirs', 'over', 'nippy', 'fresh', 'are', 'tremendous', 'fiction', 'brilliance', 'wary', 'happiness', 'fluid', 'unfortunate', 'decent', 'popular', 'pristine', ';', 'unique', 'male', 'villainous', 'handsome', 'difficult', 'spicy', 'frivolous', 'tall', '(', 's', 'his', 'even', 'sweltering', 'likable', 'diligent', 'magnificent', 'poverty', 'ability', "you're", 'vigilant', 'clever', 'puzzled', 'dull', 'heavy', 'trust', 'dental', 'some', 'just', 'decimal', 'unused', 'flimsy', 'upbeat', 'windy', 'huge', 'tangible', 'practical', 'ample', 'nervous', 'wealthy', 'fat', 'herself', 'delectable', 'evil', 'uncomfortable', 'defenseless', 'whose', 'extraneous', 'splendid', "you'll", 'moist', 'occasional', 'worst', 'subdued', 'weird', 'pretty', 'haven', 'such', 'colorful', 'aged', 'fragrant', 'modern', 'hoarse', 'wide-eyed', 'busy', 'adept', 'insecure', 'torn', 'giving', 'dopey', 'needy', 'quirky', 'should', 'clarity', 'unlined', 'now', 'hidden', 'woeful', 'sarcastic', 'closed', 'naughty', 'spiteful', 'sticky', 'husky', 'fickle', 'flex', 'quizzical', 'babyish', 'squeaky', 'scholarly', 'unsightly', 'natural', 'sad', 'in', 'wide', '/', 'passionate', 'most', 'joy', 'appropriate', 'then', 'whom', 'shiny', 'worrisome', 'similar', 'customer service', 'cheap', 'unhappy', 'nice', 'shock', 'again', 'limping', 'kindly', 'urban', 'worthless', '7', 'black', 'will', 'concrete', 'incomparable', 'calm', 'oval', 'delayed', 'cooperative', 'courageous', 'gloomy', 'blind', 'celebrated', 'arid', 'pleased', 'legal', 'glamorous', 'talkative', 'feline', 'glorious', 'nonstop', 'bountiful', 'naive', 'remarkable', 'pain', 'inborn', 'sparkling', 'disgusting', 'valuable', 'easy-going', 'wicked', 'dependent', 'into', 'variable', 'lucky', 'patience', 'blushing', 'how', 'ringed', 'old', 'alive', 'lone', 'very', 'excitable', 'merry', 'frugal', 'optimistic', 'hasty', 'fatal', 'extra-small', 'jaunty', 'hospitable', 'amazement', 'drafty', 'reflecting', 'finished', 'little', 'memes', 'terrible', 'unlucky', 'canine', 'pastel', 'chilly', 'memorable', 'obedient', 'narrow', 'with', 'brown', 'wasteful', 'steep', 'traumatic', 'loathsome', 'liberty', 'eminent', 'sturdy', 'worldly', 'yours', 'stale', '#', 'jittery', 'unacceptable', 'yourselves', 'courage', 'radiant', 'trustworthy', 'svelte', 'fantastic', 'pesky', 'sorrowful', 'quick-witted', 'wise', 'who', 'jovial', 'happy', 'true', 'insanity', 'raw', 'muddy', 'any', 'crafty', 'petty', 'antique', 'religion', 'bright', 'coordinated', 'dramatic', 'unequaled', 'intrepid', 'flawed', 'royal', 'creative', 'euphoric', 'guilty', 'voluminous', 'vital', 'periodic', 'imperfect', 'untried', 'shoddy', 'purple', 'harmonious', 'weak', 'boring', 'astonishing', 'lonely', 'tinted', 'costly', 'edible', 'unpleasant', 'everlasting', 'empty', 'wretched', 'poised', 'fearless', 'total', 'life', 'uneven', 'fruitful', 'candid', 'ambitious', 'thunderous', 'trim', 'dry', 'dapper', 'extra-large', 'linear', 'shallow', 'sneaky', 'ashamed', 'mediocre', 'its', 'irritation', 'robust', 'peaceful', 'an', 'second', 'hers', 'great', 'being', 'formal', 'meager', 'unusual', 'outlandish', 'heartfelt', 'flamboyant', 'numb', 'hurtful', 'frigid', 'vacant', 'inexperienced', 'menacing', 'oddball', 'unrealistic', 'back', 'appetite', 'rubbery', 'well-to-do', 'live', 'wild', 'sweaty', 'blaring', 'discrete', 'elegant', 'kaleidoscopic', 'pride', 'frayed', 'envious', 'mortified', 'quick', 'dimwitted', 'remorseful', 'insistent', 'grizzled', 'high-level', 'overcooked', 'afraid', 'trusty', 'sick', 'principle', 'snappy', 'prime', 'qualified', 'to', 'accurate', 'weary', 'at', 'better', 'runny', 'accomplished', 'webbed', 'idiotic', 'lost', 'verifiable', 'weekly', 'sniveling', 'supportive', 'ruddy', 'hollow', 'foolish', 'courteous', 'evergreen', 'stark', 'dishonesty', 'myself', 'bulky', 'good', 'shan', 'gaseous', 'tired', 'embellished', 'likely', "she's", 'rapid', 'slimy', 'friendly', 'beautiful', 'kosher', 'plush', 'confusion', 'vivacious', 'unknown', 'affectionate', 'well-worn', 'graceful', 'untimely', '2', 'yellowish', 'loyal', 'impressive', 'whopping', 'fancy', '-', 'glaring', 'maturity', 'clean', 'ill-informed', 'plastic', 'virtuous', 'more', 'forked', 'faith', 'ornate', 'troubled', 'another', 'pale', 'unfolded', 'salty', 'good-natured', 'strict', 'meek', 'velvety', 'complicated', 'strident', 'infatuated', 'deep', 'marvelous', 'sandy', 'innocent', 'dream', ':', 'incomplete', 'somber', 'ragged', 'rewarding', 'generation', 'joyous', 'reckless', 'acclaimed', 'aggravating', 'probable', 'ourselves', 'near', 'goodness', 'greedy', 'square', 'tan', 'dead', 'unruly', 'lie', 'responsible', 'vibrant', 'woozy', 'gruesome', 'extroverted', 'creamy', 'animated', 'biodegradable', 'whirlwind', '®', 'slow', 'nutritious', 'false', 'milky', 'bold', 'pungent', 'bleak', 'union', 'disastrous', 'luck', 'mature', 'charity', 'vicious', 'our', 'chubby', 'nor', 'elated', 'tight', 'altruistic', 'these', 'leading', 'service', 'ignorant', 'private', 'defeat', 'insubstantial', 'luxury', 'measly', 'don', 'showy', 'immaterial', 'smart', 'crooked', 'acceptable', 'nocturnal', 'definite', 'notable', 'calculating', 'ornery', 'gross', 'blue', 'childhood', 'shameful', 'repentant', 'homely', 'athletic', 'tricky', 'triangular', 'best', 'defensive', 'serpentine', 'pleasing', 'specific', 'fear', 'roasted', 'waterlogged', 'energetic', "shouldn't", 'big-hearted', 'clueless', 'stupendous', 'elaborate', 'well-groomed', 'sleepy', 'simplistic', 'queasy', 'juvenile', 'glum', 'determined', 'murky', 'scared', 'silent', 'dirty', 'fitting', 'healthy', 'power', 'short-term', 'cheery', 'ajar', ',', 'horrible', 'potable', 'growth', 'haunting', 'stimulating', 'zany', 'confused', 'rich', 'on', 'agile', 'messy', 'stingy', 'forsaken', 'imperturbable', 'last', 'clear', 'grateful', 'apt', 'watchful', 'frosty', 'hate', 'partial', 'actual', 'soulful', 'deafening', 'feminine', 'watery', 'wrathful', 'scarce', 'surprised', 'few', 'miniature', 'lustrous', 'international', 'old-fashioned', 'slight', 'superficial', '6', 'jam-packed', 'utter', 'enchanting', 'palatable', 'spectacular', 'baggy', 'harsh', 'wavy', 'ego', 'infamous', 'experienced', 'subtle', 'previous', 'loose', 'studious', 'youthful', 'worse', 'funny', 'humongous', 'colossal', 'submissive', 'normal', 'striking', 'unfit', 'multicolored', 'enlightened', 'ethical', 'under', 'both', 'quaint', 'thirsty', 'arctic', 'exemplary', 'plaintive', 'above', 'too', 'competent', "it's", 'hot', 'he', 'impossible', 'or', 'equal', 'elementary', 'questionable', 'simple', 'essential', 'violet', 'turbulent', 'acidic', 'tiredness', 'sardonic', 'kindhearted', 'gullible', 'scornful', 'cooked', 'far', 'composed', 'uncommon', 'upset', 'virtual', 'thrifty', 'silky', 'open', 'left', "you've", 'cleverness', 'enormous', '&', 'honest', 'need', 'esteemed', 'mushy', 'flawless', 'impure', 'awkward', 'straight', 'than', 'tame', 'circular', 'intelligent', 'jolly', 'shadowy', 'spiffy', 'monthly', 'meme', 'bowed', 'dependable', 'different', 'useless', 'wariness', 'down', 'muted', 'we', 'jaded', 'was', 'absolute', 'long-term', 'justice', 'personal', 'cheerful', 'rowdy', 'definitive', 'well-documented', 'imaginary', 'lively', 'colorless', 'surprise', 'other', 'new', 'positive', 'infancy', 'prestigious', 'shimmering', 'wordy', 'burdensome', 'venerated', 'mean', 'welcome', 'plain', 'darling', 'communication', 'zesty', 'violent', 'crowded', 'content', 'when', 'conventional', 'slim', 'burly', 'strength', 'novel', 'sure-footed', 'disquiet', 'Spanish', 'freedom', 'lumpy', 'average', 'cautious', 'rundown', 'worthy', 'yellow', 'green', 'lighthearted', 'misty', 'disregard', 'frilly', 'us', 'well-made', 'mercy', 'aromatic', 'medical', 'close', 'fatherly', 'loving', 'not', 'dimpled', 'starchy', 'careful', 'basic', 'peculiarity', 'template','lazy', 'sinful', 'flustered', 'automatic', 'usable', 'tempting', 'stiff', 'ultimate', 'granular', 'interesting', 'remote', 'single', 'tragic', 'nasty', 'humiliating', 'super', 'ancient', 'electric', 'recent', 'unwieldy', 'slippery', 'yearly', 'after', 'cluttered', 'terrific', 'third', 'below', 'round', 'imaginative', 'satisfied', 'itself', 'unhealthy', 'staid', 'opulent', 'threadbare', 'massive', 'enchanted', 'constant', 'sensitivity', 'daring', 'thorough', 'zigzag', 'and', 'enraged', 'scary', 'digital', 'itchy', 'defiant', 'miserly', 'common', 'doting', 'disbelief', 'wealth', 'yummy', 'primary', 'wit', 'spherical', 'alarming', 'opinion', '3', 'twin', 'slushy', 'sanity', 'unaware', 'coarse', 'apprehension', 'dismal', 'scrawny', 'bland', 'strong', 'humble', 'ripe', 'sour', 'inferior', 'mad', 'curiosity', 'optimal', 'unsteady', 'gossip', 'dishonest', 'wobbly', 'metallic', 'beneficial', 'speed', 'compassion', 'treasured', 'important', 'nautical', 'punctual', 'quarrelsome', 'familiar', 're', 'joyful', 'vapid', 'acrobatic', 'nutty', 'sorrow', 'taut', 'limp', 'skeletal', 'trusting', 'smooth', 'substantial', 'mysterious', 'lean', 'do', 'for', 'yourself', 'dedication', 'large', 'no', 'riches', 'ironclad', 'jubilant', 'agreeable', 'of', 'stable', 'thrill', 'where', 'delightful', 'amused', 'ain', 'odd', 'warmth', 'immense', 'timely', 'skill', 'well-informed', 'lanky', 'married', 'trained', 'pure', 'growling', 'caring', 'aggressive', 'awareness', 'noxious', 'thoughtful', 'lovable', 'adoration', 'once', 'prize', 'giant', 'helpful', 'chaos', 'fair', 'by', 'unwelcome', 'curvy', 'love', 'hateful', 'gray', 'impish', 'what', 'alienated', 'fuzzy', 'bony', 'whispered', 'deserted', 'envy', 'far-off', 'inflation', 'indolent', 'hopeful', 'superb', 'stupid', 'corny', 'quarterly', 'does', 'earnest', 'powerless', 'jumbo', 'impractical', 'trend', 'neglected', 'ours', 'joint', 'brilliant', 'against', 'writhing', 'pointless', 'careless', 'silliness', 'criminal', 'understated', 'fake', 'tedious', 'relief', 'scented', 'generosity', 'am', 'nimble', 'emotional', 'fragility', 'unripe', 'wonderful', 'bouncy', 'educated', 'adored', 'brief', 'hearty', 'black-and-white', 'piercing', ')', 'grim', 'fabulous', 'lined', 'valid', 'sparse', 'rusty', 'minty', 'reasonable', 'obvious', 'filthy', 'exhausted', 'idolized', 'noisy', 'bustling', 'which', 'idea', 'gentle', 'right', 'rectangular', 'muffled', 'hard', 'lopsided', 'brave', 'nap', 'respectful', 'dreary', 'relaxation', 'past', 'focused', 'cultured', 'worried', '1', 'creepy', 'profitable', 'grouchy', 'gracious', 'harmless', 'prickly', 'corrupt', 'my', 'divorce', 'scratchy', 'insignificant', 'bronze', 'grotesque', 'warmhearted', 'sharp', 'zealous', 'orange', 'putrid', 'weighty', 'descriptive', 'laughter', 'tough', 'half', 'talent', 'honorable', 'has', 'wrong', 'pushy', 'realistic', 'glass', 'frail', 'smug', 'dim', 'from', 'light', 'disappointment', 'sleep', 'female', 'sophisticated', 'each', 'while', 'alert', 'complete', 'tiny', 'cool', 'ecstatic', 'majestic', 'before', 'music', 'attractive', 'whole', 'oblong', 'offbeat', 'droopy', 'cumbersome', 'thorny', 'failing', 'short', 'impolite', 'admirable', '@', 'puny', 'but', 'rotating', 'hilarious', 'selfish', 'parched', '5', 'suspicious', 'melodic', 'jumpy', 'starry', 'until', 'liquid', 'lawful', '4', 'delight', 'fluffy', 'considerate', 'excited', 'late', 'expert', 'knowing', 'knotty', 'grumpy', 'parallel', 'loss', 'giddy', 'mindless', 'foolhardy', 'offensive', 'rosy', 'faint', 'snoopy', 'sane', 'care', 'annoyance', 'because', 'winged', 'testy', 'been', 'shrill', 'jagged', 'sociable', 'authorized', 'free', 'internal', 'utilized', 'had', 'pricey', 'ma', 'dearest', 'irritating', 'advanced', 'peace', 'secondary', 'flaky', 'angry', 'mundane', 'wry', 'leafy', 'dizzy', 'intelligence', 'she', 'first', 'opportunity', 'heavenly', 'negligible', 'adventurous', 'bubbly', 'breakable', 'warped', 'legitimate', 'safe', 'silver', '8', 'second-hand', 'tender', 'hurt', 'famous', 'functional', 'incredible', 'deceit', 'complex', 'generous', 'curly', 'upright', 'blond', 'education', 'unwritten', 'relieved', 'neat', 'during', 'gregarious', 'puzzling', 'anguished', 'soupy', 'plump', 'determination', 'unlawful', 'truthful', 'attentive', 'sugary', 'every', 'embarrassed', 'red', 'ready', 'crazy', 'this', 'spry', 'worry', 'their', 'doing', 'rough', 'hefty', 'chief', 'assured', 'unfinished', 'limited', 'illiterate', 'wee', 'unimportant', 'jealous', 'noteworthy', 'kooky', 'delirious', 'impassioned', 'squiggly', 'full', 'dense', 'weepy', 'shabby', 'etc', 'separate', 'big', 'amusing', 'them', 'instructive', 'hatred', 'overdue', 'illustrious', 'apprehensive', 'swift', 'stylish', 'neighboring', 'noted', 'admired', 'icy', 'tattered', 'demanding', 'buttery', 'serene', 'annual', 'deficient', 'small', 'perfumed', 'failure', 'obese', 'fortunate', 'klutzy', 'identical', 'orderly', 'polished', 'critical', 'suburban', 'disloyal', 'beauty', 'forceful', 'disturbance', 'medium', 'bewitched', 'judicious', 'tolerance', 'through', 'bossy', 'handy', 'well-off', 'adorable', 'keen', 'law', 'abandoned', 'aching', 'pessimistic', 'comfortable', 'genuine', 'devoted', 'standard', 'uncertainty', 'only', 'pleasure', 'infinite', 'easy', 'worthwhile', 'rigid', 'downright', 'decisive', 'vague', 'rare', 'golden', 'vs', 'grimy', 'confidence', 'pleasant', 'original', 'junior', 'victory', 'charming', 'all', 'witty', 'weakness', 'perfect', 'idealistic', 'ideal', 'ill-fated', 'silly', 'gleeful', 'cold', 'mountainous', 'gigantic', 'political', 'delicious', 'juicy', 'secret', 'carefree', '9', 'young', 'perky', 'aware', 'cavernous', 'outstanding', 'out', 'pitiful', 'flat', 'official', 'fearful', 'unemployment', 'livid', 'academic', 'regular', 'elderly', 'did', 'sympathetic', 'warlike', 'rash', 'soggy', 'direct', 'they', 'next', 'necessary', 'awful', 'motherly', 'required', 'cute', 'snarling', 'advantage', 'masculine', 'able', 'precious', 'cultivated', 'far-flung', 'here', 'lame', 'quiet', 'death', 'beloved', 'anchored', 'bruised', 'outlying', 'mammoth', 'austere', 'immaculate', 'tasty', 'lovely', 'intent', 'glistening', 'exotic', 'wan', 'loud', 'faithful', 'wet', '|', '+', 'mellow', 'goal', 'dual', 'eager', 'double', 'release', 'grand', "you'd", 'elastic', 'were', 'outrageous', 'gifted', 'damaged', 'long', 'profuse', 'further', 'useful', 'polite', 'glittering', 'him', 'serious', 'oily', 'fast', 'is', 'bogus', 'meaty', 'grounded', 'rotten', 'repulsive', 'speedy', 'her', 'hairy', 'unselfish', 'faraway', 'unwitting', 'bare', 'winding', "that'll", 'tepid', 'thin', 'gummy', 'impressionable', 'artistic', 'horror', 'spotted', 'hard-to-find', 'flowery', 'reality', 'grandiose', 'wilted', 'real', '.', 'exalted', 'intentional', 'motionless', 'flickering', 'success', 'boiling', 'sentimental', 'awe', 'buoyant', 'be', 'scientific', 'self-assured', 'illegal', 'united', 'satisfaction', 'feisty', 'steel', 'prudent', '...', 'immediate', 'have', 'dutiful', 'shady', 'fascination', 'powerful', 'crushing', 'musty', 'several', 'clear-cut', 'posh', 'mealy', 'dangerous', 'major', 'vigorous', 'growing', 'vivid', 'hungry', 'rural', 'disguised', 'stained', 'as', 'blank', 'favorable', '!', 'agitated', 'uniform', 'general', 'why', 'loneliness', 'anxious', 'll', 'early', 'shy', 'himself', 'proper', 'wiggly', 'portly', 'firsthand', 'organic', 'unconscious', '*', 'firm', 'cloudy', 'series', 'informal', 'there', 'angelic', 'dark', 'minor', 'blissful', 'gleaming', 'visible', 'icky', 'tense', 'flashy', 'distant', 'lavish', 'phony', 'infatuation', 'lumbering', 'reliable', 'if', 'poor', 'French', 'gorgeous', 'soft', 'authentic', 'avaricious', 'untrue', 'unnatural', 'severe', 'tart', 'skinny', 'up', 'anxiety', 'harmful', 'comfort', 'regal', 'pink', 'bite-sized', 'overlooked', 'knowledgeable', 'front', 'gripping', 'elliptical', 'spotless', 'so', 'your', 'playful', 'excellent', 'smoggy', 'frequent', 'humming', 'misguided', 'moral', 'paltry', 'alarmed', 'striped', 'ordinary', 'sore', 'well-lit', 'handmade', 'frightening', 'trifling', 'active', 'deadly', 'fixed', 'uk', 'delay', 'adventure', 'restoration', 'negative', 'fond', 'bitter', 'detailed', 'white', 'frank', 'damp', 'movement', 'shameless', 'monstrous', 'infantile', 'having', 'untidy', 'sunny', 'sizzling', 'physical', 'modest', 'vain', 'willing', "should've", 'dazzling', 'equatorial', 'crime', 'hope', 'glossy', 'i', 'flippant', 'conscious']

def tf (bag_of_word):
	max_key =  max(bag_of_word, key = bag_of_word.get)
	max_value = bag_of_word[max_key]
	tf_list = []

	for kw in bag_of_word:
		value = (bag_of_word[kw]/(max_value*1.0))
		tf_list.append(value)
	# print(tf_list)

	return tf_list

def idf (titles, word):
	length = len(titles)
	count = 0
	
	for title in titles:
		if word in title:
			count += 1

	# print(word,"  ", count, "  ", math.log(length*1.0/count, 10))
	return math.log(length*1.0/count, 10)

def tf_idf(titles, bag_of_word):
	processed_titles = []
	tf_idf_dict = {}
	tf_idf_list = []
	tf_list = tf(bag_of_word)
	idf_list = []

	for title in titles:
		processed_titles.append(title.lower())

	for word in bag_of_word:
		idf_list.append(idf(processed_titles, word))

	for i in range(len(tf_list)):
		tf_idf_list.append(tf_list[i]*idf_list[i])

	bag_of_word = list(bag_of_word)
	for (word, tf_idf_value) in zip (bag_of_word, tf_idf_list):
		tf_idf_dict[word] = tf_idf_value

	# print (tf_idf_dict)
	return tf_idf_dict

def preprocess_data(titles):
	words = []
	for title in titles:
		words = words + title.split()

	bag_of_word = []
	for word in words:
		word = word.lower()
		if word not in stop_words and word[-1] not in stop_words:
			bag_of_word.append(word)

	bag_of_word = dict(Counter(bag_of_word))

	return bag_of_word

def get_name_of_object_in_image(titles):
	bag_of_word = preprocess_data(titles)

	tf_idf_dict = tf_idf(titles, bag_of_word)
	result_value = tf_idf_dict[min(tf_idf_dict, key = tf_idf_dict.get)]
	
	for key in tf_idf_dict:
		if tf_idf_dict[key] == result_value:
			print(f"Key: {key}")
			return key
	