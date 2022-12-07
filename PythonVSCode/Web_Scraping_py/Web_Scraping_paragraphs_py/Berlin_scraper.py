from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

Berlin_url = 'https://www.berlin.de/corona/massnahmen/verordnung/'

# opening up connection, grab the page
reqPage = req(Berlin_url)
page_html = reqPage.read()
reqPage.close()

# html parsing (We can now in the page)
html_soup = soup(page_html, "html.parser")

paragraphs_item = html_soup.findAll('div', class_="container")

# file csv creation
filename = 'berlin_paragraphs.csv'
# file 'w' writing allow
f = open(filename, 'w')

#Header= Headline for Part
#headers = ''
#headers = 'Inhaltsverzeichnis, teil \n'
#f.write(headers)


for index in paragraphs_item:
    inhaltsVerzeichnis = index.find('h2', id='document_toc', class_='title tocnocount').text
    listVerzeichnis0 = index.find('li', class_='odd position0').text
    listVerzeichnis1 = index.find('li', class_='even position1').text
    listVerzeichnis2 = index.find('li', class_='odd position2').text
    listVerzeichnis3 = index.find('li', class_='even position3').text
    listVerzeichnis4 = index.find('li', class_='odd position4').text
    listVerzeichnis5 = index.find('li', class_='even position5').text
    listVerzeichnis6 = index.find('li', class_='odd position6').text
    listVerzeichnis7 = index.find('li', class_='even position7').text
    listVerzeichnis8 = index.find('li', class_='odd position8').text
    listVerzeichnis9 = index.find('li', class_='even position9').text
    listVerzeichnis10 = index.find('li', class_='odd position10').text
    listVerzeichnis11 = index.find('li', class_='even position11').text
    listVerzeichnis12 = index.find('li', class_='odd position12').text
    listVerzeichnis13 = index.find('li', class_='even position13').text
    listVerzeichnis14 = index.find('li', class_='odd position14').text
    listVerzeichnis15 = index.find('li', class_='even position15').text
    listVerzeichnis16 = index.find('li', class_='odd position16').text
    listVerzeichnis17 = index.find('li', class_='even position17').text
    listVerzeichnis18 = index.find('li', class_='odd position18').text
    listVerzeichnis19 = index.find('li', class_='even position19').text
    #listVerzeichnis20 = index.find('li', class_='odd position20').text
    
#for actualInfo in paragraphs_item:
    #headerInfo = actualInfo.find('h2', class_='title', id='headline_1_0').text
    
#for actualInfo2 in paragraphs_item:
    #textInfo = actualInfo2.find('div', class_='textile').text    

for paragraph0 in paragraphs_item:
    firstPart = paragraph0.find('h2', class_="title", id="part1").text

#for paragraph1 in paragraphs_item:
    #firstPartParagraph1 = paragraph1.find('#text', first=True).text
    #firstPartParagraphsearch2 = firstPartParagraphsearch1.find('div', class_='text')
    #firstPartParagraphsearch3 = firstPartParagraphsearch2.find('div', class_="textile")
    #firstPartParagraph1 = firstPartParagraphsearch3.find('h3').text

for paragraph2 in paragraphs_item:
    firstPartParagraph2 = paragraph2.find('h3', class_="title", id="paragraph2").text   

for paragraph3 in paragraphs_item:
    firstPartParagraph3 = paragraph3.find('h3', class_="title", id="paragraph3").text
    
for paragraph4 in paragraphs_item:
    firstPartParagraph4 = paragraph4.find('h3', class_="title", id="paragraph4").text

for paragraph5 in paragraphs_item:
    firstPartParagraph5 = paragraph5.find('h3', class_="title", id="paragraph5").text

for paragraph6 in paragraphs_item:
    firstPartParagraph6 = paragraph6.find('h3', class_="title", id="paragraph6").text

for paragraph7 in paragraphs_item:
    firstPartParagraph7 = paragraph7.find('h3', class_="title", id="paragraph7").text    

for paragraph8 in paragraphs_item:
    firstPartParagraph8 = paragraph7.find('h3', class_="title", id="paragraph8").text    

for Part2paragraph in paragraphs_item:
    secondPartParagraph = Part2paragraph.find('h2', id="part2", class_='title').text

for Part2paragraphAbschnitt in paragraphs_item:
    paragraphAbschnitt1 = Part2paragraphAbschnitt.find('h2', class_='title', id='paragraph9').text

#for Part2paragraph9 in paragraphs_item:
    #secondPartParagraph9 = Part2paragraph9.find('h2', class_='title', id='paragraph9').text

for Part2paragraph10 in paragraphs_item:
    secondPartParagraph10 = Part2paragraph10.find('h3', class_='title', id='paragraph10').text

for Part2paragraph11 in paragraphs_item:
    secondPartParagraph11 = Part2paragraph11.find('h3', class_='title', id='paragraph11').text

for Part2paragraph12 in paragraphs_item:
    secondPartParagraph12 = Part2paragraph12.find('h3', class_='title', id='paragraph12').text

