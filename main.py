from selenium import webdriver
import secrets


login_page = 'https://primofs01.sibi.usp.br/pds?func=load-login&calling_system=primo&institute=USP&lang=por&isMobile=false&url=http://www.buscaintegrada.usp.br:80/primo_library/libweb/action/login.do?targetURL=http%3a%2f%2fwww.buscaintegrada.usp.br%2fprimo_library%2flibweb%2faction%2fsearch.do%3fvid%3dUSP%26amp%3bdscnt%3d0%26amp%3bdstmp%3d1583081070253%26amp%3binitializeIndex%3dtrue'


# Setup Browser
browser = webdriver.Firefox()
browser.get(login_page)

browser.find_element_by_link_text('Senha da biblioteca').click()


# Login
login_user = browser.find_element_by_id('bor_id')
login_pass = browser.find_element_by_id('bor_verification')

login_user.send_keys(secrets.NUSP)
login_pass.send_keys(secrets.PASS)
