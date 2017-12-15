 Data-mining-on-Zillow


Scrapping the data from zillow.com

In this project,the data has been scrapped from zillow.com using the zillow API. The API key allows to access a XML file using which we can scrape the data with the help of root. The libraries used for scarpping the data were Requests, urllib2 and ElemetTree. The extrated data is transferred to a csv file using the library pandas. The various attributes extracted from the XML file using the method GetDeepComps are zillow Property id, street, zipcode,city,state, Tax assessement, year built, lot size, finished square feet, last sold date, last sold prize. Around 4000 data were collected which reduced to 2119 after cleaning. 


Implemetation of Machine learning algorithms on the data set

Have implemented Linear regression, Decision tree and KNN on the attributes lot size over last sold price. Decision tree has an accuracy of 80%, KNN has an accuracy of 80% with N = 1 78% with N = 2 and linear regression has an accuracy of 73%.  
