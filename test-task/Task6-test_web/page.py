class Order:

    def __init__(self, driver):
        self.driver = driver

    def CustomerName(self, customer_name):
        self.driver.find_element_by_name("custname").send_keys(customer_name)

    def Telephone(self, telephone):
        self.driver.find_element_by_name("custtel").send_keys(telephone)

    def EmailAddress(self, customer_email):
        self.driver.find_element_by_name("custemail").send_keys(customer_email)

    def PizzaSize(self, pizza_size):
        self.driver.find_element_by_css_selector(f"input[type='radio'][value='{pizza_size}']").click()

    def PizzaToppings(self, toppings_list):
        for i in toppings_list:
            self.driver.find_element_by_css_selector(
                f"input[type='checkbox'][value='{i}']"
                ).click()

    def DeliveryTime(self, delivery_time):
        self.driver.find_element_by_name("delivery").send_keys(delivery_time)

    def Comments(self, comments):
        self.driver.find_element_by_name("comments").send_keys(comments)

    def SubmitOrder(self):
        self. driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Delivery instructions:'])[1]/following::button[1]"
            ).click()
