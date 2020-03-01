from selenium import webdriver
import secrets
from datetime import date


# Setup Browser
login_page = 'https://primofs01.sibi.usp.br/pds?func=load-login&calling_system=primo&institute=USP&lang=por&isMobile=false&url=http://www.buscaintegrada.usp.br:80/primo_library/libweb/action/login.do?targetURL=http%3a%2f%2fwww.buscaintegrada.usp.br%2fprimo_library%2flibweb%2faction%2fsearch.do%3fvid%3dUSP%26amp%3bdscnt%3d0%26amp%3bdstmp%3d1583081070253%26amp%3binitializeIndex%3dtrue'

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get(login_page)
browser.find_element_by_link_text('Senha da biblioteca').click()


# Login
login_user = browser.find_element_by_id('bor_id')
login_pass = browser.find_element_by_id('bor_verification')

login_user.send_keys(secrets.NUSP)
login_pass.send_keys(secrets.PASS)

browser.find_element_by_xpath('//*[@value = "OK"]').click()
browser.find_element_by_id('exlidMyAccount').click()


# Book Info
checkboxes = browser.find_elements_by_xpath('//*[@type = "checkbox"]')
titles = browser.find_elements_by_xpath('//*[@class = "MyAccount_Loans_2 MyAccount_Loans_title"]')
dates = browser.find_elements_by_xpath('//*[@class = "MyAccount_Loans_4 MyAccount_Loans_dueDate"]')
locals = browser.find_elements_by_xpath('//*[@class = "MyAccount_Loans_7 MyAccount_Loans_location"]')

checkboxes.pop() # Last element is not associated with a book
td = date.today().strftime("%d/%m/%y")
selected = [] # Books that must be renewed
returned = [] # Books that must be returned

for i in range(len(dates)):
    print('\nBook {0}: {1}'.format(str(i), titles[i].text))

    if dates[i].text == td:
        checkboxes[i].click()
        selected.append(i)
        print('\t... Selected.')
    else:
        print('\t... OK')

browser.find_element_by_link_text('Renovar selecionados').click()
new_dates = browser.find_elements_by_xpath('//*[@class = "MyAccount_Loans_4 MyAccount_Loans_dueDate"]')

for i in selected:
    # Return date didn't change after selection => the book must be returned
    if dates[i].text == new_dates[i].text:
        returned.append(i)


# Logout
browser.find_element_by_id('exlidSignOut').click()
browser.quit()
