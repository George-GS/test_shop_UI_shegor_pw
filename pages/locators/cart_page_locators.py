from selenium.webdriver.common.by import By


product_in_cart = (By.CLASS_NAME, 'align-top')
cart_header = (By.TAG_NAME, 'h3')
empty_cart_info = (By.XPATH, '//*[contains(@class, "alert-info")]')
remove_btn = (By.CSS_SELECTOR, '[title="Remove from cart"]')
