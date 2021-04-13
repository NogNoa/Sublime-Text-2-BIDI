# This is not actually a valid script, it's just a .py for the highlighting. Trying to run this is at your own risk, responsibility and folly.

class bidiCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view

bidiCommand.view <- bidiCommand.__init__

class View(object):
    def __init__(self, id):
        self.view_id = id
        self.selection = Selection(id)
        self.settings_object = None

class Selection(object):
    def __init__(self, id):
        self.view_id = id


bidiCommand.view.selection.view_id = bidiCommand.view.view_id <- bidiCommand.view.__init__ 

def bidiCommand.run(self, edit):
		region = sublime.Region(0, self.view.size())
		bidiRegion(region, self.view, edit)

bidiCommand.view.size() = return sublime_api.view_size(bidiCommand.view.view_id) = "Returns the number of character in the file."

class Region(object):
    __slots__ = ['a', 'b', 'xpos']

    def __init__(self=bidiCommand.run.region, a=0, b=bidiCommand.view.size(), xpos=-1):
        if b is None:
            b = a
        self.a = a
        self.b = b
        self.xpos = xpos

bidiCommand.run.region = "region for 0 to bidiCommand.view.size()"

def bidiRegion(region=bidiCommand.run.region, view=bidiCommand.view, edit=bidiCommand.run.edit):
	txt = view.substr(region)
	reshaped_text = reshape(txt)
	bdiText = get_display(reshaped_text)
	view.replace(edit, region, bdiText)

bidiRegion.txt = bidiCommand.view.substr(bidiCommand.run.region)

    def substr(self=bidiCommand.view, x=bidiCommand.run.region):
        if isinstance(x, Region):
            return sublime_api.view_cached_substr(self.view_id, x.a, x.b)
        else:
            s = sublime_api.view_cached_substr(self.view_id, x, x + 1)
            # S2 backwards compat
            if len(s) == 0:
                return "\x00"
            else:
                return s


isinstance(x, Region) = isinstance(bidiCommand.run.region, Region) = True
bidiCommand.view.substr(bidiCommand.run.region) = return sublime_api.view_cached_substr(self.view_id, x.a, x.b) = sublime_api.view_cached_substr(bidiCommand.view.view_id, bidiCommand.run.region.a, bidiCommand.run.region.b) = sublime_api.view_cached_substr(bidiCommand.view.view_id, 0, bidiCommand.view.size()) = "another object releted to the substring from 0 to size of bidiCommand.view"

skip(reshaped_text = reshape(txt))

bdiText = get_display(reshaped_text)

def algorithm.get_display(unicode_or_str=bidiRegion.reshaped_text, encoding='utf-8', upper_is_rtl=False,
                base_dir=None, debug=False)

get_display.storage = get_empty_storage()
def algorithm.get_empty_storage():
	    return {
        'base_level': None,
        'base_dir' : None,
        'chars': [],
        'runs' : deque(),
    }
algorithm.get_display.storage ={'base_level': None, 'base_dir' : None, 'chars': [], 'runs' : deque(),}

isinstance(unicode_or_str, str) = isinstance(reshaped_text, str) = False
text = unicode_or_str.decode(encoding) = bidiRegion.reshaped_text.decode('utf-8')
decoded = True

base_dir is None  = True

get_display.base_level = get_base_level(text, upper_is_rtl) = get_base_level(bidiRegion.reshaped_text, False)

def algorithm.get_base_level(text=bidiRegion.reshaped_text, upper_is_rtl=False):

	get_base_level.base_level = None
	prev_surrogate = False
	for _ch in text:
		if _IS_UCS2 and (_SURROGATE_MIN <= ord(_ch) <= _SURROGATE_MAX):
			prev_surrogate = _ch
            continue

algorithm._IS_UCS2 = (sys.maxunicode == 65535)
"for my system it's 1114111"

algorithm._SURROGATE_MIN, algorithm._SURROGATE_MAX = 55296, 56319  # D800, DBFF
"it's what it says, the surrogate planes of unicode"
python.ord(_ch) = "the unicode number of _ch"

        elif prev_surrogate:
            _ch = prev_surrogate + _ch
            prev_surrogate = False

"it let's the computer to use multiple surrogate to make presumebly a single human character, which it presumebly need only if its unicode range is limited i.e it uses utf-16=ucs2"

upper_is_rtl and _ch.isupper() = False

bidi_type = bidirectional(_ch) = "returns the directional beheviour of the character from unicodedata.bidirectional"

if bidi_type in ('AL', 'R') = if bidi_type in ('RIGHT_TO_LEFT_ARABIC', 'RIGHT_TO_LEFT') = True
            base_level = 1
            break
return base_level


get_display.base_level = 1
storage['base_level'] = base_level
storage['base_dir'] = ('L', 'R')[base_level] = ('L', 'R')[1] = 'R'
algorithm.get_display.storage ={'base_level': 1, 'base_dir' : 'R', 'chars': [], 'runs' : deque(),}

get_embedding_levels(text, storage, upper_is_rtl, debug) = get_embedding_levels(bidiRegion.reshaped_text, algorithm.get_display.storage, False, False)

def algorithm.get_embedding_levels(text=bidiRegion.reshaped_text, storage=get_display.storage, upper_is_rtl=False, debug=False):
	prev_surrogate = False
    base_level = storage['base_level']

    for _ch in text:
    	bidi_type = bidirectional(_ch)
    	storage['chars'].append({'ch':_ch, 'level':base_level=1, 'type':bidi_type, 'orig':bidi_type}) 
