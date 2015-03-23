from BeautifulSoup import BeautifulSoup
import urllib
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('a test sheet')
f = urllib.urlopen("http://www.cgd.ucar.edu/cas/catalog/surface/dai-runoff/coastal-stns-byVol-updated-oct2007.txt")
html = f.read()
soup = BeautifulSoup(html)
#print soup.prettify()
#print soup
 
#codigo a buscar en la _URL_
table = soup.find("table",id="alignmentTable")
 
rows = table.findAll("tr")
x = 0
for tr in rows:
    cols = tr.findAll("td")
    if not cols:
        # when we hit an empty row
        # we should not print anything to the workbook
        continue
    y = 0
    for td in cols:
        texte_bu = td.text
        texte_bu = texte_bu.encode('utf-8')
        texte_bu = texte_bu.strip()
        ws.write(x, y, td.text)
        print(x, y, td.text)
        y = y + 1
    # update the row pointer AFTER a row has been printed
    # this avoids the blank row at the top of your table
    x = x + 1
 
wb.save('BlastResults.xls')
