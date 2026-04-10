from selenium.webdriver.common.by import By


search_loc = (
    By.XPATH,
    '//input[contains(@class, "text-bg-light") and not(contains(@class, "ps-3")) and @type="search" and @name="search"]')
visible_products_loc = (By.XPATH, '//td[@class="oe_product"]')
no_result = (By.TAG_NAME, 'h3')
no_result_with_product = (By.XPATH, '//*[contains(text(), "No results for")]')
checkbox_aluminium = (By.XPATH, '//input[@type="checkbox" and @id="1-2"]')
sss = (By.XPATH, '//*[text()="$ 85.00"]')
product_table = (By.XPATH, '//img[@alt="Customizable Desk"]')
cart_btn = (By.CSS_SELECTOR, '[title="Shopping cart"]')
