import customtkinter as ctk
from CTkToolTip import CTkToolTip

from Src.Util import imageLoader
import sqlite3, re

class CreateAccountPage(ctk.CTkToplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.background = None
        self.wm_overrideredirect(True)

        self.openWindowCentreOfScreen(936, 563)
        self.xOffSet = None
        self.yOffSet = None

        self.viewPassword = False
        self.setupGui()

    def setupGui(self) -> None:
        self.background = ctk.CTkLabel(master = self, image = imageLoader.Images().createAccountPage, width = 936, height = 563, text ="")
        self.background.pack(fill = "both", expand = True)
        self.background.bind("<Button-1>", self.startMovingWindow)
        self.background.bind("<B1-Motion>", self.dragWindow)

        createAccountPageTitle = ctk.CTkLabel(master = self.background, text = "Create Account", font = ("Inter", 36, "bold"), width = 323, height = 36, anchor = "w", bg_color = "#FFFFFF", text_color = "#0C1421")
        createAccountPageTitle.place(x = 27, y = 30)

        createAccountPageNameHeading = ctk.CTkLabel(master = self.background, width = 44, height = 16, text = "Name Surname", font = ("Roboto", 16), bg_color = "#FFFFFF", text_color = "#0C1421")
        createAccountPageNameHeading.place(x = 27, y = 100)
        self.createAccountPageNameSurnameEntry = ctk.CTkEntry(master = self.background, width = 388, height = 48, placeholder_text = "John Doe", corner_radius = 10, bg_color = "#FFFFFF", text_color = "#0C1421")
        self.createAccountPageNameSurnameEntry.place(x = 27, y = 124)

        createAccountPageEmailHeading = ctk.CTkLabel(master = self.background, width = 44, height = 16, text = "Email", font = ("Roboto", 16), bg_color = "#FFFFFF", text_color = "#0C1421")
        createAccountPageEmailHeading.place(x = 27, y = 190)
        self.createAccountPageEmailEntry = ctk.CTkEntry(master = self.background, width = 388, height = 48, placeholder_text = "Example@email.com", corner_radius = 10, bg_color = "#FFFFFF", text_color = "#0C1421")
        self.createAccountPageEmailEntry.place(x = 27, y = 212)

        createAccountPagePasswordHeading = ctk.CTkLabel(master = self.background, width = 44, height = 16, text = "Password", font = ("Roboto", 16), bg_color = "#FFFFFF", text_color = "#0C1421")
        createAccountPagePasswordHeading.place(x = 27, y = 278)
        self.createAccountPagePasswordEntry = ctk.CTkEntry(master = self.background, width = 388, height = 48, placeholder_text = "At least 8 characters", corner_radius = 10, bg_color = "#FFFFFF", text_color = "#0C1421", show = "*")
        self.createAccountPagePasswordEntry.place(x = 27, y = 300)
        self.createAccountViewPasswordIcon = ctk.CTkLabel(master = self.createAccountPagePasswordEntry, image = imageLoader.Images().viewPassword, width = 24, height = 24, text ="")
        self.createAccountViewPasswordIcon.place(x = 352, y = 12)
        self.createAccountViewPasswordIcon.bind("<Button-1>", self.passwordView)

        createAccountPageSignIn = ctk.CTkLabel(master = self.background, width = 388, height = 16, text = "Sign In", font = ("Roboto", 16), bg_color = "#FFFFFF", text_color = "#1E4AE9", anchor = "center")
        createAccountPageSignIn.place(x = 27, y = 380)
        createAccountPageSignIn.bind("<Button-1>", self.goToSignInPage)

        createAccountPageButton = ctk.CTkButton(master = self.background, width = 388, height = 52, text = "Create Account", font = ("Roboto", 16), bg_color = "#FFFFFF", command = self.createAccount)
        createAccountPageButton.place(x = 27, y = 420)

        createAccountPageFooter = ctk.CTkLabel(master = self.background, width = 382, height = 16, text = "© AirVenture 2024 ALL RIGHTS RESERVED", bg_color = "#FFFFFF", font = ("Roboto", 16), text_color = "#0C1421")
        createAccountPageFooter.place(x = 27, y = 526)

        self.closeWindowButton = ctk.CTkLabel(master = self.background, text = "", width = 22, height = 22, image = imageLoader.Images().closeWindow, bg_color ="#FFFFFF")
        self.closeWindowButton.place(x = 914, y = 0)
        closeWindowToolTip = CTkToolTip(self.closeWindowButton, message = "Close Window")
        self.closeWindowButton.bind("<Button-1>", self.closeWindow)
        self.closeWindowButton.bind("<Enter>", self.startCloseWindowHover)
        self.closeWindowButton.bind("<Leave>", self.stopCloseWindowHover)

    def createAccount(self) -> None:
        try:
            table = sqlite3.connect("Src/Database/airVentureDB.db")
            cursor = table.cursor()
            try:
                data = cursor.execute("SELECT email FROM users").fetchall()
                data = [email[0] for email in data]
            except Exception as e:
                print(e)
            name = self.createAccountPageNameSurnameEntry.get()
            email = self.createAccountPageEmailEntry.get()
            password = self.createAccountPagePasswordEntry.get()
            if name == "" or email == "" or password == "": return self.emptyFields()
            elif not self.isValidemail(email): return self.incorrectEmailWarning()
            elif email in data: return self.incorrectAccountExistsAlready()
            elif len(password) < 8: return self.incorrectPasswordLength()
            else:
                cursor.execute("INSERT INTO users (nameSurname, email, password) VALUES (?, ?, ?)", (name, email, password))
                table.commit()
            cursor.close()
            table.close()
            self.destroy()
            self.root.account = (email, password, name)
        except Exception as e:
            print(e)

    def incorrectAccountExistsAlready(self) ->  None:
        emailWarning = ctk.CTkLabel(master = self.background, width = 390, height = 53, text = "", image = imageLoader.Images().errorEmailUsedAlready, bg_color ="#FFFFFF")
        emailWarning.place(x = 27, y = 420)
        self.after(3000, emailWarning.destroy)

    def incorrectEmailWarning(self) ->  None:
        emailWarning = ctk.CTkLabel(master = self.background, width = 390, height = 53, text = "", image = imageLoader.Images().errorEmail, bg_color ="#FFFFFF")
        emailWarning.place(x = 27, y = 420)
        self.after(3000, emailWarning.destroy)

    def incorrectPasswordLength(self) ->  None:
        passwordLength = ctk.CTkLabel(master = self.background, width = 390, height = 53, text = "", image = imageLoader.Images().errorPasswordLength, bg_color ="#FFFFFF")
        passwordLength.place(x = 27, y = 420)
        self.after(3000, passwordLength.destroy)

    def emptyFields(self) -> None:
        emptyFields = ctk.CTkLabel(master = self.background, width = 390, height = 53, text = "", image = imageLoader.Images().errorEmptyField, bg_color ="#FFFFFF")
        emptyFields.place(x = 27, y = 420)
        self.after(3000, emptyFields.destroy)

    def goToSignInPage(self, event) -> None:
        try:
            self.destroy()
            from Src.Views.loginPage import LoginPage
            LoginPage(self.root)
        except Exception as e:
            print(e)

    def isValidemail(self, email : str) -> bool:
        regexPatternEmailValidator = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(regexPatternEmailValidator, email))

    def passwordView(self, event) -> None:
        try:
            if self.viewPassword:
                self.createAccountPagePasswordEntry.configure(show = "*")
                self.createAccountViewPasswordIcon.configure(image = imageLoader.Images().viewPassword)
                self.viewPassword = False
            elif not self.viewPassword:
                self.createAccountPagePasswordEntry.configure(show = "")
                self.createAccountViewPasswordIcon.configure(image = imageLoader.Images().noViewPassword)
                self.viewPassword = True
        except Exception as e:
            print(e)

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

    def closeWindow(self, event) -> None:
        self.destroy()
        self.root.deiconify()

    def startCloseWindowHover(self, event) -> None:
        self.closeWindowButton.configure(image = imageLoader.Images().closeWindowHover)

    def stopCloseWindowHover(self, event) -> None:
        self.closeWindowButton.configure(image = imageLoader.Images().closeWindow)