for Part2paragraph13 in paragraphs_item:
    secondPartParagraph13 = Part2paragraph13.find('h3', class_='title', id='paragraph13').text

for Part2paragraph14 in paragraphs_item:
    secondPartParagraph14 = Part2paragraph14.find('h3', class_='title', id='paragraph14').text

for Part2paragraphAbschnitt2 in paragraphs_item:
    paragraphAbschnitt2 = Part2paragraphAbschnitt2.find('h2', class_='title', id='paragraph15').text
    
#for Part2paragraph15 in paragraphs_item:
    #secondPartParagraph15 = Part2paragraph15.find('h3', class_='title', id='paragraph15').text

for Part2paragraph16 in paragraphs_item:
    secondPartParagraph16 = Part2paragraph16.find('h3', class_='title', id='paragraph16').text

for Part2paragraph17 in paragraphs_item:
    secondPartParagraph17 = Part2paragraph17.find('h3', class_='title', id='paragraph17').text

for Part2paragraph18 in paragraphs_item:
    secondPartParagraph18 = Part2paragraph18.find('h3', class_='title', id='paragraph18').text

for Part2paragraph19 in paragraphs_item:
    secondPartParagraph19 = Part2paragraph19.find('h3', class_='title', id='paragraph19').text

for paragraphAbschnitt3 in paragraphs_item:
    secondPartParagraphAbschnitt3 = paragraphAbschnitt3.find('h2', class_='title', id='paragraph20').text

#for part3Paragraph20 in paragraphs_item:
    #Paragraph20 = part3Paragraph20.find('h2', class_='title', id='paragraph20').text

for part3Paragraph21 in paragraphs_item:
    secondPartParagraph21 = part3Paragraph21.find('h3', class_='title', id='paragraph21').text

for part3Paragraph22 in paragraphs_item:
    secondPartParagraph22 = part3Paragraph22.find('h3', class_='title', id='paragraph22').text
    
for part3Paragraph23 in paragraphs_item:
    secondPartParagraph23 = part3Paragraph23.find('h3', class_='title', id='paragraph23').text

for Part4paragraphAbschnitt4 in paragraphs_item:
    secondPartParagraphAbschnitt4 = Part4paragraphAbschnitt4.find('h2', class_='title', id='paragraph24').text

#for Part4paragraph24 in paragraphs_item:
    #fourthPartParagraph24 = Part4paragraph24.find('h2', class_='title', id='paragraph24').text

for part4Paragraph25 in paragraphs_item:
    secondPartParagraph25 = part4Paragraph25.find('h3', class_='title', id='paragraph25').text

for part4Paragraph26 in paragraphs_item:
    secondPartParagraph26 = part4Paragraph26.find('h3', class_='title', id='paragraph26').text

for part4Paragraph27 in paragraphs_item:
    secondPartParagraph27 = part4Paragraph27.find('h3', class_='title', id='paragraph27').text
    
for part4Paragraph28 in paragraphs_item:
    secondPartParagraph28 = part4Paragraph28.find('h3', class_='title', id='paragraph28').text

for Part4paragraphAbschnitt5 in paragraphs_item:
    secondPartParagraphAbschnitt5 = Part4paragraphAbschnitt5.find('h2', class_='title', id='paragraph29').text
    
#for Part4paragraph29 in paragraphs_item:
    #fourthPartParagraph29 = Part4paragraph29.find('h2', class_='title', id='paragraph29').text

for Part4paragraphAbschnitt6 in paragraphs_item:
    secondPartParagraphAbschnitt6 = Part4paragraphAbschnitt6.find('h2', class_='title', id='paragraph30').text
    
#for Part4paragraph30 in paragraphs_item:
    #fourthPartParagraph30 = Part4paragraph30.find('h2', class_='title', id='paragraph29').text

for part4Paragraph31 in paragraphs_item:
    secondPartParagraph31 = part4Paragraph31.find('h3', class_='title', id='paragraph31').text

for part4Paragraph32 in paragraphs_item:
    secondPartParagraph32 = part4Paragraph32.find('h3', class_='title', id='paragraph32').text

for part4Paragraph33 in paragraphs_item:
    secondPartParagraph33 = part4Paragraph33.find('h3', class_='title', id='paragraph33').text

for part4Paragraph34 in paragraphs_item:
    secondPartParagraph34 = part4Paragraph34.find('h3', class_='title', id='paragraph34').text

for Part4paragraphAbschnitt7 in paragraphs_item:
    secondPartParagraphAbschnitt7 = Part4paragraphAbschnitt7.find('h2', class_='title', id='paragraph35').text

#for Part4paragraph35 in paragraphs_item:
    #fourthPartParagraph35 = Part4paragraph35.find('h2', class_='title', id='paragraph25').text

for part4Paragraph36 in paragraphs_item:
    secondPartParagraph36 = part4Paragraph36.find('h3', class_='title', id='paragraph36').text

for part4Paragraph37 in paragraphs_item:
    secondPartParagraph37 = part4Paragraph37.find('h3', class_='title', id='paragraph37').text

