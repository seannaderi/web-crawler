from urllib.request import urlopen
from html.parser import HTMLParser

htmlExample = """
<HEAD>
<TITLE>Basic HTML Sample Page</TITLE>
</HEAD>
<BODY BGCOLOR="WHITE">
<CENTER>
<H1>A Simple Sample Web Page</H1>

 

  <IMG SRC="http://sheldonbrown.com/images/scb_eagle_contact.jpeg">

 

 

  <H4>By Sheldon Brown</H4>

<H2>Demonstrating a few HTML features</H2>

</CENTER>

HTML is really a very simple language. It consists of ordinary text, with commands that are enclosed by "<" and ">" characters, or bewteen an "&" and a ";". <P>
 

You don't really need to know much HTML to create a page, because you can copy bits of HTML from other pages that do what you want, then change the text!<P>
 

This page shows on the left as it appears in your browser, and the corresponding HTML code appears on the right. The HTML commands are linked to explanations of what they do.
 

 

<H3>Line Breaks</H3>

HTML doesn't normally use line breaks for ordinary text. A white space of any size is treated as a single space. This is because the author of the page has no way of knowing the size of the reader's screen, or what size type they will have their browser set for.<P>

 

If you want to put a line break at a particular place, you can use the "<BR>" command, or, for a paragraph break, the "<P>" command, which will insert a blank line. The heading command ("<4></4>") puts a blank line above and below the heading text.

 

<H4>Starting and Stopping Commands</H4>

Most HTML commands come in pairs: for example, "<H4>" marks the beginning of a size 4 heading, and "</H4>" marks the end of it. The closing command is always the same as the opening command, except for the addition of the "/".<P>

 

Modifiers are sometimes included along with the basic command, inside the opening command's < >. The modifier does not need to be repeated in the closing command.

 

 

<H1>This is a size "1" heading</H1>

<H2>This is a size "2" heading</H2>

<H3>This is a size "3" heading</H3>

<H4>This is a size "4" heading</H4>

<H5>This is a size "5" heading</H5>

<H6>This is a size "6" heading</H6>

<center>

<H4>Copyright © 1997, by
<A HREF="http://sheldonbrown.com/index.html">Sheldon Brown</A>
</H4>

If you would like to make a link or bookmark to this page, the URL is:<BR> http://sheldonbrown.com/web_sample1.html</body>
"""

#override the HTMLParser 'handle_data' function to get custom behaviours
class ParseHTML(HTMLParser):
    
    def __init__(self):
        self.urlText = []
        super(ParseHTML, self).__init__()
        self.hrefs = set()

    def handle_data(self, data):
        if data is not '\n':
            self.urlText.append(data)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            dict_attrs = dict(attrs)
            if dict_attrs.get('href'):
                self.hrefs.add(dict_attrs['href'])


testParser = ParseHTML()

#url = 'http://www.google.com/'

url = 'http://stackoverflow.com/questions/4981977/how-to-handle-response-encoding-from-urllib-request-urlopen'


handle = urlopen(url)

html_stuff = handle.read().decode(handle.headers.get_content_charset())

testParser.feed(htmlExample)
testParser.close()
#print(htmlExample)
for item in testParser.urlText:
    print(item)
for item in testParser.hrefs:
    print(item)

