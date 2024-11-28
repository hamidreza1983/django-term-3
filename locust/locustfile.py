from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(1, 5)

    # @task
    # def get_home(self):
    #     self.client.get("/")
    #     #self.client.get("/services")
    
    # @task
    # def get_service(self):
    #     self.client.get("/services")

    @task
    def post_login(self):
        self.client.post("/accounts/api/v5/api/token/", data={'email': "admin@admin.com", "password":"1234"})
        
        