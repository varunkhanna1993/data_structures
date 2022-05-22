class Cookie:
    def __init__(self, color):
        self.color = color 

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        

cookie_one = Cookie('green') # this creates a green cookie but it creates its own data class. 
cookie_two = Cookie('blue')

if __name__ == '__main__':
    print('Cookie one is:' , cookie_one.get_color())
    print('Cookie two is:' , cookie_two.get_color())

    #
    cookie_one.set_color('black')
    print('cookie one has now changed color', cookie_one.get_color())