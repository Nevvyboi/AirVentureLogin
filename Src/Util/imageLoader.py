import customtkinter as ctk
from PIL import Image
import os, sys

def getBasePath():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getImagePath(fileName) -> str:
    components_folder = os.path.join(getBasePath(), "Components")
    return os.path.join(components_folder, fileName)

class Images:
    def __init__(self):
        self.closeWindow : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("closeWindowIcon.png")), size = (22, 22))
        self.closeWindowHover : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("closeWindowHoverIcon.png")), size = (22, 22))
        self.loginImage : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("loginPage.png")), size = (936, 563))
        self.createAccountPage : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("createAccountPage.png")), size = (936, 563))
        self.viewPassword : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("viewPassword.png")), size = (24, 24))
        self.noViewPassword : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("noViewPassword.png")), size = (24, 24))
        self.homePage : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("homePage.png")), size = (1200, 750))
        self.homePageLoginButton : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("homePageLoginButton.png")), size = (120, 48))
        self.homePageLoginButtonHover : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("homePageLoginButtonHover.png")), size = (120, 48))
        self.homePageSignInButton : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("homePageSignInButton.png")), size = (120, 48))
        self.homePageSignInButtonHover : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("homePageSignInButtonHover.png")), size = (120, 48))
        self.homePageLogo = ctk.CTkImage(Image.open(getImagePath("homePageLogo.png")), size = (151, 35))
        self.homePageBookFlightsButton : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("bookFlightButton.png")), size = (234, 87))
        self.homePageBookFlightsButtonHover : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("bookFlightHover.png")), size = (234, 87))
        #Recommendation Button
        self.allRecommendSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("allRecSelected.png")), size = (82, 46))
        self.allRecommend : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("allRec.png")), size = (82, 46))
        self.asiaRecommendSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("asianRecSelected.png")), size = (73, 46))
        self.asiaRecommend : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("asianRec.png")), size = (73, 46))
        self.europeRecommendSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("europeRecSelected.png")), size = (106, 46))
        self.europeRecommend : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("europeRec.png")), size = (106, 46))
        self.middleEastRecommendSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("middleEastRecSelected.png")), size = (126, 46))
        self.middleEastRecommend : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("middleEastRec.png")), size = (126, 46))
        self.africaRecommendSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("africaRecSelected.png")), size = (86, 46))
        self.africaRecommend : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("africaRec.png")), size = (86, 46))
        self.americanRecommendSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("americaRecSelected.png")), size = (86, 46))
        self.americanRecommend : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("americaRec.png")), size = (86, 46))
        self.australiaRecommendSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("australiaRecSelected.png")), size = (97, 46))
        self.australiaRecommend : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("australiaRec.png")), size = (97, 46))

        #Ads (All)
        self.allTurkeyAd1 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("allTurkey.png")), size = (211, 151))
        self.allUsaAd2 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("allUsa.png")), size = (213, 242))
        self.allJapanAd3 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("allJapan.png")), size = (210, 181))
        #Ads (Asia)
        self.asiaChinaAd1 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("asianChina.png")), size = (211, 151))
        self.asiaIndonesiaAd2 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("asianIndonesia.png")), size = (213, 242))
        self.asiaIndiaAd3 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("asianIndia.png")), size = (210, 181))
        #Ads (Europe)
        self.europeItalyAd1 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("europeItaly.png")), size = (211, 151))
        self.europeFranceAd2 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("europeFrance.png")), size = (213, 242))
        self.europeGreeceAd3 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("europeGreece.png")), size = (210, 181))
        #Ads (Middle East)
        self.middleEastEgyptAd1 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("middleEastEqypt.png")), size = (211, 151))
        self.middleEastUAEAd2 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("middleEastUAE.png")), size = (213, 242))
        self.middleEastJordanAd3 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("middleEastJordan.png")), size = (210, 181))
        #Ads (Africa)
        self.africaSouthAfricaAd1 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("africaSouthAfrica.png")), size = (211, 151))
        self.africaMoroccoAd2 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("africaMorocco.png")), size = (213, 242))
        self.africaKenyaAd3 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("africaKenya.png")), size = (210, 181))
        #Ads (Australia)
        self.australiaSydneyAd1 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("australiaSydney.png")), size = (211, 151))
        self.australiaMelbourneAd2 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("australiaMelbourne.png")), size = (213, 242))
        self.australiaPerthAd3 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("australiaPerth.png")), size = (210, 181))
        #Ads (America)
        self.americaMexicoAd1 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("americaMexico.png")), size = (211, 151))
        self.americaCanadaAd2 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("americaCanada.png")), size = (213, 242))
        self.americaBrazilAd3 : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("americaBrazil.png")), size = (210, 181))

        self.errorEmail : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorIncorrectEmail.png")), size = (390, 53))
        self.errorEmptyField : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorEmptyFields.png")), size = (390, 53))
        self.errorMissingCode : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorMissingCode.png")), size = (390, 53))
        self.errorResetCodeWrong : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorResetCodeInvalid.png")), size = (390, 53))
        self.errorNewPasswordFieldEmpty : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorEmptyNewPassword.png")), size = (390, 53))
        self.errorNewPasswordEmailNotFound : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorForgotPasswordEmailNotFound.png")), size = (390, 53))
        self.errorPasswordLength : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorPasswordLength.png")), size = (390, 53))
        self.errorResetCodeExpired : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorResetCodeExpired.png")), size = (390, 53))
        self.errorIncorrectPassword : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorIncorrectPassword.png")), size = (390, 53))
        self.errorEmailUsedAlready : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("errorEmailAlreadyBinded.png")), size = (390, 53))
        self.successPasswordReset : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("successPasswordReset.png")), size = (390, 53))

        self.flightTicketPage : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightTicketPage.png")), size = (1200, 750))
        self.flightNavBarHome : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageHomeBar.png")), size = (137, 34))
        self.flightNavBarHomeHover : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageHomeBarHover.png")), size = (137, 34))
        self.flightNavBarHomeSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageHomeBarSelected.png")), size = (144, 41))
        self.flightNavBarTicket : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageTicketBar.png")), size = (137, 34))
        self.flightNavBarTicketHover : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageTicketBarHover.png")), size = (137, 34))
        self.flightNavBarTicketSelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageTicketBarSelected.png")), size = (144, 41))
        self.flightNavBarHistory : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageHistoryBar.png")), size = (137, 34))
        self.flightNavBarHistoryHover : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageHistoryBarHover.png")), size = (137, 34))
        self.flightNavBarHistorySelected : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageHistoryBarSelected.png")), size = (144, 41))
        self.flightNavBarSetting : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageSettingsBar.png")), size = (137, 34))
        self.flightNavBarSettingHover : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageSettingsBarHover.png")), size = (137, 34))
        self.flightNavBarSettingSelected: ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageSettingsBarSelected.png")), size = (144, 41))
        self.flightPageImage : ctk.CTkImage = ctk.CTkImage(Image.open(getImagePath("flightPageImage.png")), size = (982, 714))
