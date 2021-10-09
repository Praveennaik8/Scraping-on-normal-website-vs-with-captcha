from selenium import webdriver
import time

SITE = "https://praveennaik8.github.io/Movie-Finder-captcha/"
# SITE = "https://praveennaik8.github.io/Movie-Finder/"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('C:/Users/manin/Desktop/chromedriver.exe',options=options)
page = driver.get(SITE)

def writeToFile(MovieList,file):
    # print(MovieList)
    if not MovieList:
        raise Exception("Error")
    for movie in MovieList:
        
        file.write("Name : "+movie['name']+'\n')
        file.write("Image URL : "+movie['image']+'\n')
        file.write("Plot : "+movie['plot']+'\n')
        file.write("\n------------------------------\n\n")
    

def getMovieDetails(activity,file):

    

    search_activity = driver.find_element_by_xpath('//*[@id="search"]')
    search_activity.clear()
    search_activity.send_keys(activity)

    search = driver.find_element_by_xpath('//*[@id="search"]')
    search.submit()
    MovieList = []
    MovieDetails = {}
    time.sleep(3)

    for i in range(5):
        try:
            MovieDetails = {}
            MovieDetails['name'] = driver.find_element_by_xpath('//*[@id="main"]/div['+str(i)+']/div[1]/h3').text
            # print(MovieDetails['name'])
            img = driver.find_element_by_xpath('//*[@id="main"]/div['+str(i)+']/img')
            src = img.get_attribute('src')
            MovieDetails['image'] = src
            # print(MovieDetails['image'])
            MovieDetails['plot'] = driver.find_element_by_xpath('//*[@id="main"]/div['+str(i)+']/div[2]/p').get_attribute('textContent').lstrip()
            
            # print(MovieDetails['plot'])
            MovieList.append(MovieDetails)
        except:
            pass

    # print(MovieList)
    writeToFile(MovieList,file)

#-----------------------------------------------------------------------

file = open("MovieDetails.txt", "w")
MovieTitles = ['star wars','Avengers','batman']
for movie in MovieTitles:
    try:
        getMovieDetails(movie,file)
        print("Scraping was successful!!")
    except:
        print("Scraping was unsuccessful!!")
file.close()

#-----------------------------------------------------------------------