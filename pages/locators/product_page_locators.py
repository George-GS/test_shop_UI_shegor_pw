from selenium.webdriver.common.by import By


name_product_loc = (By.TAG_NAME, 'h1')
price_product_loc = (By.CSS_SELECTOR, '[class="oe_price"]')
image_product_loc = (By.XPATH, '//img[@alt="Office Design Software"]')
add_one = (By.CSS_SELECTOR, '[title="Add one"]')
add_to_cart = (By.ID, 'add_to_cart')
product_name_in_cart_loc = (By.XPATH, '//div[@class="toast-body"]//span')
currency_loc = (By.XPATH, '//section//*[@data-bs-toggle="dropdown"]')
eur_loc = (By.CSS_SELECTOR, '[data-pl_id="3"]')
