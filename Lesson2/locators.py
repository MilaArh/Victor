from selenium.webdriver.common.by import By

USER_NAME = (By.CSS_SELECTOR, '#user-name')
PASSWORD = (By.CSS_SELECTOR, '#password')
SUBMIT = (By.CSS_SELECTOR, '[type="submit"]')
ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
ADD_TO_CART_ITEM = (By.ID, 'add-to-cart')
REMOVE_ITEM = (By.ID, 'remove')
IMG_CART = (By.XPATH, '//img[@alt="Sauce Labs Backpack"]')
NAME_CART = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
BASKET = (By.CLASS_NAME, "shopping_cart_link")
CHECKOUT = (By.ID, "checkout")
CONTINUE = (By.ID, "continue")
FINISH = (By.ID, "finish")
SELECT = (By.CLASS_NAME, 'product_sort_container')
BURGER_MENU = (By.ID, "react-burger-menu-btn")
LOGOUT = (By.ID, "logout_sidebar_link")
ABOUT = (By.ID, "about_sidebar_link")
RESET_APP_STATE = (By.ID, "reset_sidebar_link")
# ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-bike-light')