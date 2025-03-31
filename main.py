import customtkinter as ctk
from Src.Views.loginPage import LoginPage
from Src.Views.createAccountPage import CreateAccountPage
from Src.Util import imageLoader
from CTkToolTip import *

class HomePage(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.background = None
        self.wm_overrideredirect(True)

        self.openWindowCentreOfScreen(1200, 750)
        self.xOffSet = None
        self.yOffSet = None

        self.advertisement = "All"
        self.account = None
        self.loggedIn = False
        self.setupGui()

    def setupGui(self):
        self.background = ctk.CTkLabel(master = self, image = imageLoader.Images().homePage, width = 1200, height = 750, text = "")
        self.background.pack(fill = "both", expand = True)
        self.background.bind("<Button-1>", self.startMovingWindow)
        self.background.bind("<B1-Motion>", self.dragWindow)

        #Navigation Bar
        homePageLogo = ctk.CTkLabel(master = self.background, width = 151, height = 35, text = "", image = imageLoader.Images().homePageLogo, bg_color ="#FFFFFF")
        homePageLogo.place(x = 23, y = 36)
        self.navBarBookFlightButton = ctk.CTkLabel(master = self.background, width = 149, height = 34, text = "Book Flight", font = ("Plus Jakarta Sans", 24), bg_color = "#FFFFFF", anchor = "w")
        self.navBarBookFlightButton.place(x = 650, y = 36)
        bookFlightToolTip = CTkToolTip(self.navBarBookFlightButton, message = "Book a Flight")
        self.navBarBookFlightButton.bind("<Enter>", lambda event, widget = "NavBarBookFlight": self.startHover(event, widget))
        self.navBarBookFlightButton.bind("<Leave>", lambda event, widget = "NavBarBookFlight": self.endHover(event, widget))
        self.navBarBlogButton = ctk.CTkLabel(master = self.background, width = 149, height = 34, text = "Blog", font = ("Plus Jakarta Sans", 24), bg_color = "#FFFFFF", anchor = "w")
        self.navBarBlogButton.place(x = 828, y = 36)
        blogToolTip = CTkToolTip(self.navBarBlogButton, message = "Check out our Blogs")
        self.navBarBlogButton.bind("<Enter>", lambda event, widget = "NavBarBlog": self.startHover(event, widget))
        self.navBarBlogButton.bind("<Leave>", lambda event, widget = "NavBarBlog": self.endHover(event, widget))

        self.navBarLoginButton =  ctk.CTkLabel(master = self.background, width = 120, height = 48, text = "", image = imageLoader.Images().homePageLoginButton, bg_color ="#FFFFFF")
        self.navBarLoginButton.place(x = 910, y = 30)
        navBarLoginToolTip = CTkToolTip(self.navBarLoginButton, message = "Login to Book Flights")
        self.navBarLoginButton.bind("<Enter>", lambda event, widget = "Login": self.startHover(event, widget))
        self.navBarLoginButton.bind("<Leave>", lambda event, widget = "Login": self.endHover(event, widget))
        self.navBarLoginButton.bind("<Button-1>", lambda event, widget = "Login": self.pressWidget(event, widget))

        self.navBarSignInButton = ctk.CTkLabel(master = self.background, width = 120, height = 48, text = "", image = imageLoader.Images().homePageSignInButton, bg_color ="#FFFFFF")
        self.navBarSignInButton.place(x = 1056, y = 30)
        navBarSignInToolTip = CTkToolTip(self.navBarSignInButton, message = "Create Account to Book Flights")
        self.navBarSignInButton.bind("<Enter>", lambda event, widget = "SignIn": self.startHover(event, widget))
        self.navBarSignInButton.bind("<Leave>", lambda event, widget = "SignIn": self.endHover(event, widget))
        self.navBarSignInButton.bind("<Button-1>", lambda event, widget = "SignIn": self.pressWidget(event, widget))

        homePageTitle = ctk.CTkLabel(master = self.background, width = 400, height = 42, text = "Discover Places", font = ("Plus Jakarta Sans", 30, "bold"), anchor = "w", bg_color = "#FFFFFF")
        homePageTitle.place(x = 23, y = 474)
        homePageSlogan = ctk.CTkLabel(master = self.background, width = 507, height = 62, text = "Find your perfect flight with JetSetGo—\nbook now and take off to adventure!", anchor = "w", bg_color = "#FFFFFF", font = ("Plus Jakarta Sans", 26), justify = "left")
        homePageSlogan.place(x = 23, y = 527)

        #Recommendations
        self.allRec = ctk.CTkLabel(master = self.background, width = 82, height = 46, text = "", image = imageLoader.Images().allRecommendSelected, bg_color ="#FFFFFF")
        self.allRec.place(x = 23, y = 610)
        self.allRec.bind("<Button-1>", lambda event, widget = "All": self.pressWidget(event, widget))
        self.asianRec = ctk.CTkLabel(master = self.background, width = 73, height = 46, text = "", image = imageLoader.Images().asiaRecommend, bg_color ="#FFFFFF")
        self.asianRec.place(x = 129, y = 610)
        self.asianRec.bind("<Button-1>", lambda event, widget = "Asia": self.pressWidget(event, widget))
        self.europeRec = ctk.CTkLabel(master = self.background, width = 106, height = 46, text = "", image = imageLoader.Images().europeRecommend, bg_color ="#FFFFFF")
        self.europeRec.place(x = 226, y = 610)
        self.europeRec.bind("<Button-1>", lambda event, widget = "Europe": self.pressWidget(event, widget))
        self.middleEastRec = ctk.CTkLabel(master = self.background, width = 126, height = 46, text = "", image = imageLoader.Images().middleEastRecommend, bg_color ="#FFFFFF")
        self.middleEastRec.place(x = 356, y = 610)
        self.middleEastRec.bind("<Button-1>", lambda event, widget = "MiddleEast": self.pressWidget(event, widget))
        self.africaRec = ctk.CTkLabel(master = self.background, width = 86, height = 46, text = "", image = imageLoader.Images().africaRecommend, bg_color ="#FFFFFF")
        self.africaRec.place(x = 23, y = 677)
        self.africaRec.bind("<Button-1>", lambda event, widget = "Africa": self.pressWidget(event, widget))
        self.americaRec = ctk.CTkLabel(master = self.background, width = 104, height = 46, text = "", image = imageLoader.Images().americanRecommend, bg_color ="#FFFFFF")
        self.americaRec.place(x = 129, y = 677)
        self.americaRec.bind("<Button-1>", lambda event, widget = "America": self.pressWidget(event, widget))
        self.australiaRec = ctk.CTkLabel(master = self.background, width = 97, height = 46, text = "", image = imageLoader.Images().australiaRecommend, bg_color ="#FFFFFF")
        self.australiaRec.place(x = 253, y = 677)
        self.australiaRec.bind("<Button-1>", lambda event, widget = "Australia": self.pressWidget(event, widget))

        self.ad1 = ctk.CTkLabel(master = self.background, text = "", width = 211, height = 151, bg_color = "#FFFFFF", image = imageLoader.Images().allTurkeyAd1)
        self.ad1.place(x = 525, y = 579)
        self.ad2 = ctk.CTkLabel(master = self.background, text = "", width = 213, height = 242, bg_color = "#FFFFFF", image = imageLoader.Images().allUsaAd2)
        self.ad2.place(x = 745, y = 500)
        self.ad3 = ctk.CTkLabel(master = self.background, text = "", width = 210, height = 181, bg_color = "#FFFFFF", image = imageLoader.Images().allJapanAd3)
        self.ad3.place(x = 966, y = 471)

        #Book Flights
        self.bookFlightButton = ctk.CTkLabel(master = self.background, text = "", width = 234, height = 87, bg_color = "#FFFFFF", image = imageLoader.Images().homePageBookFlightsButton)
        self.bookFlightButton.place(x = 956, y = 655)
        bookFlightToolTip = CTkToolTip(self.bookFlightButton, message = "Book Flights")
        self.bookFlightButton.bind("<Enter>", lambda event, widget = "BookFlight": self.startHover(event, widget))
        self.bookFlightButton.bind("<Leave>", lambda event, widget = "BookFlight": self.endHover(event, widget))

        #Close Window Button
        self.closeWindowButton = ctk.CTkLabel(master = self.background, text = "", width = 22, height = 22, image = imageLoader.Images().closeWindow, bg_color ="#FFFFFF")
        self.closeWindowButton.place(x = 1178, y = 0)
        closeWindowToolTip = CTkToolTip(self.closeWindowButton, message = "Close Window")
        self.closeWindowButton.bind("<Button-1>", lambda event, widget = "CloseWindow" : self.pressWidget(event, widget))
        self.closeWindowButton.bind("<Enter>", lambda event, widget = "CloseWindow": self.startHover(event, widget))
        self.closeWindowButton.bind("<Leave>", lambda event, widget = "CloseWindow": self.endHover(event, widget))

    def startHover(self, event, widget : str) -> None:
        if widget == "SignIn":
            self.navBarSignInButton.configure(image = imageLoader.Images().homePageSignInButtonHover)
        elif widget == "Login":
            self.navBarLoginButton.configure(image = imageLoader.Images().homePageLoginButtonHover)
        elif widget == "BookFlight":
            self.bookFlightButton.configure(image = imageLoader.Images().homePageBookFlightsButtonHover)
        elif widget == "NavBarBookFlight":
            self.navBarBookFlightButton.configure(text_color = "#003DF6")
        elif widget == "NavBarBlog":
            self.navBarBlogButton.configure(text_color = "#003DF6")
        elif widget == "CloseWindow":
            self.closeWindowButton.configure(image = imageLoader.Images().closeWindowHover)

    def endHover(self, event, widget : str) -> None:
        if widget == "SignIn":
            self.navBarSignInButton.configure(image = imageLoader.Images().homePageSignInButton)
        elif widget == "Login":
            self.navBarLoginButton.configure(image = imageLoader.Images().homePageLoginButton)
        elif widget == "BookFlight":
            self.bookFlightButton.configure(image = imageLoader.Images().homePageBookFlightsButton)
        elif widget == "NavBarBookFlight":
            self.navBarBookFlightButton.configure(text_color = "#000000")
        elif widget == "NavBarBlog":
            self.navBarBlogButton.configure(text_color = "#000000")
        elif widget == "CloseWindow":
            self.closeWindowButton.configure(image = imageLoader.Images().closeWindow)

    def pressWidget(self, event, widget : str) -> None:
        recommendationSelected = {
            "All" : lambda :  self.allRec.configure(image = imageLoader.Images().allRecommendSelected),
            "Asia" : lambda :  self.asianRec.configure(image = imageLoader.Images().asiaRecommendSelected),
            "Europe" : lambda :  self.europeRec.configure(image = imageLoader.Images().europeRecommendSelected),
            "MiddleEast" : lambda :  self.middleEastRec.configure(image = imageLoader.Images().middleEastRecommendSelected),
            "Africa" : lambda :  self.africaRec.configure(image = imageLoader.Images().africaRecommendSelected),
            "Australia" : lambda :  self.australiaRec.configure(image = imageLoader.Images().australiaRecommendSelected),
            "America" : lambda :  self.americaRec.configure(image = imageLoader.Images().americanRecommendSelected)
        }
        recommendationDeSelected = {
            "All" : lambda : self.allRec.configure(image = imageLoader.Images().allRecommend),
            "Asia" : lambda :  self.asianRec.configure(image = imageLoader.Images().asiaRecommend),
            "Europe" : lambda :  self.europeRec.configure(image = imageLoader.Images().europeRecommend),
            "MiddleEast" : lambda :  self.middleEastRec.configure(image = imageLoader.Images().middleEastRecommend),
            "Africa" : lambda :  self.africaRec.configure(image = imageLoader.Images().africaRecommend),
            "Australia" : lambda :  self.australiaRec.configure(image = imageLoader.Images().australiaRecommend),
            "America" : lambda :  self.americaRec.configure(image = imageLoader.Images().americanRecommend)
        }
        if widget == "SignIn":
            self.withdraw()
            CreateAccountPage(self)
        elif widget == "Login":
            self.withdraw()
            LoginPage(self)
        elif widget == "All":
            if self.advertisement == "All": return
            else:
                recommendationDeSelected[self.advertisement]()
                recommendationSelected["All"]()
                self.ad1.configure(image = imageLoader.Images().allTurkeyAd1)
                self.ad2.configure(image = imageLoader.Images().allUsaAd2)
                self.ad3.configure(image = imageLoader.Images().allJapanAd3)
                self.advertisement = "All"
        elif widget == "Asia":
            if self.advertisement == "Asia": return
            else:
                recommendationDeSelected[self.advertisement]()
                recommendationSelected["Asia"]()
                self.ad1.configure(image = imageLoader.Images().asiaChinaAd1)
                self.ad2.configure(image = imageLoader.Images().asiaIndonesiaAd2)
                self.ad3.configure(image = imageLoader.Images().asiaIndiaAd3)
                self.advertisement = "Asia"
        elif widget == "Europe":
            if self.advertisement == "Europe": return
            else:
                recommendationDeSelected[self.advertisement]()
                recommendationSelected["Europe"]()
                self.ad1.configure(image = imageLoader.Images().europeItalyAd1)
                self.ad2.configure(image = imageLoader.Images().europeFranceAd2)
                self.ad3.configure(image = imageLoader.Images().europeGreeceAd3)
                self.advertisement = "Europe"
        elif widget == "MiddleEast":
            if self.advertisement == "MiddleEast": return
            else:
                recommendationDeSelected[self.advertisement]()
                recommendationSelected["MiddleEast"]()
                self.ad1.configure(image = imageLoader.Images().middleEastEgyptAd1)
                self.ad2.configure(image = imageLoader.Images().middleEastUAEAd2)
                self.ad3.configure(image = imageLoader.Images().middleEastJordanAd3)
                self.advertisement = "MiddleEast"
        elif widget == "Africa":
            if self.advertisement == "Africa": return
            else:
                recommendationDeSelected[self.advertisement]()
                recommendationSelected["Africa"]()
                self.ad1.configure(image = imageLoader.Images().africaSouthAfricaAd1)
                self.ad2.configure(image = imageLoader.Images().africaMoroccoAd2)
                self.ad3.configure(image = imageLoader.Images().africaKenyaAd3)
                self.advertisement = "Africa"
        elif widget == "Australia":
            if self.advertisement == "Australia": return
            else:
                recommendationDeSelected[self.advertisement]()
                recommendationSelected["Australia"]()
                self.ad1.configure(image = imageLoader.Images().australiaSydneyAd1)
                self.ad2.configure(image = imageLoader.Images().australiaMelbourneAd2)
                self.ad3.configure(image = imageLoader.Images().australiaPerthAd3)
                self.advertisement = "Australia"
        elif widget == "America":
            if self.advertisement == "America": return
            else:
                recommendationDeSelected[self.advertisement]()
                recommendationSelected["America"]()
                self.ad1.configure(image = imageLoader.Images().americaMexicoAd1)
                self.ad2.configure(image = imageLoader.Images().americaCanadaAd2)
                self.ad3.configure(image = imageLoader.Images().americaBrazilAd3)
                self.advertisement = "America"
        elif widget == "CloseWindow":
            self.destroy()

    def startMovingWindow(self, event) -> None:
        self.xOffSet = event.x
        self.yOffSet = event.y

    def dragWindow(self, event) -> None:
        if self.xOffSet is not None and self.yOffSet is not None:
            self.geometry(f'+{event.x_root - self.xOffSet}+{event.y_root - self.yOffSet}')

    def openWindowCentreOfScreen(self, width : int, height : int) -> None:
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screenHeight - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')

if "__main__" == __name__:
    JetSetGo = HomePage()
    JetSetGo.mainloop()
