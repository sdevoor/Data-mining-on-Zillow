#import library
import urllib2
import requests
import xml.etree.ElementTree as ET
import csv

#set file name
download_dir = "HousingData.csv"
#open file
csv = open(download_dir, "w")
#set coloumn name
columnTitleRow = "zpid, street, zipcode, city, state, taxAssessment, yearBuilt, lotSizeSqFt, finishedSqFt, lastSoldDate, lastSoldPrice, valuationRangelow, valuationRangehigh, bedrooms \n"
#write the column name
csv.write(columnTitleRow)


#set range for no. of pages to be scraped 
for i in range(40000000,40005000):
    #print 'sfa'
    a = str(i)
    #set url
    url = 'http://www.zillow.com/webservice/GetDeepComps.htm?zws-id=X1-ZWz18var16lnnv_14qhc&zpid=' + a + '&count=1'
    #open the xml file from the url
    tree = ET.parse(urllib2.urlopen(url))
    #set root
    root = tree.getroot()
    #if message is successfully processed
    if root[1][1].text == '0':
        #set row to empty string
        row = ""
        #get properties from response
        for properties in root[2]:
            #get sub tag, if it is not None, extract else set to NA and concatenate to row
            zpid = properties.find('principal').find('zpid')
            if zpid != None:
                row = row + zpid.text + ','
            street = properties.find('principal').find('address').find('street')
            if street != None:
                row = row + street.text + ','
            else:
                row = row + 'NA' + ','
            zipcode = properties.find('principal').find('address').find('zipcode')
            if zipcode != None:
                row = row + zipcode.text + ','
            else:
                row = row + 'NA' + ','
            city = properties.find('principal').find('address').find('city')
            if city != None:
                row = row + city.text + ','
            else:
                row = row + 'NA' + ','
            state = properties.find('principal').find('address').find('state')
            if state != None:
                row = row + state.text + ','
            else:
                row = row + 'NA' + ','
            taxAssessment = properties.find('principal').find('taxAssessment')
            if taxAssessment != None:
                row = row + taxAssessment.text + ','
            else:
                row = row + 'NA' + ','
            yearBuilt =properties.find('principal').find('yearBuilt')
            if yearBuilt != None:
                row = row + yearBuilt.text + ','
            else:
                row = row + 'NA' + ','
            lotSizeSqFt =properties.find('principal').find('lotSizeSqFt')
            if lotSizeSqFt != None:
                row = row + lotSizeSqFt.text + ','
            else:
                row = row + 'NA' + ','
            finishedSqFt =properties.find('principal').find('finishedSqFt')
            if finishedSqFt != None:
                row = row + finishedSqFt.text + ','
            else:
                row = row + 'NA' + ','
            lastSoldDate = properties.find('principal').find('lastSoldDate')
            if lastSoldDate != None:
                row = row + lastSoldDate.text + ','
            else:
                row = row + 'NA' + ','
            lastSoldPrice= properties.find('principal').find('lastSoldPrice')
            if lastSoldPrice != None:
                row = row + lastSoldPrice.text + ','
            else:
                row = row + 'NA' + ','
            valuationRangelow = properties.find('principal').find('zestimate').find('valuationRange').find('low')
            if valuationRangelow != None:
                row = row + valuationRangelow.text + ','
            else:
                row = row + 'NA' + ','
            valuationRangehigh = properties.find('principal').find('zestimate').find('valuationRange').find('high')
            if valuationRangehigh != None:
                row = row + valuationRangehigh.text + ','
            else:
                row = row + 'NA' + ','
            bedrooms = properties.find('principal').find('bedrooms')
            if bedrooms != None:
                row = row + bedrooms.text + '\n'
            else:
                row = row + 'NA' + '\n'
               
               
            print(zpid.text)
            #write each row to csv file
            csv.write(row)

#close csv
csv.close()


            
        
            


