def go_to_login_page(browser):
    """Opens the login page

    :param: browser: selenium browser object
    
    :return: None
    """
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser): 
   browser.get(link) 
   go_to_login_page(browser)     