for part5Paragraph38 in paragraphs_item:
    thirdPartParagraph38 = part5Paragraph38.find('h2', class_='title', id='paragraph38').text

#for part5Paragraph38 in paragraphs_item:
    #thirdPartParagraph38 = part5Paragraph38.find('h3', class_='title', id='paragraph38').text

for part5Paragraph39 in paragraphs_item:
    thirdPartParagraph39 = part5Paragraph39.find('h3', class_='title', id='paragraph39').text
    
for part5Paragraph40 in paragraphs_item:
    thirdPartParagraph40 = part5Paragraph40.find('h3', class_='title', id='paragraph40').text

for part5Paragraph41 in paragraphs_item:
    thirdPartParagraph41 = part5Paragraph41.find('h3', class_='title', id='paragraph41').text

for part5Paragraph42 in paragraphs_item:
    thirdPartParagraph42 = part5Paragraph42.find('h3', class_='title', id='paragraph42').text
             
f.write('Das ' + inhaltsVerzeichnis + ' der Corona Regelungen des Bundeslandes Berlin' '\n' +
            '- ' + listVerzeichnis0 + '\n' +
            '- ' + listVerzeichnis1 + '\n' +
            '- ' + listVerzeichnis2 + '\n' +
            '- ' + listVerzeichnis3 + '\n' +
            '- ' + listVerzeichnis4 + '\n' +
            '- ' + listVerzeichnis5 + '\n' +
            '- ' + listVerzeichnis6 + '\n' +
            '- ' + listVerzeichnis7 + '\n' +
            '- ' + listVerzeichnis8 + '\n' +
            '- ' + listVerzeichnis9 + '\n' +
            '- ' + listVerzeichnis10 + '\n' +
            '- ' + listVerzeichnis11 + '\n' +
            '- ' + listVerzeichnis12 + '\n' +
            '- ' + listVerzeichnis13 + '\n' +
            '- ' + listVerzeichnis14 + '\n' +
            '- ' + listVerzeichnis15 + '\n' +
            '- ' + listVerzeichnis16 + '\n' +
            '- ' + listVerzeichnis17 + '\n' +
            '- ' + listVerzeichnis18 + '\n' +
            '- ' + listVerzeichnis19 + '\n' +
            #'- ' + listVerzeichnis20 + '\n' +
            '\n' +
            #headerInfo + '\n' +
            #textInfo + '\n' +
            '\n' +
            firstPart + '\n' +
            #firstPartParagraph1 + '\n' +
            firstPartParagraph2 + '\n' +
            firstPartParagraph3 + '\n' +
            firstPartParagraph4 + '\n' +
            firstPartParagraph5 + '\n' +
            firstPartParagraph6 + '\n' +
            firstPartParagraph7 + '\n' +
            firstPartParagraph8 + '\n' +            
            '\n' +
            '\n' +
            secondPartParagraph + '\n' +
            paragraphAbschnitt1 +
            #secondPartParagraph9 + '\n' +
            secondPartParagraph10 + '\n' +
            secondPartParagraph11 + '\n' +
            secondPartParagraph12 + '\n' +
            secondPartParagraph13 + '\n' +
            secondPartParagraph14 + '\n' +
            '\n' +
            paragraphAbschnitt2 + '\n' +
            #secondPartParagraph15 + '\n' +
            secondPartParagraph16 + '\n' +
            secondPartParagraph17 + '\n' +
            secondPartParagraph18 + '\n' +
            secondPartParagraph19 + '\n' +
            '\n' +
            secondPartParagraphAbschnitt3 + '\n' +
            #thirdPartParagraph20 + \n +
            secondPartParagraph21 + '\n' +
            secondPartParagraph22 + '\n' +
            secondPartParagraph23 + '\n' +
            '\n' +
            secondPartParagraphAbschnitt4 + '\n' +
            #paragraph24 + '\n' +
            secondPartParagraph25 + '\n' +
            secondPartParagraph26 + '\n' +
            secondPartParagraph27 + '\n' +
            secondPartParagraph28 + '\n' + 
            '\n' +
            secondPartParagraphAbschnitt5 + '\n' +
            #fourthPartParagraph29 + '\n' +
            '\n' +
            secondPartParagraphAbschnitt6 + '\n' +
            # fourthPartParagraph30
            secondPartParagraph31 + '\n' +
            secondPartParagraph32 + '\n' +
            secondPartParagraph33 + '\n' +
            secondPartParagraph34 + '\n' +
            '\n' +
            secondPartParagraphAbschnitt7 + '\n' +
            #fourthPartParagraph35 + '\n' +
            secondPartParagraph36 + '\n' +
            secondPartParagraph37 + '\n' +
            '\n' +
            '\n' +
            thirdPartParagraph38 + '\n' +
            thirdPartParagraph39 + '\n' +
            thirdPartParagraph40 + '\n' +
            thirdPartParagraph41 + '\n' +
            thirdPartParagraph42 + '\n'
            )
    
f.close()