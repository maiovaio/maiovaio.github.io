<!DOCTYPE html>
<html lang="en">
	<head>
        <title>Window Creator</title>
		<meta charset="utf-8" />
        <meta content="Windows Error message generator" property="og:title" />
        <meta content="Free and open-source error message generator. Supports Windows XP, Windows 95, Windows 7 and more!" property="og:description" />
        <meta content="https://relt-1.github.io/app.html" property="og:url" />
        <meta content="https://github.com/relt-1/WindowCreator/raw/main/95/Critical%20Error.png" property="og:image" />
        <meta content="#FF0000" data-react-helmet="true" name="theme-color" />
        <meta name="description" content="Free and open-source online error message generator. Supports Windows XP, Windows 95, Windows 7 and more!" />
        <meta name="google-site-verification" content="QR_SBSjEUmXu-LYnybwDFrW7cqzWaFGHMzt0Bqj5574" />
		<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
		<script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        <style>
        canvas{
        margin-left:auto;
        margin-right:auto;
        }
        body{
        background-image: linear-gradient(0deg, transparent 35%, rgba(54, 57, 63) 100%);
        background-color: rgba(28, 29, 30);
        text-align:center;
        }
        input[type="text"],textarea,input[type="number"] {
        border: 1px solid rgba(114,114,114,0.6);
        box-shadow: inset 0 0 0 1px rgba(0,0,0,0.6);
        background: linear-gradient(0deg, transparent 35%, rgba(23,25,27) 100%);
        background-color: rgba(55,58,64);
        border-radius: 5px;
        color: rgba(251,251,251);
        margin-left:auto;
        margin-right:auto;
        }
        ::placeholder{
        color: rgba(114,118,125);
        }
        p{
        color: rgba(251,251,251);
        margin-left:auto;
        margin-right:auto;
        }
        td,tr,th {
        /*border: 3px ridge black;*/
        text-align:center;
        color: rgba(251,251,251);
        }
        th{
        text-align:center;
        background-image: linear-gradient(0deg, transparent 35%, rgba(54, 57, 63) 100%);
        background-color: rgba(28, 29, 30);
        width:12px;
        height:12px;
        padding-left:12px;
        padding-right:12px;
        border-radius: 5px;
        box-shadow: inset 0 0 0 1px rgba(28,29,30), inset 0 0 0 2px rgba(114,114,114,0.8);
        }
        input[type="checkbox"]{
            appearance:none;
            -webkit-appearance:none;
            background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAH0CAYAAAD11uftAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsEAAA7BAbiRa+0AAADMSURBVGhD7ZGxDoMwDAXtMNL/n/upNW2XXIwE6tg79Ix0iU0Uct8fzwDj+57oZY4RzMjMYHpZHGVOZs1BTtqPwizz3jOrXDvn0vpJI9uZZY+VOUvrkRz1RaQWtipM294efqvtTETWr5pTC1swty6ktjPX29udrawLrcL0M+sXIP3MuoGFGrs+J+3rdd76ULfzx8N/3xNKoARKoARKoARKoARKoARKoARKoARKoARKoARKoARKoARKoARKoARKoARKoARKoARKoAR/ISNeM/kIGgP1tiYAAAAASUVORK5CYII=);
            border: 1px solid rgba(88,89,94) !important;
            box-shadow: inset 0 0 3px 3px rgba(0,0,0,0.2);
            color: gray;
            border-radius: 5px;
            width:15px;
            height:15px;
        }
        input[type="checkbox"]:hover{
            background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAH0CAYAAAD11uftAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsAAAA7AAWrWiQkAAADNSURBVGhD7ZFBDoMwDATtcKT/f10fU9P2komRQD12Bq2RJrGJQu774xlgfN8TvcwxghmZGUwvi6PMyaw5yEn7UZhl3ntmlWvnXFo/aWQ7s+yxMmdpPZKjvojUwlaFadvbw2+1nYnI+lVzamEL5taF1Hbmenu7s5V1oVWYfmb9AqSfWTewUGPX56R9vc5bH+p2/nj473tCCZRACZRACZRACZRACZRACZRACZRACZRACZRACZRACZRACZRACZRACZRACZRACZRACZTgL2TEC9CACFYClGVkAAAAAElFTkSuQmCC);
        }
        input[type="checkbox"]:checked{
            background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAH0CAYAAAD11uftAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsEAAA7BAbiRa+0AAAC7SURBVGhD7ZBRCgIxDAXjXs0reCkv3RrYftjZFCn76Qy8LQw1r/HxfL1bgGOcE0fvPZi7N8c5ceT9YG7PLKhntvww9c1SjtkTi/bWgsn2lo1zdtrzw2zsviPzwUj9143CiXr3RVEhIzdjVmueb/v9zrKolJfqzGrN/AmymnnyPbWeOc4JJVACJVACJVACJVACJVACJVACJVACJVACJVACJVACJVACJVACJVACJVACJVACJVACJVCC/5URHxX0nEEyRcPgAAAAAElFTkSuQmCC);
            border: 1px solid rgba(230,230,230,0.6) !important;
            box-shadow: 0 0 3px 3px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(0,0,0,0.6);
            border-radius: 5px;
        }
        input[type="radio"]{
            appearance:none;
            -webkit-appearance:none;
            width:100%;
            height:100%;
            border-top: 1px solid;
            background-color: transparent !important;
            border-image: linear-gradient(to left, #0000 5px,#787878, #0000 calc(100% - 5px)) 1;
            
        }
        input[type="radio"]:hover{
            background: linear-gradient(0deg, transparent 20%, rgba(80,80,80,0.8) 100%);
            background-color: #00000030
            border-radius: 5px !important;
            box-shadow: inset 0 0 0 1px rgba(28,29,30), inset 0 0 0 2px rgba(114,114,114,0.8);
        }
        input[type="radio"]:checked{
            background: linear-gradient(0deg, transparent 20%, rgba(10,10,10,0.8) 100%) !important;
            background-color: rgba(40,40,40,0.8) !important;
            border-radius: 5px !important;
            box-shadow: inset 0 0 0 1px rgba(28,29,30), inset 0 0 0 2px rgba(134,134,134,0.8) !important;
        }
        .wrapper{
            position:relative;
            min-width:64px;
            min-height:64px;
        }
        .background{
            position: absolute;
            top: 0;
            left: 0;
            z-index: 1;
            width:100%;
            height:100%;
        }
        .content{
            position: absolute;
            z-index: 20;
            pointer-events: none;
            width:100%;
            height:100%;
        }
        img{
        position: absolute;
        margin:auto;
        top:0;
        bottom:0;
        left:0;
        right:0;
        }
        button{
            width:200px;
            height:40px;
            background: linear-gradient(0deg, transparent 10%, rgba(67,137,76) 100%);
            background-color: rgba(37,104,46);
            color: white;
            border-radius: 5px;
            border: 1px solid rgba(60,60,60,0.6);
            box-shadow: inset 0 0 0 1px rgba(230,230,230,0.6);
        }
        button:hover{
            background: linear-gradient(0deg, transparent 10%, rgba(87,157,96) 100%);
            background-color: rgba(57,124,66);
        }
        button:active{
            background: linear-gradient(0deg, transparent 10%, rgba(17,84,26) 100%);
            background-color: rgba(47,117,56);
        }
        </style>
	</head>
	<body>
    <p>title:</p>
    <input id="title" type="text" value="" placeholder="title here">
    <p>text:</p>
	<textarea id="text" value="" placeholder="main error text here" style="width: 30%; height: 200px;"></textarea>
    <p>second text:</p>
	<textarea id="subtext" value="" placeholder="second error text here" style="width: 30%; height: 200px;"></textarea>
    <p>icon: </p>
    <form>
    <table style="margin-left:auto;margin-right:auto;">
    <tr>
        <th>Windows
        
        XP</th>
        <th>Windows
        
        7</th>
        <th>Windows
        
        3.1</th>
        <th>Ubuntu
        
        10.04</th>
        <th>Mac OS 9</th>
        </th>
        <th>Windows
        
        95</th>
    </tr>
    <tr>
        <td>
            <div class="wrapper">
                <div class="background">
                    <input type="radio" name="icon" value="xp/Critical Error.png" selected>
                </div>
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/xp/Critical%20Error.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/7/Critical%20Error.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="7/Critical Error.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/3.1/Stop.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="3.1/Stop.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/ubuntu/Error.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="ubuntu/Error.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/mac/hand.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="mac/hand.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/95/Critical%20Error.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="95/Critical Error.png">
                </div>
            </div>
        </td>
    </tr>
    <tr>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/xp/Exclamation.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="xp/Exclamation.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/7/Exclamation.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="7/Exclamation.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/3.1/Exclamation.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="3.1/Exclamation.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/ubuntu/Exclamation.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="ubuntu/Exclamation.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/mac/Exclamation.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="mac/Exclamation.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/95/Exclamation.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="95/Exclamation.png">
                </div>
            </div>
        </td>
    </tr>
    <tr>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/xp/Information.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="xp/Information.png">
                </div>
            </div>
        </td>
         <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/7/Information.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="7/Information.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/3.1/Information.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="3.1/Information.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/ubuntu/Information.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="ubuntu/Information.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/mac/Speech Bubble.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="mac/Speech Bubble.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/95/Information.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="95/Information.png">
                </div>
            </div>
        </td>
    </tr>
    <tr>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/xp/Question.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="xp/Question.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/7/Question Mark.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="7/Question Mark.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/3.1/Question Mark.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="3.1/Question Mark.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/ubuntu/Question Mark.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="ubuntu/Question Mark.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/mac/Speech Bubble Small.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="mac/Speech Bubble Small.png">
                </div>
            </div>
        </td>
        <td>
            <div class="wrapper">
                <div class="content">
                    <img src="https://github.com/relt-1/WindowCreator/raw/main/95/Question.png">
                </div>
                <div class="background">
                    <input type="radio" name="icon" value="95/Question.png">
                </div>
            </div>
        </td>
    </tr>
    </table>
    <input id="customicon" type="text" value="" placeholder="custom url here like https://i.imgur.com/cUoeEc0.png" style="width:500px">
    <div class="wrapper" style="width:128px;height:128px;margin-left:auto;margin-right:auto;">
        <div class="content">
            <img id="customiconimg" src="">
        </div>
        <div class="background">
            <input type="radio" id="customiconradio" name="icon" value="">
        </div>
    </div>
    </form>
    <p>button 1:</p>
    <input id="button1" type="text" value="OK"> <input id="button1style" type="number" value="0" min="0" max="4"> <input id="button1default" type="checkbox">
    <p>button 2:</p>
    <input id="button2" type="text" value=""> <input id="button2style" type="number" value="0" min="0" max="4"> <input id="button2default" type="checkbox">
    <p>button 3:</p>
    <input id="button3" type="text" value=""> <input id="button3style" type="number" value="0" min="0" max="4"> <input id="button3default" type="checkbox">
    <p>active: </p>
    <input id="active" type="checkbox" checked>
    <p>secondary value (different behavior per os): </p>
    <input id="secondary" type="checkbox" checked>
    <p>click the button only ONCE, and wait a while. the first generation takes a minute, but after that it should be faster</p>
    <button id="generate"> Generate! </button>
	<canvas id="xpoutput"></canvas>
    <canvas id="7output"></canvas>
    <canvas id="macoutput"></canvas>
    <canvas id="macalertoutput"></canvas>
    <canvas id="macwindoidoutput"></canvas>
    <canvas id="ubuntuoutput"></canvas>
    <canvas id="3_1output"></canvas>
    <canvas id="taskdialogoutput"></canvas>
    <canvas id="95output"></canvas>
    
    <br />
    <p>theme used from the amazing Skeuocord <a href="https://github.com/Marda33/SkeuoCord">https://github.com/Marda33/SkeuoCord (link)</a></p>
<py-env>
- numpy
- Pillow

</py-env>

<py-script>
from js import console, document, ImageData, Uint8ClampedArray, CanvasRenderingContext2D as Context2d, requestAnimationFrame
#import generate
from pyodide import to_js, create_proxy
from pyodide.http import pyfetch
from numpy import *
from PIL import Image, ImageFont, ImageDraw, ImageMath,ImageChops, ImageOps
from math import ceil,floor
import asyncio
cache = {}
async def imageopenGETBYTES(text):
    text = text.replace("\\","/")
    text = text.replace("//","/")
    text = text.replace("./","")
    if( not text.startswith("http") ):
        url = f"https://raw.githubusercontent.com/relt-1/WindowCreator/main/{text}"
    else:
        url = text
    response = await pyfetch(url)
    if response.status == 200:
        return await response.bytes()
async def imageopenWEB(text):
    global cache
    if text in cache:
        return cache[text]
    else:
        bytes_list = bytearray(await imageopenGETBYTES(text))
        bytes = io.BytesIO(bytes_list) 
        image = Image.open(bytes).convert("RGBA")
        cache[text] = image
        return image
def put(canvas, image,a,b,alignment="00"):
    canvas.alpha_composite(image,(int(a)-( image.size[0] * int(alignment[0]) // 2 ),int(b)-( image.size[1] * int(alignment[1]) // 2) ) )
    return canvas
def put7(canvas, image, a, b, alignment = "00"):  #this is the same as put(), but using windows's weird transparency algorithm. ImageRGB+(BackgroundRGB*ImageAlpha).   this assumes that background alpha is 1(fully opaque), i haven't figured out what it does on a transparent background
    x = int(a)-( image.size[0] * int(alignment[0]) // 2 )
    y = int(b)-( image.size[1] * int(alignment[1]) // 2 )
    cr, cg, cb, ca = canvas.crop((x,y,x+w(image),y+h(image))).split()
    ir, ig, ib, ia = image.split()
    r = ImageMath.eval("convert(  c+(b*(255-a)/255) ,'L')",c=ir,b=cr,a=ia)
    g = ImageMath.eval("convert(  c+(b*(255-a)/255) ,'L')",c=ig,b=cg,a=ia)
    b = ImageMath.eval("convert(  c+(b*(255-a)/255) ,'L')",c=ib,b=cb,a=ia)
    canvas.paste(Image.merge("RGBA",(r,g,b,ca)),(x,y))
    return canvas
#async def ApplyRules(rules,width,height,
def h(img):  #get the height
    return img.size[1]
def w(img):  #get the width
    return img.size[0]
def cropx(img,a,b):  #crop but only x
    return img.crop((a,0,b,h(img)))
def cropy(img,a,b):  #crop but only y
    return img.crop((0,a,x(img),b))

async def createtext(text,fontdirectory,color=(255,255,255,255), buffersize=(1000,1000)):
    drawntext = Image.new("RGBA",buffersize,(255,127,127,0))
    width = 0
    height = 0
    line = 0
    cursorpos = 0
    newlinesize = int(await imageopenGETBYTES(fontdirectory+"newlinesize.txt"))
    for i in text:
        if(i=="\n"):
            height += newlinesize
            line += newlinesize
            cursorpos = 0
            continue
        char = await imageopenWEB(fontdirectory+str(ord(i))+".png")
        whitechar = await imageopenWEB(fontdirectory+"white"+str(ord(i))+".png")
        cred, cgreen, wcblue, calpha = char.split()
        wcred, wcgreen, cblue, wcalpha = whitechar.split()
        alpha2 = ImageMath.eval("convert( int( (r1-r2+255+g1-g2+255+b1-b2+255)/3*alp/255 ), 'L')",r1 = cred,r2 = wcred,b1 = cblue,b2 = wcblue,g1 = cgreen,g2 = wcgreen, alp = (color[3]))
        r = Image.new("L",(w(char),h(char)),color[0])
        g = Image.new("L",(w(char),h(char)),color[1])
        b = Image.new("L",(w(char),h(char)),color[2])
        char = Image.merge("RGBA",(r,g,b,alpha2))
        drawntext.paste(char,(cursorpos,line))
        cursorpos +=w(char)
        width = max(width,cursorpos)
        height = max(height,h(char))
    return drawntext.crop((0,0,width,height))
async def createtextmac(text,fontdirectory,color=(0,0,0,255), buffersize=(1000,1000),underline=False, underlineoffset=0):
    drawntext = Image.new("RGBA",buffersize,(255,127,127,0))
    width = 0
    height = 0
    line = 0
    cursorpos = 0
    newlinesize = int(await imageopenGETBYTES(fontdirectory+"newlinesize.txt"))
    if(underline):
        i = text[0]
        if(i=="\n"):
            height += newlinesize
            line += newlinesize
            cursorpos = 0
        else:
            char = await imageopenWEB(fontdirectory+str(ord(i))+".png")
            char = put(char, Image.new("RGBA",(w(char),1),(255,255,255,255)),0,h(char)-2+underlineoffset)
            colorimg = Image.new("RGBA",(w(char),h(char)),(color[0],color[1],color[2],255))
            char = ImageChops.multiply(char,colorimg)
            drawntext.paste(char,(cursorpos,line))
            cursorpos +=w(char)
            width = max(width,cursorpos)
            height = max(height,h(char))
        text = text[1:]
    for i in text:
        if(i=="\n"):
            height += newlinesize
            line += newlinesize
            cursorpos = 0
            continue
        char = await imageopenWEB(fontdirectory+str(ord(i))+".png")
        colorimg = Image.new("RGBA",(w(char),h(char)),(color[0],color[1],color[2],255))
        char = ImageChops.multiply(char,colorimg)
        drawntext.paste(char,(cursorpos,line))
        cursorpos +=w(char)
        width = max(width,cursorpos)
        height = max(height,h(char))
    return drawntext.crop((0,0,width,height))
async def createtext7(im,x,y,text,fontdirectory,color=(0,0,0,255), buffersize=(1000,1000),align="00", kerningadjust=0, fit=9999999):
    drawntext = Image.new("RGBA",buffersize,(255,255,0,0))
    whitedrawntext = Image.new("RGBA",buffersize,(0,0,255,0))
    width = 0
    height = 0
    line = 0
    cursorpos = 0
    newlinesize = int(await imageopenGETBYTES(fontdirectory+"newlinesize.txt"))
    for i in text:
        if(i=="\n"):
            height += newlinesize
            line += newlinesize
            cursorpos = 0
            continue
        char = await imageopenWEB(fontdirectory+str(ord(i))+".png")
        if(cursorpos+w(char)+kerningadjust > fit):
            height += newlinesize
            line += newlinesize
            cursorpos = 0
            continue
        whitechar = await imageopenWEB(fontdirectory+"white"+str(ord(i))+".png")
        #colorimg = Image.new("RGBA",(w(char),h(char)),(color[0],color[1],color[2],255))
        #char = ImageChops.multiply(char,colorimg)
        drawntext.paste(char,(cursorpos,line))
        whitedrawntext.paste(whitechar,(cursorpos,line))
        cursorpos +=w(char)+kerningadjust
        width = max(width,cursorpos)
        height = max(height,h(char))
    drawntext = drawntext.crop((0,0,width,height))
    drawntext = put(Image.new("RGBA",(w(im),h(im)),(0,0,0,0)),drawntext,x,y,align)
    whitedrawntext = whitedrawntext.crop((0,0,width,height))
    whitedrawntext = put(Image.new("RGBA",(w(im),h(im)),(0,0,0,0)),whitedrawntext,x,y,align)
    imgcolor = Image.new("RGBA",(w(im),h(im)),color)
    c = imgcolor.split()
    ir,ig,ib,ia = im.split()
    r,g,b,a = drawntext.split()
    wr,wg,wb,wa = whitedrawntext.split()
    r = ImageMath.eval("convert( b*c/255+(255-w)*(255-c)/255 ,'L')",w=r,b=wr,c=c[0])
    g = ImageMath.eval("convert( b*c/255+(255-w)*(255-c)/255 ,'L')",w=g,b=wg,c=c[1])
    b = ImageMath.eval("convert( b*c/255+(255-w)*(255-c)/255 ,'L')",w=wb,b=b,c=c[2])
    #imgcolor.show()
    #drawntext.show()
    red = ImageMath.eval("convert( int(((i*(255-t)/255+(c*t)/255)*a/255+i*(255-a)/255)*o/255+(i*(255-o))/255) , 'L')",i=ir,t=r,c=c[0],a=a,o=c[3])   #i is the image RGB,  t is the text RGB,  c is the RGB color variable,  a is the text alpha,  o is the alpha color variable
    #ImageMath.eval("convert( int((255-t)*255/255),'L')",i=ir,t=r,c=c[0]).show()
    green = ImageMath.eval("convert( int(((i*(255-t)/255+(c*t)/255)*a/255+i*(255-a)/255)*o/255+(i*(255-o))/255) , 'L')",i=ig,t=g,c=c[1],a=a,o=c[3])
    blue = ImageMath.eval("convert( int(((i*(255-t)/255+(c*t)/255)*a/255+i*(255-a)/255)*o/255+(i*(255-o))/255) , 'L')",i=ib,t=b,c=c[2],a=a,o=c[3])
    alpha = ImageMath.eval("convert( int(((((r+g+b)/3+(255-(r+g+b)/3)*i/255))*t/255+(i*(255-t))/255)*o/255+(i*(255-o))/255) , 'L')",i=ia,r=r,g=g,b=b,t=a,o=c[3]) #i is the image alpha,  r,g,b are RGB values of the text,  t is text alpha,  o is color alpha
    result = Image.merge("RGBA",(red,green,blue,alpha))
    return result

async def measuretext7(text,fontdirectory, buffersize=(1000,1000), kerningadjust=0, fit=9999999): #this gives width and height of text using windows 7 rendering
    #drawntext = Image.new("RGBA",buffersize,(255,127,127,0))
    width = 0
    height = 0
    line = 0
    cursorpos = 0
    newlinesize = int(await imageopenGETBYTES(fontdirectory+"newlinesize.txt"))
    for i in text:
        if(i=="\n"):
            height += newlinesize
            line += newlinesize
            cursorpos = 0
            continue
        char = await imageopenWEB(fontdirectory+str(ord(i))+".png")
        if(cursorpos+w(char)+kerningadjust > fit):
            height += newlinesize
            line += newlinesize
            cursorpos = 0
            continue
        #colorimg = Image.new("RGBA",(w(char),h(char)),(color[0],color[1],color[2],255))
        #char = ImageChops.multiply(char,colorimg)
        #drawntext.paste(char,(cursorpos,line))
        cursorpos +=w(char)+kerningadjust
        width = max(width,cursorpos)
        height = max(height,h(char))
    return [width,height]

async def createtextubuntu(im,x,y,text,fontdirectory,color=(0,0,0,255), buffersize=(1000,1000),align="00"):
    drawntext = Image.new("RGBA",buffersize,(255,255,0,0))
    width = 0
    height = 0
    line = 0
    cursorpos = 0
    newlinesize = int(await imageopenGETBYTES(fontdirectory+"newlinesize.txt"))
    for i in text:
        if(i=="\n"):
            height += newlinesize
            line += newlinesize
            cursorpos = 0
            continue
        char = await imageopenWEB(fontdirectory+str(ord(i))+".png")
        #colorimg = Image.new("RGBA",(w(char),h(char)),(color[0],color[1],color[2],255))
        #char = ImageChops.multiply(char,colorimg)
        drawntext.paste(char,(cursorpos,line))
        cursorpos +=w(char)
        width = max(width,cursorpos)
        height = max(height,h(char))
    drawntext = drawntext.crop((0,0,width,height))
    drawntext = put(Image.new("RGBA",(w(im),h(im)),(0,0,0,0)),drawntext,x,y,align)
    imgcolor = Image.new("RGBA",(w(im),h(im)),color)
    c = imgcolor.split()
    ir,ig,ib,ia = im.split()
    r,g,b,a = drawntext.split()
    #imgcolor.show()
    red = ImageMath.eval("convert( int(((i*(255-t)/255+(c*t)/255)*a/255+i*(255-a)/255)*o/255+(i*(255-o))/255) , 'L')",i=ir,t=r,c=c[0],a=a,o=c[3])   #i is the image RGB,  t is the text RGB,  c is the RGB color variable,  a is the text alpha,  o is the alpha color variable
    #ImageMath.eval("convert( int((255-t)*255/255),'L')",i=ir,t=r,c=c[0]).show()
    green = ImageMath.eval("convert( int(((i*(255-t)/255+(c*t)/255)*a/255+i*(255-a)/255)*o/255+(i*(255-o))/255) , 'L')",i=ig,t=g,c=c[1],a=a,o=c[3])
    blue = ImageMath.eval("convert( int(((i*(255-t)/255+(c*t)/255)*a/255+i*(255-a)/255)*o/255+(i*(255-o))/255) , 'L')",i=ib,t=b,c=c[2],a=a,o=c[3])
    alpha = ImageMath.eval("convert( int(((((r+g+b)/3+(255-(r+g+b)/3)*i/255))*t/255+(i*(255-t))/255)*o/255+(i*(255-o))/255) , 'L')",i=ia,r=r,g=g,b=b,t=a,o=c[3]) #i is the image alpha,  r,g,b are RGB values of the text,  t is text alpha,  o is color alpha
    result = Image.merge("RGBA",(red,green,blue,alpha))
    return result

def resize(im,width,height,left,right,up,down,scalingmethod=Resampling.NEAREST):  #this resizes image but keeps margins intact. think of Unity GUI elements
    if width < w(im):
        im = im.resize((width,h(im)),scalingmethod)
        left = 1
        right = 1
    if height < h(im):
        im = im.resize((w(im),height),scalingmethod)
        up = 1
        down = 1
    result = Image.new("RGBA",(width,height),(0,0,0,0))
    tl = im.crop((0,0,left,up))
    tm = im.crop((left,0,w(im)-right,up))
    tr = im.crop((w(im)-right,0,w(im),up))
    ml = im.crop((0,up,left,h(im)-down))
    mm = im.crop((left,up,w(im)-right,h(im)-down))
    mr = im.crop((w(im)-right,up,w(im),h(im)-down))
    dl = im.crop((0,h(im)-down,left,h(im)))
    dm = im.crop((left,h(im)-down,w(im)-right,h(im)))
    dr = im.crop((w(im)-right,h(im)-down,w(im),h(im)))
    result = put(result,tl,0,0)
    result = put(result,tm.resize((width-left-right,h(tm)),scalingmethod),left,0)
    result = put(result,tr,width,0,"20")
    result = put(result,ml.resize((w(ml),height-up-down),scalingmethod),0,up)
    result = put(result,mm.resize((width-left-right,height-up-down),scalingmethod),left,up)
    result = put(result,mr.resize((w(mr),height-up-down),scalingmethod),width,up,"20")
    result = put(result,dl,0,height,"02")
    result = put(result,dm.resize((width-left-right,h(dm)),scalingmethod),left,height,"02")
    result = put(result,dr,width,height,"22")
    return result

def resizeanchor(im,x1,y1,x2,y2,left,right,up,down,scalingmethod=Resampling.NEAREST):  #this is resize, but you give it desired coordinates and it calculates the size the image should be
    return resize(im,x2-x1,y2-y1,left,right,up,down,scalingmethod)

def tile(im,width,height):    #this tiles an image
    result = Image.new("RGBA",(width,height),(0,0,0,0))
    for x in range(ceil(width/w(im))):
        for y in range(ceil(height/h(im))):
            result = put(result,im,x*w(im),y*h(im))
    return result

#the button functions return an image of a button for the OS.

async def CreateXPButton(text,style=0):
    styles = ["xp/Button.png","xp/Button Hovered.png","xp/Button Clicked.png","xp/Button Disabled.png","xp/Button Default.png"]
    style = min(style,len(styles)-1)
    Button = await imageopenWEB(styles[style])
    col = (0,0,0,255)
    if(style==3):
        col = (161,161,146,255)
    textgraphic = await createtext(text,".\\xp\\fonts\\text\\",col)
    Button = resize(Button,max(w(textgraphic)+16,75),max(23,h(textgraphic)+10),8,8,9,9,Resampling.NEAREST)
    Button = put(Button,textgraphic,w(Button)//2-w(textgraphic)//2,5)
    return Button

async def CreateMacButton(text,style=0):
    styles = ["mac/Button.png","mac/Button Disabled.png"]
    style = min(style,len(styles)-1)
    Button = await imageopenWEB(styles[style])
    col = (0,0,0,255)
    if(style==1):
        col = (161,161,146,255)
        textgraphic = await createtextmac(text,".\\mac\\fonts\\caption\\",col)
        Button = resize(Button,max(w(textgraphic)+10,60),max(20,h(textgraphic)+4),2,2,2,2,Resampling.NEAREST)
    else:
        textgraphic = await createtextmac(text,".\\mac\\fonts\\caption\\",col)
        Button = resize(Button,max(w(textgraphic)+10,60),max(20,h(textgraphic)+4),4,4,4,4,Resampling.NEAREST)
    Button = put(Button,textgraphic,floor(w(Button)/2-w(textgraphic)/2),2)
    return Button

async def Create7Button(text,style=0):
    styles = ["7/Button.png","7/Button.png","7/Button.png","7/Button Disabled.png","7/Button Defaulted.png","7/Button Defaulted Animation.png"]
    Button = await imageopenWEB(styles[min(style,len(styles)-1)])
    col = (0,0,0,255)
    #if(style==3):
    #    col = (161,161,146,255)
    #textgraphic = await createtext(text,".\\7\\fonts\\text\\",col)
    textsize = await measuretext7(text,"7\\fonts\\text\\",kerningadjust=-1)
    Button = resize(Button,max(textsize[0]+16,86),max(24,textsize[1]+9),3,3,3,3,Resampling.NEAREST)
    Button = await createtext7(Button,w(Button)//2-textsize[0]//2,4,text,"7\\fonts\\text\\",kerningadjust=-1)
    return Button

async def Create7TaskDialogButton(text,style=0):
    styles = ["7/Button.png","7/Button.png","7/Button.png","7/Button Disabled.png","7/Button Defaulted.png","7/Button Defaulted Animation.png"]
    Button = await imageopenWEB(styles[min(style,len(styles)-1)])
    col = (0,0,0,255)
    #if(style==3):
    #    col = (161,161,146,255)
    #textgraphic = await createtext(text,".\\7\\fonts\\text\\",col)
    textsize = await measuretext7(text,"7\\fonts\\text\\",kerningadjust=-1)
    Button = resize(Button,max(textsize[0]+30,66),max(21,textsize[1]+6),3,3,3,3,Resampling.NEAREST)
    Button = await createtext7(Button,w(Button)//2-textsize[0]//2,3,text,"7\\fonts\\text\\",kerningadjust=-1)
    return Button

async def Create3_1Button(text,style=0,underline=False):
    styles = ["3.1/Button.png","3.1/Button Default.png"]
    style = min(style,len(styles)-1)
    Button = await imageopenWEB(styles[style])
    textgraphic = await createtextmac(text,"3.1//fonts//text//",underline=underline)
    if style == 1:
        Button = resize(Button,max(58,w(textgraphic)+5+5),h(textgraphic)+6+6,4,4,4,4)
        Border = await imageopenWEB("3.1//Button Text Outline.png")
        BorderImg = tile(Border,max(58,w(textgraphic)+5+5),h(textgraphic)+6+6)
        textx = floor(w(Button)/2-w(textgraphic)/2-1)
        textendx = textx+w(textgraphic)
        Button = put(Button,textgraphic,textx,6,"00")
        Button = put(Button,BorderImg.crop((textx-2,      6,                   textx-1,            7+h(textgraphic))),   textx-2,    6)
        Button = put(Button,BorderImg.crop((textx-1,      7+h(textgraphic),    textendx,           7+h(textgraphic)+1)), textx-1,    7+h(textgraphic))
        Button = put(Button,BorderImg.crop((textendx+1,   6,                   textendx+2,         7+h(textgraphic))),   textendx+1, 6)
        Button = put(Button,BorderImg.crop((textx-1,      5,                   textendx,           6)),                  textx-1,    5)
    else:
        Button = resize(Button,max(58,w(textgraphic)+6+6),h(textgraphic)+6+6,3,3,3,3)
        Button = put(Button,textgraphic,floor(w(Button)/2-w(textgraphic)/2-1),6,"00")
    return Button

async def CreateUbuntuButton(text,style=0,predefinedsize=[]):
    styles = ["ubuntu/Button.png","ubuntu/Button Default.png"]
    Button = await imageopenWEB(styles[min(style,len(styles)-1)])
    if predefinedsize:
        size = predefinedsize
    else:
        size = await measuretext7(text,"ubuntu/fonts/text/")
        size[0] += 16
        size[1] += 10
        size[0] = max(85,size[0])
        size[1] = max(29,size[1])
    Button = resize(Button,size[0],size[1],5,5,5,5,scalingmethod=Image.BICUBIC)
    Button = await createtextubuntu(Button, size[0]//2, size[1]//2, text, "ubuntu/fonts/text/",(60,59,55,255),align="11")
    return Button

async def Create95Button(text,style=0,underline=False):
    styles = ["95/Button.png","95/Button Default.png"]
    style = min(style,len(styles)-1)
    Button = await imageopenWEB(styles[style])
    textgraphic = await createtextmac(text,"95//fonts//text//",underline=underline,underlineoffset=1)
    if style == 1:
        Button = resize(Button,max(75,w(textgraphic)+5+5),h(textgraphic)+6+4,3,3,3,3)
        Border = await imageopenWEB("95//Button Text Outline.png")
        BorderImg = tile(Border,max(75,w(textgraphic)+5+5),h(textgraphic)+6+4)
        textx = floor(w(Button)/2-w(textgraphic)/2)
        outx = 4
        outendx = max(75,w(textgraphic)+5+5)-4
        #BorderImg.show()
        Button = put(Button,textgraphic,textx,4)
        Button = put(Button,BorderImg.crop((outx,      4,                   outx+1,            6+h(textgraphic))),   outx,    4)
        Button = put(Button,BorderImg.crop((outx,      5+h(textgraphic),    outendx,           5+h(textgraphic)+1)), outx,    5+h(textgraphic))
        Button = put(Button,BorderImg.crop((outendx-1,   4,                   outendx,         6+h(textgraphic))),   outendx-1, 4)
        Button = put(Button,BorderImg.crop((outx,      4,                   outendx,           5)),                  outx,    4)
    else:
        Button = resize(Button,max(75,w(textgraphic)+5+5),h(textgraphic)+4+6,2,2,2,2)
        Button = put(Button,textgraphic,floor(w(Button)/2-w(textgraphic)/2),4)
    return Button

async def CreateXPWindow(width,height,captiontext="",active=True,insideimagepath = "",erroriconpath="",errortext="",button1="",button2="",button3="",button1style=0,button2style=0,button3style=0):
    #brug = open("./brug.txt")
    #print(brug.read())
    if active:
        TopFrame = await imageopenWEB("./xp/Frame Up Active.png")
        LeftFrame = await imageopenWEB("./xp/Frame Left Active.png")
        RightFrame = await imageopenWEB("./xp/Frame Right Active.png")
        BottomFrame = await imageopenWEB("./xp/Frame Bottom Active.png")
        CloseButton = await imageopenWEB("./xp/Close button.png")
    else:
        TopFrame = await imageopenWEB("./xp/Frame Up Inactive.png")
        LeftFrame = await imageopenWEB("./xp/Frame Left Inactive.png")
        RightFrame = await imageopenWEB("./xp/Frame Right Inactive.png")
        BottomFrame = await imageopenWEB("./xp/Frame Bottom Inactive.png")
        CloseButton = await imageopenWEB("./xp/Close button Inactive.png")
        button1style = button1style*(button1style != 4)
        button2style = button2style*(button2style != 4) 
        button3style = button3style*(button3style != 4)
    textposx = 15+3
    textposy = 11+h(TopFrame)
    
    captiontextwidth = w(await createtext(captiontext,".\\xp\\fonts\\caption\\"))
    width = max(width,captiontextwidth+43)
    createdtext = await createtext(errortext,".\\xp\\fonts\\text\\",(0,0,0,255))
    #textposy -= min(15,h(createdtext)//2)
    width = max(width,w(createdtext)+textposx+8+3)
    height = max(height,h(createdtext)+h(TopFrame)+3+25)
    print(textposy)
    if(insideimagepath != ""):
        insideimage = await imageopenWEB(insideimagepath)
        height = max(h(insideimage)+h(TopFrame)+3,height)
        width = max(width,w(insideimage)+6)
    if(erroriconpath != ""):
        erroricon = await imageopenWEB(erroriconpath)
        textposx += 15+w(erroricon)
        textposy = max(textposy,11+floor(h(erroricon)/2-h(createdtext)/2)+h(TopFrame))
        height = max(height,h(erroricon)+h(TopFrame)+3+11+11+3)
        width += 14+w(erroricon)
        
    buttonsimage = Image.new("RGBA",(0,0),(0,0,0,0))
    buttonswidth = 0
    buttonsheight = 0
    if button1 != "":
        buttonswidth += 11
        
        button1img = await CreateXPButton(button1,button1style)
        #IMAGE = put(IMAGE,button1img,3+12,height-3-12,"02")
        buttonsheight = max(buttonsheight,h(button1img)+14)
        temp = Image.new("RGBA",(buttonswidth+w(button1img),buttonsheight),(0,0,0,0))
        temp = put(temp,buttonsimage,0,0)
        temp = put(temp,button1img,buttonswidth,3)
        buttonsimage = temp.copy()
        buttonswidth += w(button1img)
        if button2 != "":
            buttonswidth += 6
            button2img = await CreateXPButton(button2,button2style)
            #IMAGE = put(IMAGE,button2img,3+12,height-3-12,"02")
            buttonsheight = max(buttonsheight,h(button2img)+14)
            temp = Image.new("RGBA",(buttonswidth+w(button2img),buttonsheight),(0,0,0,0))
            temp = put(temp,buttonsimage,0,0)
            temp = put(temp,button2img,buttonswidth,3)
            buttonsimage = temp.copy()
            buttonswidth += w(button2img)
            if button3 != "":
                buttonswidth += 6
                button3img = await CreateXPButton(button3,button3style)
                #IMAGE = put(IMAGE,button2img,3+12,height-3-12,"02")
                buttonsheight = max(buttonsheight,h(button3img)+14)
                temp = Image.new("RGBA",(buttonswidth+w(button3img),buttonsheight),(0,0,0,0))
                temp = put(temp,buttonsimage,0,0)
                temp = put(temp,button3img,buttonswidth,3)
                buttonsimage = temp.copy()
                buttonswidth += w(button3img)
        width = max(width,buttonswidth+12)
        height += buttonsheight
    #buttonswidth.show()
    
    width = max(66,width)
    IMAGE = Image.new("RGBA", (width,height), (236,233,216,0))
    #IMAGE = put(IMAGE,cropx(TopFrame,0,27),0,0,"00")
    #IMAGE = put(IMAGE,cropx(TopFrame,28,31).resize((width-w(TopFrame)+4,h(TopFrame)),Resampling.NEAREST),27,0,"00")
    #IMAGE = put(IMAGE,cropx(TopFrame,31,w(TopFrame)),width,0,"20")
    IMAGE = put(IMAGE,resize(TopFrame,width,h(TopFrame),28,35,9,17,Resampling.NEAREST),0,0)
    IMAGE = put(IMAGE,LeftFrame.resize((3,height-h(TopFrame)-3),Resampling.NEAREST),0,h(TopFrame),"00")
    IMAGE = put(IMAGE,RightFrame.resize((3,height-h(TopFrame)-3),Resampling.NEAREST),width,h(TopFrame),"20")
    IMAGE = put(IMAGE,cropx(BottomFrame,0,5).resize((5,3),Resampling.NEAREST),0,height,"02")
    IMAGE = put(IMAGE,cropx(BottomFrame,4,w(BottomFrame)-5).resize((width-10,3),Resampling.NEAREST),5,height,"02")
    IMAGE = put(IMAGE,cropx(BottomFrame,w(BottomFrame)-5,w(BottomFrame)).resize((5,3),Resampling.NEAREST),width,height,"22")
    IMAGE = put(IMAGE,Image.new("RGBA", (width-6,height-3-h(TopFrame)), (236,233,216,255)),3,h(TopFrame),"00")
    IMAGE = put(IMAGE,CloseButton,width-5,5,"20")
    if active:
        IMAGE = put(IMAGE,await createtext(captiontext,".\\xp\\fonts\\captionshadow\\",(10,24,131,255)),8,8,"00")
        IMAGE = put(IMAGE,await createtext(captiontext,".\\xp\\fonts\\caption\\"),7,7,"00")
    else:
        IMAGE = put(IMAGE,await createtext(captiontext,".\\xp\\fonts\\caption\\",(216,228,248,255)),7,7,"00")
    if(insideimagepath != ""):
        IMAGE = put(IMAGE,insideimage,3,h(TopFrame))
    if(erroriconpath != ""):
        IMAGE = put(IMAGE,erroricon,3+11,h(TopFrame)+11)
    IMAGE = put(IMAGE,await createtext(errortext,".\\xp\\fonts\\text\\",(0,0,0,255)),textposx,textposy)
    IMAGE = put(IMAGE,buttonsimage,width//2-5,height-3,"12")
    return IMAGE

async def CreateMacAlertDialog(width,height,title="",bar=True,icon="",errortext="",subtext="",button1="",button2="",button3="",button1default=False,button2default=False,button3default=False,button1style=0,button2style=0,button3style=0):
    WindowBar = await imageopenWEB("mac/Error Window With bar.png")
    WindowNoBar = await imageopenWEB("mac/Error Window No bar.png")
    Ridges = await imageopenWEB("mac/Red Ridges.png")
    ButtonBorder = await imageopenWEB("mac//Button Outline.png")
    TextHeight = 0
    IconPadding = 0
    Paddingwidth = 7
    if(bar):
        Paddingheight = 29+4
        Barheight = 29
    else:
        Paddingheight = 3+4
        Barheight = 0
    if(errortext != ""):
        ErrorTextImg = await createtextmac(errortext,"mac//fonts//caption//")
        width = max(width,w(ErrorTextImg)+79+90)
        #height = max(height,h(ErrorTextImg)+Paddingheight+20)
        TextHeight += h(ErrorTextImg)
    if(subtext != ""):
        SubTextImg = await createtextmac(subtext,"mac//fonts//text//")
        SubTextPos = TextHeight
        width = max(width,w(SubTextImg)+79+90)
        TextHeight += h(SubTextImg)
    height += TextHeight + Paddingheight
    if(icon != ""):
        IconImg = await imageopenWEB(icon)
        height = max(height,h(IconImg)+Paddingheight)
        width += w(IconImg)
        IconPadding = w(IconImg)
    buttonswidth = 0
    if(button1 != ""):
        height += 60
        button1img = await CreateMacButton(button1,button1style)
        buttonswidth += w(button1img)
        if(button2 != ""):
            button2img = await CreateMacButton(button2,button2style)
            buttonswidth += w(button2img)
            if(button3 != ""):
                button3img = await CreateMacButton(button3,button3style)
                buttonswidth += w(button3img)
    width = max(width,buttonswidth+79+90)
    IMAGE = Image.new("RGBA", (width,height), (236,233,216,0))
    if(bar):
        IMAGE = put(IMAGE,resize(WindowBar,width,height,3,4,24,4),0,0)
    else:
        IMAGE = put(IMAGE,resize(WindowNoBar,width,height,3,4,3,4),0,0)
    if bar:
        if(title == ""):
            IMAGE = put(IMAGE,resizeanchor(Ridges,5,4,width-6,16,1,1,1,1),5,4)
        else:
            TitleImage = await createtextmac(title,"mac//fonts//caption//")
            IMAGE = put(IMAGE,TitleImage,width//2-w(TitleImage)//2,3)
            IMAGE = put(IMAGE,resizeanchor(Ridges,5,4,width//2-w(TitleImage)//2-3,16,1,1,1,1),5,4)
            IMAGE = put(IMAGE,resizeanchor(Ridges,width//2+w(TitleImage)//2+5,4,width-6,16,1,1,1,1),width//2+w(TitleImage)//2+5,4)
    if(icon != ""):
        IMAGE = put(IMAGE,IconImg,26,Barheight+15)
    if(errortext != ""):
        IMAGE = put(IMAGE,ErrorTextImg,47+IconPadding,Barheight+14)
    if(subtext != ""):
        IMAGE = put(IMAGE,SubTextImg,47+IconPadding,Barheight+SubTextPos+16)
    if(button1 != ""):
        button1img = await CreateMacButton(button1,button1style)
        IMAGE = put(IMAGE,button1img,width-17,height-17,"22")
        if(button1default):
            button1border = resize(ButtonBorder,w(button1img)+6,h(button1img)+6,5,5,5,5)
            IMAGE = put(IMAGE,button1border,width-17+3,height-17+3,"22")
        if(button2 != ""):
            button2img = await CreateMacButton(button2,button2style)
            IMAGE = put(IMAGE,button2img,width-17-w(button1img)-22,height-17,"22")
            if(button2default):
                button2border = resize(ButtonBorder,w(button2img)+6,h(button2img)+6,5,5,5,5)
                IMAGE = put(IMAGE,button2border,width-17+3-w(button1img)-22,height-17+3,"22")
            if(button3 != ""):
                button3img = await CreateMacButton(button3,button3style)
                IMAGE = put(IMAGE,button3img,width-17-w(button2img)-22-w(button1img)-22,height-17,"22")
                if(button3default):
                    button3border = resize(ButtonBorder,w(button3img)+6,h(button3img)+6,5,5,5,5)
                    IMAGE = put(IMAGE,button3border,width-17+3-w(button2img)-22-w(button1img)-22,height-17+3,"22")
    return IMAGE

async def CreateMacWindow(width,height,title="",icon="",errortext="",button1="",button2="",button3="",button1default=False,button2default=False,button3default=False,button1style=0,button2style=0,button3style=0):
    WindowBar = await imageopenWEB("mac/Window With bar.png")
    Ridges = await imageopenWEB("mac/Ridges.png")
    ButtonBorder = await imageopenWEB("mac//Button Outline.png")
    Paddingheight = 29+4
    TextHeight = 0
    iconsize = 0
    if(icon != ""):
        IconImg = await imageopenWEB(icon)
        iconsize = w(IconImg)+26
    if(errortext != ""):
        ErrorTextImg = await createtextmac(errortext,"mac//fonts//caption//")
        width = max(width,w(ErrorTextImg)+iconsize+20+20+100)
        #height = max(height,h(ErrorTextImg)+Paddingheight+20)
        TextHeight += h(ErrorTextImg)+36
    #if(subtext != ""):
    #    SubTextImg = await createtextmac(subtext,"mac//fonts//text//")
    #    width = max(width,w(SubTextImg)+79+90)
    #    TextHeight += h(SubTextImg)
    height += TextHeight+24+4
    if(button1 != ""):
        height += 17+17
    IMAGE = Image.new("RGBA", (width,height), (236,233,216,0))
    IMAGE = put(IMAGE,resize(WindowBar,width,height,3,4,24,4),0,0)
    if(title == ""):
        IMAGE = put(IMAGE,resizeanchor(Ridges,5,4,width-6,16,1,1,1,1),5,4)
    else:
        TitleImage = await createtextmac(title,"mac//fonts//caption//")
        IMAGE = put(IMAGE,TitleImage,width//2-w(TitleImage)//2,3)
        IMAGE = put(IMAGE,resizeanchor(Ridges,5,4,width//2-w(TitleImage)//2-3,16,1,1,1,1),5,4)
        IMAGE = put(IMAGE,resizeanchor(Ridges,width//2+w(TitleImage)//2+5,4,width-6,16,1,1,1,1),width//2+w(TitleImage)//2+5,4)
    if(icon != ""):
        IMAGE = put(IMAGE,IconImg,26,37)
    if(errortext != ""):
        IMAGE = put(IMAGE,ErrorTextImg,iconsize+20,36)
    if(button1 != ""):
        button1img = await CreateMacButton(button1,button1style)
        IMAGE = put(IMAGE,button1img,width-17,height-17,"22")
        if(button1default):
            button1border = resize(ButtonBorder,w(button1img)+6,h(button1img)+6,5,5,5,5)
            IMAGE = put(IMAGE,button1border,width-17+3,height-17+3,"22")
        if(button2 != ""):
            button2img = await CreateMacButton(button2,button2style)
            IMAGE = put(IMAGE,button2img,width-17-w(button1img)-22,height-17,"22")
            if(button2default):
                button2border = resize(ButtonBorder,w(button2img)+6,h(button2img)+6,5,5,5,5)
                IMAGE = put(IMAGE,button2border,width-17+3-w(button1img)-22,height-17+3,"22")
            if(button3 != ""):
                button3img = await CreateMacButton(button3,button3style)
                IMAGE = put(IMAGE,button3img,width-17-w(button2img)-22-w(button1img)-22,height-17,"22")
                if(button3default):
                    button3border = resize(ButtonBorder,w(button3img)+6,h(button3img)+6,5,5,5,5)
                    IMAGE = put(IMAGE,button3border,width-17+3-w(button2img)-22-w(button1img)-22,height-17+3,"22")
    return IMAGE

async def CreateMacWindoid(icon="",text="",collapsed=False):
    contentwidth = 0
    contentheight = 0
    textpos = 6
    if(text != ""):
        TextImg = await createtextmac(text,"mac//fonts//text//")
        contentwidth += w(TextImg)+7
        contentheight += h(TextImg)+3
    if(icon != ""):
        IconImg = await imageopenWEB(icon)
        contentwidth += w(IconImg) + 7
        contentheight = max(contentheight,h(IconImg))
        textpos += w(IconImg) + 7
    contentwidth += 12
    contentheight += 8
    CONTENT = Image.new("RGBA",(contentwidth,contentheight),(255,255,198))
    if(text != ""):
        CONTENT = put(CONTENT,TextImg,textpos,5)
    if(icon != ""):
        CONTENT = put(CONTENT,IconImg,6,4)
    Border = await imageopenWEB("mac//Windoid.png")
    CollapsedBorder = await imageopenWEB("mac//Windoid Hidden.png")
    Studs = await imageopenWEB("mac//Studs.png")
    CloseButton = await imageopenWEB("mac//Windoid Close Button.png")
    HideButton = await imageopenWEB("mac//Windoid Hide Button.png")
    width = contentwidth + 19
    height = contentheight + 9
    IMAGE = Image.new("RGBA",(width,height),(0,0,0,0))
    if not collapsed:
        IMAGE = put(IMAGE,resize(Border,width,height,14,5,4,5),0,0)
        IMAGE = put(IMAGE,CONTENT,14,4)
        IMAGE = put(IMAGE,CloseButton,2,2)
        IMAGE = put(IMAGE,HideButton,2,height-3,"02")
        IMAGE = put(IMAGE,tile(Studs,8,height-14-15),3,14)
    else:
        IMAGE = put(IMAGE,resize(CollapsedBorder,15,height,2,3,2,3),0,0)
        IMAGE = put(IMAGE,CloseButton,2,2)
        IMAGE = put(IMAGE,HideButton,2,height-3,"02")
        IMAGE = put(IMAGE,tile(Studs,8,height-14-15),3,14)
    return IMAGE

async def mix(a,b,c):     #smoothly mixes between two values.
    c = min(1,max(0,c))
    c = c**0.5
    return a*(1-c)+b*c


#this function just takes a corner and squishes it based on width and the height of the image by some amount.
#amount of 3 will put it in the width/3,height/3 position
#amount of 7 will put it in the width/7,height/7 position and so on.
#c is there to animate the translation, from 0 - fully translated, to 1 - no translation
async def stretch(size,amount,c):   
    result = size-size*(size/(size-size/amount)) #this is needed because deform() does the opposite of what you would think it will do, it takes 4 points, and then squishes them into a rectangle.
    return mix(result,0,c)

class Windows7Anim:
    async def __init__(self,second):
        self.second = second
    
    async def getmesh(self, img):
        return [((0,0,w(img),h(img)),(stretch(w(img),30,self.second*4),stretch(h(img),56,self.second*4),
                                      stretch(w(img),18,self.second*4),h(img)-stretch(h(img),16,self.second*4),
                                      w(img)-stretch(w(img),18,self.second*4),h(img)-stretch(h(img),16,self.second*4),
                                      w(img)-stretch(w(img),30,self.second*4),stretch(h(img),56,self.second*4)))]  #values arbitrary, somebody needs to look into dwm and find how it animates the window

async def Create7Window(icon="",text="",title="",pos=(0,0),screenres=(1920,1080),wallpaper="",buttons=[]):
    #pos and screenres dictate the glass texture position and size on the window border
    #if wallpaper is not empty, it will composite the error onto an image at pos's coordinates, screenres should be the same size as the wallpaper
    contentwidth = 106
    contentheight = 53
    textpos = 0
    textposy = 25+13
    print("1")
    if(text != ""):
        TextDim = await measuretext7(text,"7//fonts//text//",kerningadjust=-1)
        contentwidth = max(contentwidth,TextDim[0]+38+12)
        contentheight += TextDim[1]
        textposy = textposy-min(TextDim[1],21)
    if(icon != ""):
        IconImg = await imageopenWEB(icon)
        contentwidth = max(contentwidth,w(IconImg)+25+25)
        contentheight = max(contentheight,h(IconImg)+26+26)
        textpos += w(IconImg)-4+25
        textposy += h(IconImg)//2-7
        if(text != ""):
            contentwidth = max(contentwidth,w(IconImg)+25+TextDim[0]+38+9)
    print("2")
    if(title != ""):
        TitleDim = await measuretext7(title,"7//fonts//text//",kerningadjust=-1)
        contentwidth = max(contentwidth,TitleDim[0]+49)
    buttonswidth = 0
    #len(buttons)*95
    for i in buttons:
        tempbuttontextsize = await measuretext7(i[0],"7\\fonts\\text\\",kerningadjust=-1)
        buttonswidth += max(tempbuttontextsize[0]+16,86) + 10
    if(buttons):
        contentheight += 49
        contentwidth = max(contentwidth,buttonswidth+43)
    print("3")
    CONTENT = Image.new("RGBA",(contentwidth,contentheight),(255,255,255))
    if(icon != ""):
        CONTENT = put(CONTENT,IconImg,25,26)
    if(text != ""):
        CONTENT = await createtext7(CONTENT,textpos+12,textposy,text,"7//fonts//text//",kerningadjust=-1)
    if(buttons):
        CONTENT = put(CONTENT, Image.new("RGBA",(contentwidth,49),(240,240,240)),0,contentheight,"02")
    buttonpos = 0
    print("4")
    for i in buttons:
        buttonpos += 10
        Button = await Create7Button(i[0],i[1])
        CONTENT = put7(CONTENT, Button, contentwidth-buttonpos,contentheight-12,"22")
        buttonpos += w(Button)
    Window = await imageopenWEB("7//Window.png")
    CloseButton = await imageopenWEB("7//Close Button Single.png")
    CloseSymbol = await imageopenWEB("7//Close Symbol.png")
    GlassImg = await imageopenWEB("7//Glass.png")
    GlassMask = await imageopenWEB("7//Glass Mask.png")
    print("5")
    TextGlow = await imageopenWEB("7//Text Glow.png")
    SideGlowLeft = await imageopenWEB("7//Sideglow 1 Left.png")
    SideGlowRight = await imageopenWEB("7//Sideglow 1 Right.png")
    SideShine = await imageopenWEB("7//Side Shine.png")
    print("6")
    width = contentwidth+8+8
    height = contentheight+8+30
    GlassMask = resize(GlassMask,width,height,8,8,30,8)
    #Glass = put(Image.new("RGBA",(800,602),(0,0,0,0)),GlassImg.resize(screenres),int((width/screenres[0])*50-50-pos[0]+pos[0]*0.12173472694),0)
    Glass = put(Image.new("RGBA",(800,602),(0,0,0,0)),GlassImg.resize(screenres),int(-pos[0]+width/16-screenres[0]/16+pos[0]/8),-pos[1])
    WithBorder = ImageChops.multiply(GlassMask,Glass)
    WithBorder = put(WithBorder, SideGlowLeft, 0, 0)
    WithBorder = put(WithBorder, SideGlowRight, width, 0, "20")
    WithBorder = put(WithBorder, SideShine.resize((w(SideShine),(height-29-8)//4)), 0, 29)
    WithBorder = put(WithBorder, SideShine.resize((w(SideShine),(height-29-8)//4)), width, 29, "20")
    print("7")
    #WithBorder.show()
    if(title != ""):
        WithBorder = put(WithBorder,resize(TextGlow,TitleDim[0]+7+14+10,h(TextGlow),23,23,1,1),-7,0)
        WithBorder = await createtext7(WithBorder,8,7,title,"7//fonts//text//",kerningadjust=-1)
    
    WithBorder = put(WithBorder,resize(Window,width,height,8,8,30,8),0,0)
    WithBorder = put(WithBorder,CONTENT,8,30)
    WithBorder = put(WithBorder,CloseButton,width-6,1,"20")
    WithBorder = put(WithBorder,CloseSymbol,width-6-18,5,"20")
    print("8")
    ShadowTop = await imageopenWEB("7//Shadow Top.png")
    ShadowRight = await imageopenWEB("7//Shadow Right.png")
    ShadowBottom = await imageopenWEB("7//Shadow Bottom.png")
    ShadowLeft = await imageopenWEB("7//Shadow Left.png")
    print("9")
    IMAGE = Image.new("RGBA",(width+19+13,height+18+12),(0,0,0,0))
    IMAGE = put(IMAGE, resize(ShadowTop,width+13+16,12,26,26,1,1),0,0)
    IMAGE = put(IMAGE, resize(ShadowLeft,13,height,1,1,20,14),0,12)
    IMAGE = put(IMAGE, resize(ShadowRight,19,height,1,1,20,14),width+13,12)
    IMAGE = put(IMAGE, resize(ShadowBottom,width+13+17,18,28,27,1,1),0,height+12)
    IMAGE = put(IMAGE,WithBorder,13,12)
    print("10")
    if(wallpaper != ""):
        WallpaperImg = await imageopenWEB(wallpaper)
        IMAGE = put(WallpaperImg, IMAGE, pos[0]-13, pos[1]-12)
    return IMAGE

async def Create7ButtonPanel(buttons,windowwidth=360,screenres=(1920,1080)):
    summedwidth = 11
    summedheight = 20
    curwidth = 0
    curlevel = 0
    cachedbuttons = []
    for button in buttons:
        button = await Create7Button(button[0],button[1])
        cachedbuttons.append(button)
        size = button.size
        if(curwidth + size[0] > screenres[0]):
            summedheight += curlevel+2
            curwidth = 0
            curlevel = 0
        curwidth += size[0]
        summedwidth= max(summedwidth,curwidth)
        curlevel = max(curlevel,size[1])
    summedheight += curlevel
    
    for button in cachedbuttons:
        size = button.size
        
async def Create7TaskDialog(icon="",textbig="",textsmall="",title="",buttons=[],closebutton=True,pos=(200,100),screenres=(1920,1080),wallpaper=""):
    width = 360
    height = 0
    iconsize = 0
    if(title != ""):
        TitleDim = await measuretext7(title,"7//fonts//text//",kerningadjust=-1)
    if(icon != ""):
        IconImg = await imageopenWEB(icon)
        iconsize = w(IconImg)+10
        height += iconsize+10
    textbigheight = 0
    if(textbig != ""):
        textbigheight = (await measuretext7(textbig,"7/fonts/bigtext/",fit=width-iconsize-10-10))[1]+10
        height = max(height,textbigheight+10+30)
    if(textsmall != ""):
        height = max(height,(await measuretext7(textsmall,"7/fonts/text/",fit=width-iconsize-10-10))[1]+15+15)
    if buttons:
        height += 41
    CONTENT = Image.new("RGBA",(width,height),(255,255,255,255))
    if(icon != ""):
        CONTENT = put(CONTENT,IconImg,10,10)
    
    if(textbig != ""):
        CONTENT = await createtext7(CONTENT,iconsize+10,10,textbig,"7/fonts/bigtext/",(0,51,153,255),kerningadjust=-1,fit=width-iconsize-10-10)
    if(textsmall != ""):
        CONTENT = await createtext7(CONTENT,iconsize+10,textbigheight+15,textsmall,"7/fonts/text/",kerningadjust=-1,fit=width-iconsize-10-10)
    if buttons:
        CONTENT = put(CONTENT, Image.new("RGBA",(width,40),(240,240,240,255)),0,height,"02")
        CONTENT = put(CONTENT, Image.new("RGBA",(width,1),(222,222,222,255)),0,height-41)
    buttonpos = 12
    for button in buttons:
        ButtonImg = await Create7TaskDialogButton(button[0],button[1])
        CONTENT = put(CONTENT, ButtonImg, width-buttonpos,height-11,"22")
        buttonpos += w(ButtonImg)+8



        
    Window = await imageopenWEB("7//Window.png")
    CloseButton = await imageopenWEB("7//Close Button Single.png")
    CloseSymbol = await imageopenWEB("7//Close Symbol.png")
    GlassImg = await imageopenWEB("7//Glass.png")
    GlassMask = await imageopenWEB("7//Glass Mask.png")
    TextGlow = await imageopenWEB("7//Text Glow.png")
    SideGlowLeft = await imageopenWEB("7//Sideglow 1 Left.png")
    SideGlowRight = await imageopenWEB("7//Sideglow 1 Right.png")
    SideShine = await imageopenWEB("7//Side Shine.png")
    width = width+8+8
    height = height+8+30
    GlassMask = resize(GlassMask,width,height,8,8,30,8)
    #Glass = put(Image.new("RGBA",(800,602),(0,0,0,0)),GlassImg.resize(screenres),int((width/screenres[0])*50-50-pos[0]+pos[0]*0.12173472694),0)
    Glass = put(Image.new("RGBA",(800,602),(0,0,0,0)),GlassImg.resize(screenres),int(-pos[0]+width/16-screenres[0]/16+pos[0]/8),-pos[1])
    WithBorder = ImageChops.multiply(GlassMask,Glass)
    WithBorder = put(WithBorder, SideGlowLeft, 0, 0)
    WithBorder = put(WithBorder, SideGlowRight, width, 0, "20")
    WithBorder = put(WithBorder, SideShine.resize((w(SideShine),(height-29-8)//4)), 0, 29)
    WithBorder = put(WithBorder, SideShine.resize((w(SideShine),(height-29-8)//4)), width, 29, "20")
    #WithBorder.show()
    if(title != ""):
        WithBorder = put(WithBorder,resize(TextGlow,TitleDim[0]+7+14+10,h(TextGlow),23,23,1,1),-7,0)
        WithBorder = await createtext7(WithBorder,8,7,title,"7//fonts//text//",kerningadjust=-1)
    
    WithBorder = put(WithBorder,resize(Window,width,height,8,8,30,8),0,0)
    WithBorder = put(WithBorder,CONTENT,8,30)
    if closebutton:
        WithBorder = put(WithBorder,CloseButton,width-6,1,"20")
        WithBorder = put(WithBorder,CloseSymbol,width-6-18,5,"20")
    ShadowTop = await imageopenWEB("7//Shadow Top.png")
    ShadowRight = await imageopenWEB("7//Shadow Right.png")
    ShadowBottom = await imageopenWEB("7//Shadow Bottom.png")
    ShadowLeft = await imageopenWEB("7//Shadow Left.png")
    IMAGE = Image.new("RGBA",(width+19+13,height+18+12),(0,0,0,0))
    IMAGE = put(IMAGE, resize(ShadowTop,width+13+16,12,26,26,1,1),0,0)
    IMAGE = put(IMAGE, resize(ShadowLeft,13,height,1,1,20,14),0,12)
    IMAGE = put(IMAGE, resize(ShadowRight,19,height,1,1,20,14),width+13,12)
    IMAGE = put(IMAGE, resize(ShadowBottom,width+13+17,18,28,27,1,1),0,height+12)
    IMAGE = put(IMAGE,WithBorder,13,12)
    if(wallpaper != ""):
        WallpaperImg = await imageopenWEB(wallpaper)
        IMAGE = put(WallpaperImg, IMAGE, pos[0]-13, pos[1]-12)
    return IMAGE

def Export7Animation(img,savepath):  #just put the generated window into img and set savepath to the folder you want it to save  "7//animoutput//" is recommended
    for i in range(16):
        ImageChops.multiply(ImageOps.deform(img, Windows7Anim(i/60)),Image.new("RGBA",(w(img),h(img)),(255,255,255,int(max(0,min(1,(i+0.1)/15))**0.5*255)))).save(savepath+str(i)+".png")
def even(a):
    c = ceil(a/2)*2
    dc = abs(c-a)
    f = floor(a/2)*2
    df = abs(f-a)
    if(df <= dc):
        return f
    else:
        return c
def buttoneven(a):
    c = ceil(a/2)*2
    dc = abs(c-a)
    f = floor(a/2)*2
    df = abs(f-a)
    if(df < dc):
        return f
    else:
        return c
def getsafe(a, i, fallback):
    try:
        return a[i]
    except IndexError:
        return fallback
async def Create3_1Window(icon="",text="",title="",buttons=[],active=True):
    contentwidth = 0
    contentheight = 0
    textpos = 18
    textposy = 16
    iconposy = 17
    if(text != ""):
        TextImg = await createtextmac(text,"3.1//fonts//text//")
        contentwidth += w(TextImg)+18+17
        contentheight += h(TextImg)+16+16
    if(icon != ""):
        IconImg = await imageopenWEB(icon)
        textpos += w(IconImg)+19
        contentwidth += w(IconImg)+18
        contentwidth = max(contentwidth,w(IconImg)+19+19)
        contentheight = max(contentheight,17+h(IconImg)+15)
        if(text != ""):
            textposy = max(16,h(IconImg)//2-h(TextImg)//2+17)
    if(title != ""):
        TitleImg = await createtextmac(text,"3.1//fonts//text//")
        contentwidth = max(contentwidth,w(TitleImg)+20+1)
    if buttons:
        contentheight += 44
    buttonswidth = 0
    for button in buttons:
        CurrentButton = await Create3_1Button(button[0],button[1],getsafe(button,2,False))
        buttonswidth += w(CurrentButton)+17
    contentwidth = max(contentwidth,buttonswidth+17)
    contentwidth = even(contentwidth)
    if active:
        Window = await imageopenWEB("3.1//Window.png")
    else:
        Window = await imageopenWEB("3.1//Window Inactive.png")
    CloseButton = await imageopenWEB("3.1//Close Button.png")
    CONTENT = Image.new("RGBA",(contentwidth,contentheight),(255,255,255,255))
    if(text != ""):
        CONTENT = put(CONTENT,TextImg,even(textpos),even(textposy))
        if(icon != ""):
            iconposy = even(textposy+h(TextImg)/2-h(IconImg)/2)
    if(icon != ""):
        CONTENT = put(CONTENT,IconImg,18,iconposy)
    buttonpos = contentwidth/2-(58*len(buttons)+17*len(buttons)-17)/2
    if active:
        for i in range(len(buttons)):
            CONTENT = put(CONTENT,await Create3_1Button(buttons[i][0],buttons[i][1],getsafe(buttons[i],2,False)),buttoneven(buttonpos),contentheight-10,"02")
            print(buttons[i][0]+":",buttonpos,"which is",buttoneven(buttonpos))
            buttonpos += 58+17
    else:
        for i in range(len(buttons)):
            CONTENT = put(CONTENT,await Create3_1Button(buttons[i][0],0,getsafe(buttons[i],2,False)),buttoneven(buttonpos),contentheight-10,"02")
            print(buttons[i][0]+":",buttonpos,"which is",buttoneven(buttonpos))
            buttonpos += 58+17
    print(contentwidth,contentheight)
    width = contentwidth+5+5
    height = contentheight+24+5
    IMAGE = resize(Window,width,height,6,6,24,5)
    IMAGE = put(IMAGE,CONTENT,5,24)
    IMAGE = put(IMAGE, CloseButton,6,5)
    if(title != ""):
        if active:
            TitleImg = await createtextmac(title,"3.1//fonts//text//",(255,255,255,255))
        else:
            TitleImg = await createtextmac(title,"3.1//fonts//text//")
        IMAGE = put(IMAGE,TitleImg,floor((contentwidth-20-1)/2-w(TitleImg)/2)+19+6,6)
    return IMAGE
    #

async def CreateUbuntuWindow(icon="",bigtext="",text="",title="",buttons=[],active=True):
    contentwidth = 12+12+12
    contentheight = 12+16+24
    textwidth = 0
    textheight = 0
    if(bigtext != ""):
        bigtextsize = await measuretext7(bigtext,"ubuntu/fonts/bigtext/")
        textwidth += bigtextsize[0]
        textheight += bigtextsize[1]+12
    if(text != ""):
        textsize = await measuretext7(text,"ubuntu/fonts/text/")
        textwidth = max(textwidth,textsize[0])
        textheight += textsize[1]
    else:
        textheight += 17
    contentwidth += textwidth
    contentheight = max(contentheight,textheight+12+24+16)
    if(icon != ""):
        IconImg = await imageopenWEB(icon)
        contentwidth += w(IconImg)
        contentheight = max(contentheight,h(IconImg)+12+24+16)
    maxbuttonwidth = 0
    maxbuttonheight = 0
    for button in buttons:
        ButtonImg = await CreateUbuntuButton(button[0],button[1])
        maxbuttonwidth = max(w(ButtonImg),maxbuttonwidth)
        maxbuttonheight = max(h(ButtonImg),maxbuttonheight)
    contentwidth = max(contentwidth, (maxbuttonwidth+4+4)*len(buttons)+8+8)
    contentheight += maxbuttonheight
    CONTENT = Image.new("RGBA",(contentwidth,contentheight),(240,235,226))
    iconsize = 0
    if(icon != ""):
        CONTENT = put(CONTENT,IconImg,12,12)
        iconsize = w(IconImg)
    if(bigtext == ""):
        if(text != ""):
            CONTENT = await createtextubuntu(CONTENT,iconsize+24,12,text,"ubuntu/fonts/text/",(60,59,55,255))
    else:
        CONTENT = await createtextubuntu(CONTENT,iconsize+24,12,bigtext,"ubuntu/fonts/bigtext/",(60,59,55,255))
        if(text != ""):
            CONTENT = await createtextubuntu(CONTENT,iconsize+24,bigtextsize[1]+12+12,text,"ubuntu/fonts/text/",(60,59,55,255))
    buttonpos = contentwidth-12
    for button in buttons:
        CONTENT = put(CONTENT, await CreateUbuntuButton(button[0],active and button[1] or 0,[maxbuttonwidth,maxbuttonheight]),buttonpos,contentheight-16,"22")
        buttonpos -= maxbuttonwidth+8
    
    Frame = await imageopenWEB(active and "ubuntu/Window.png" or (not active and "ubuntu/Window Inactive.png"))
    CloseButton = await imageopenWEB(active and "ubuntu/Close Button.png" or (not active and "ubuntu/Close Button Inactive.png"))
    Mask = await imageopenWEB("ubuntu/Mask.png")
    Highlight = await imageopenWEB("ubuntu/Highlight.png")
    Mask = resize(Mask,contentwidth,contentheight,5,5,1,4)  
    WINDOW = resize(Frame,contentwidth+1+1,contentheight+27+1,5,5,27,5)
    WINDOW = put(WINDOW, ImageChops.multiply(Mask,CONTENT), 1, 27)
    WINDOW = put(WINDOW, CloseButton, 10, 5)
    WINDOW = put(WINDOW, Highlight,0,27)
    WINDOW = put(WINDOW, Highlight,contentwidth+1,27)
    if(title != ""):
        WINDOW = await createtextubuntu(WINDOW, 42, 6, title, "ubuntu/fonts/caption/", (51,51,51,255))
        WINDOW = await createtextubuntu(WINDOW, 42, 4, title, "ubuntu/fonts/caption/", (51,51,51,255))
        WINDOW = await createtextubuntu(WINDOW, 41, 5, title, "ubuntu/fonts/caption/", (51,51,51,255))
        WINDOW = await createtextubuntu(WINDOW, 43, 5, title, "ubuntu/fonts/caption/", (51,51,51,255))
        WINDOW = await createtextubuntu(WINDOW, 42, 5, title, "ubuntu/fonts/caption/", (223,216,200,255))
    Shadow = await imageopenWEB("ubuntu/Shadow.png")
    IMAGE = resize(Shadow,contentwidth+1+1+8+10,contentheight+27+1+8+10,20,20,21,21)
    IMAGE = put(IMAGE,WINDOW,8,8)
    return IMAGE

async def Create95Window(icon="",text="",title="",buttons=[],active=True,closebutton=True):
    buttons = buttons.copy()
    width = 0
    height = 0
    textshift = 0
    iconheight = 32
    if(icon):
        IconImg = await imageopenWEB(icon)
        width += w(IconImg)+12+12
        height = max(height,h(IconImg)+12+6)
        textshift += w(IconImg)+10
        iconheight = h(IconImg)
    if(text):
        TextImg = await createtextmac(text,"95/fonts/text/")
        print(w(TextImg))
        print(w(TextImg)+textshift+18+12)
        width = max(width,w(TextImg)+textshift+18+11)
        height = max(height,h(TextImg)+12+6)
    print(buttons)
    if(buttons):
        button = buttons[0]
        ButtonsImg = Image.new("RGBA",(1,1),(0,0,0,0))
        ButtonImg = await Create95Button(button[0],getsafe(button,1,0) if active else 0,getsafe(button,2,False))
        ButtonsImg = put(Image.new("RGBA",(w(ButtonsImg)+w(ButtonImg),max(h(ButtonsImg),h(ButtonImg))),(0,0,0,0)),ButtonsImg,0,0)
        ButtonsImg = put(ButtonsImg,ButtonImg,w(ButtonsImg),0,"20")
        buttons.pop(0)
        for button in buttons:
            ButtonImg = await Create95Button(button[0],getsafe(button,1,0) if active else 0,getsafe(button,2,False))
            ButtonsImg = put(Image.new("RGBA",(w(ButtonsImg)+w(ButtonImg)+6,max(h(ButtonsImg),h(ButtonImg))),(0,0,0,0)),ButtonsImg,0,0)
            ButtonsImg = put(ButtonsImg,ButtonImg,w(ButtonsImg),0,"20")
        width = max(width,w(ButtonsImg)+12+12)
        height += h(ButtonsImg)+12+11
        buttons.append("good")
    #width = 262
    #height = 96
    IMAGE = Image.new("RGBA",(width,height),(192,192,192,255))
    if(icon):
        IMAGE = put(IMAGE,IconImg,12,12)
    if(text):

        IMAGE = put(IMAGE,TextImg,18+textshift,21 if h(TextImg) == 13 else 16 if h(TextImg) == 26 else 12 )
    if(buttons):
        print(width/2-w(ButtonsImg)/2+1)
        print(floor(width/2-w(ButtonsImg)/2)+1)
        IMAGE = put(IMAGE, ButtonsImg,floor(width/2-w(ButtonsImg)/2)+1,height-12,"02")
    if active:
        Window = await imageopenWEB("95/Window.png")
    else:
        Window = await imageopenWEB("95/Window Inactive.png")
    if closebutton:
        CloseButton = await imageopenWEB("95/Close Button.png")
    else:
        CloseButton = await imageopenWEB("95/Close Button Disabled.png")
    IMAGE = put(resize(Window,width+2+2,height+21+2,3,3,21,2),IMAGE,2,21)
    if(title):
        TitleImg = await createtextmac(title,"95/fonts/caption/",(255,255,255) if active else (192,192,192))
        IMAGE = put(IMAGE,TitleImg,5,5)
    print(IMAGE.size)
    IMAGE = put(IMAGE,CloseButton,width-1,5,"20")
    return IMAGE

async def UpdateImagexp():
    image = await CreateXPWindow(0,0,errortext=document.getElementById("text").value,
captiontext=document.getElementById("title").value,
active=document.getElementById("active").checked,
erroriconpath=document.querySelector('input[name="icon"]:checked').value,
button1=document.getElementById("button1").value,
button2=document.getElementById("button2").value,
button3=document.getElementById("button3").value,
button1style=int(document.getElementById("button1style").value),
button2style=int(document.getElementById("button2style").value),
button3style=int(document.getElementById("button3style").value))
    canvas = document.getElementById("xpoutput")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)
def createlist(b1,b2,b3,s1,s2,s3):
    buttonlist = []
    if(b1 != ""):
        buttonlist.append([b1,s1])
        if(b2 != ""):
            buttonlist.append([b2,s2])
            if(b3 != ""):
                buttonlist.append([b3,s3])
    return buttonlist
def createlist95(b1,b2,b3,s1,s2,s3,u1,u2,u3):
    buttonlist = []
    if(b1 != ""):
        buttonlist.append([b1,s1,u1])
        if(b2 != ""):
            buttonlist.append([b2,s2,u2])
            if(b3 != ""):
                buttonlist.append([b3,s3,u3])
    return buttonlist
async def UpdateImage7():
    button1=document.getElementById("button1").value
    button2=document.getElementById("button2").value
    button3=document.getElementById("button3").value
    button1style=int(document.getElementById("button1style").value)
    button2style=int(document.getElementById("button2style").value)
    button3style=int(document.getElementById("button3style").value)
    image = await Create7Window(text=document.getElementById("text").value,
title=document.getElementById("title").value,
icon=document.querySelector('input[name="icon"]:checked').value,
buttons=createlist(button1,button2,button3,button1style,button2style,button3style))
    canvas = document.getElementById("7output")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)

async def UpdateImage3_1():
    button1=document.getElementById("button1").value
    button2=document.getElementById("button2").value
    button3=document.getElementById("button3").value
    button1style=int(document.getElementById("button1style").value)
    button2style=int(document.getElementById("button2style").value)
    button3style=int(document.getElementById("button3style").value)
    button1underline=int(document.getElementById("button1default").checked)
    button2underline=int(document.getElementById("button2default").checked)
    button3underline=int(document.getElementById("button3default").checked)
    image = await Create3_1Window(text=document.getElementById("text").value,
title=document.getElementById("title").value,
icon=document.querySelector('input[name="icon"]:checked').value,
buttons=createlist95(button1,button2,button3,button1style,button2style,button3style,button1underline,button2underline,button3underline),
active=document.getElementById("active").checked)
    canvas = document.getElementById("3_1output")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)

async def UpdateImageUbuntu():
    button1=document.getElementById("button1").value
    button2=document.getElementById("button2").value
    button3=document.getElementById("button3").value
    button1style=int(document.getElementById("button1style").value)
    button2style=int(document.getElementById("button2style").value)
    button3style=int(document.getElementById("button3style").value)
    image = await CreateUbuntuWindow(bigtext=document.getElementById("text").value,
text=document.getElementById("subtext").value,
title=document.getElementById("title").value,
icon=document.querySelector('input[name="icon"]:checked').value,
buttons=createlist(button1,button2,button3,button1style,button2style,button3style),
active=document.getElementById("active").checked)
    canvas = document.getElementById("ubuntuoutput")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)

async def UpdateImageMac():
    image = await CreateMacWindow(0,0,errortext=document.getElementById("text").value,
title=document.getElementById("title").value,
icon=document.querySelector('input[name="icon"]:checked').value,
button1=document.getElementById("button1").value,
button2=document.getElementById("button2").value,
button3=document.getElementById("button3").value,
button1style=int(document.getElementById("button1style").value),
button2style=int(document.getElementById("button2style").value),
button3style=int(document.getElementById("button3style").value),
button1default=int(document.getElementById("button1default").checked),
button2default=int(document.getElementById("button2default").checked),
button3default=int(document.getElementById("button3default").checked))
    canvas = document.getElementById("macoutput")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)

async def UpdateImageMacAlert():
    image = await CreateMacAlertDialog(0,0,errortext=document.getElementById("text").value,
title=document.getElementById("title").value,
icon=document.querySelector('input[name="icon"]:checked').value,
bar=document.getElementById("secondary").checked,
button1=document.getElementById("button1").value,
button2=document.getElementById("button2").value,
button3=document.getElementById("button3").value,
button1style=int(document.getElementById("button1style").value),
button2style=int(document.getElementById("button2style").value),
button3style=int(document.getElementById("button3style").value),
button1default=int(document.getElementById("button1default").checked),
button2default=int(document.getElementById("button2default").checked),
button3default=int(document.getElementById("button3default").checked))
    canvas = document.getElementById("macalertoutput")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)

async def UpdateImageMacWindoid():
    image = await CreateMacWindoid(text=document.getElementById("text").value,
icon=document.querySelector('input[name="icon"]:checked').value,
collapsed=not document.getElementById("secondary").checked)
    canvas = document.getElementById("macwindoidoutput")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)

async def UpdateImage7TaskDialog():
    button1=document.getElementById("button1").value
    button2=document.getElementById("button2").value
    button3=document.getElementById("button3").value
    button1style=int(document.getElementById("button1style").value)
    button2style=int(document.getElementById("button2style").value)
    button3style=int(document.getElementById("button3style").value)
    image = await Create7TaskDialog(textbig=document.getElementById("text").value,
textsmall=document.getElementById("subtext").value,
closebutton=document.getElementById("secondary").checked,
title=document.getElementById("title").value,
icon=document.querySelector('input[name="icon"]:checked').value,
buttons=createlist(button1,button2,button3,button1style,button2style,button3style))
    canvas = document.getElementById("taskdialogoutput")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)

async def UpdateImage95():
    button1=document.getElementById("button1").value
    button2=document.getElementById("button2").value
    button3=document.getElementById("button3").value
    button1style=int(document.getElementById("button1style").value)
    button2style=int(document.getElementById("button2style").value)
    button3style=int(document.getElementById("button3style").value)
    button1underline=int(document.getElementById("button1default").checked)
    button2underline=int(document.getElementById("button2default").checked)
    button3underline=int(document.getElementById("button3default").checked)
    image = await Create95Window(text=document.getElementById("text").value,
title=document.getElementById("title").value,
icon=document.querySelector('input[name="icon"]:checked').value,
buttons=createlist95(button1,button2,button3,button1style,button2style,button3style,button1underline,button2underline,button3underline),
active=document.getElementById("active").checked,
closebutton=document.getElementById("secondary").checked)
    canvas = document.getElementById("95output")
    ctx = canvas.getContext("2d")
    width,height = image.size
    
    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"
    
    canvas.width = width
    canvas.height = height
    
    ctx.clearRect(0, 0, width, height)
    data = Uint8ClampedArray.new(to_js(image.tobytes()))
    image_data = ImageData.new(data, width, height)
    ctx.putImageData(image_data, 0, 0)

async def UpdateImage(e):
    await asyncio.gather(
        UpdateImagexp(),
        UpdateImage7(),
        UpdateImage3_1(),
        UpdateImageUbuntu(),
        UpdateImageMac(),
        UpdateImageMacAlert(),
        UpdateImageMacWindoid(),
        UpdateImage7TaskDialog(),
        UpdateImage95()
    )

def UpdateCustomIcon(e=None):
    url = document.getElementById("customicon").value
    document.getElementById("customiconimg").src = url
    document.getElementById("customiconradio").value = url
    
Update = create_proxy(UpdateImage)
document.getElementById("generate").addEventListener("click",Update)

UpdateIcon = create_proxy(UpdateCustomIcon)
document.getElementById("customicon").addEventListener("change",UpdateIcon)
UpdateCustomIcon()
</py-script>
	
	</body>
</html>
