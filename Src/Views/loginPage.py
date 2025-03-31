import time

import customtkinter as ctk

from CTkToolTip import CTkToolTip
from Src.Util import imageLoader
from Src.Util import sendEmail
import re, sqlite3, time

ctk.set_appearance_mode("light")

class LoginPage(ctk.CTkToplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.background = None
        self.wm_overrideredirect(True)

        self.openWindowCentreOfScreen(936, 563)
        self.xOffSet = None
        self.yOffSet = None

        self.viewPassword = False
        self.ButtonType = "code"
        self.confirmationCode = None
        self.setupGui()

    def setupGui(self):
        self.background = ctk.CTkLabel(master = self, image = imageLoader.Images().loginImage, width = 936, height = 563, text ="")
        self.background.pack(fill = "both", expand = True)
        self.background.bind("<Button-1>", self.startMovingWindow)
        self.background.bind("<B1-Motion>", self.dragWindow)

        loginPageTitle = ctk.CTkLabel(master = self.background, text = "Welcome Back", font = ("Inter", 36, "bold"), width = 315, height = 36, bg_color = "#FFFFFF", anchor = "w", text_color = "#0C1421")
        loginPageTitle.place(x = 496, y = 38)
        loginPageDescription = ctk.CTkLabel(master = self.background, text = "Today is a new day. It's your day. You shape it.\nSign in to start managing your flight tickets.", width = 388, height = 54, bg_color = "#FFFFFF", anchor = "w", justify = "left", font = ("Inter", 17, "normal"), text_color = "#0C1421")
        loginPageDescription.place(x = 501, y = 95)

        loginPageEmailHeading = ctk.CTkLabel(master = self.background, width = 41, height = 16, text = "Email", font = ("Roboto", 16), bg_color = "#FFFFFF")
        loginPageEmailHeading.place(x = 496, y = 170)
        self.loginPageEmailEntry = ctk.CTkEntry(master = self.background, width = 388, height = 48, placeholder_text = "Example@email.com", corner_radius = 10, bg_color = "#FFFFFF", text_color = "#0C1421")
        self.loginPageEmailEntry.place(x = 496, y = 194)

        loginPagePasswordHeading = ctk.CTkLabel(master = self.background, width = 41, height = 16, text = "Password", font = ("Roboto", 16), bg_color = "#FFFFFF", text_color = "#0C1421")
        loginPagePasswordHeading.place(x = 496, y = 260)
        self.loginPagePasswordEntry = ctk.CTkEntry(master = self.background, width = 388, height = 48, show = "*", placeholder_text = "Enter your password", corner_radius = 10, bg_color = "#FFFFFF")
        self.loginPagePasswordEntry.place(x = 496, y = 282)
        self.loginPageViewPasswordIcon = ctk.CTkLabel(master = self.loginPagePasswordEntry, image = imageLoader.Images().viewPassword, width = 24, height = 24, text ="")
        self.loginPageViewPasswordIcon.place(x = 352, y = 12)
        loginPageViewPasswordIconToolTip = CTkToolTip(self.loginPageViewPasswordIcon, message = "View your Password")
        self.loginPageViewPasswordIcon.bind("<Button-1>", self.passwordView)

        loginPageForgotPassword = ctk.CTkLabel(master = self.background, width = 132, height = 16, text = "Forgot Password?", font = ("Roboto", 16), bg_color = "#FFFFFF", text_color = "#1E4AE9", anchor = "e")
        loginPageForgotPassword.place(x = 751, y = 362)
        loginPageForgotPasswordToolTip = CTkToolTip(loginPageForgotPassword, message = "Reset your Password")
        loginPageForgotPassword.bind("<Button-1>", self.forgotPassword)

        loginPageButton = ctk.CTkButton(master = self.background, width = 388, height = 52, text = "Sign In", font = ("Roboto", 16), bg_color = "#FFFFFF", command = self.loginInSignIn)
        loginPageButton.place(x = 495, y = 402)

        loginPageCreateAccount = ctk.CTkLabel(master = self.background, width = 388, height = 16, text = "Create Account", font = ("Roboto", 16), bg_color = "#FFFFFF", text_color = "#1E4AE9", anchor = "center")
        loginPageCreateAccount.place(x = 495, y = 478)
        loginPageCreateAccount.bind("<Button-1>", self.goToCreateAccountPage)

        loginPageFooter = ctk.CTkLabel(master = self.background, width = 382, height = 16, text = "© AirVenture 2024 ALL RIGHTS RESERVED", bg_color = "#FFFFFF", font = ("Roboto", 16), text_color = "#0C1421")
        loginPageFooter.place(x = 496, y = 526)

        self.closeWindowButton = ctk.CTkLabel(master = self.background, text = "", width = 22, height = 22, image = imageLoader.Images().closeWindow, bg_color ="#FFFFFF")
        self.closeWindowButton.place(x = 914, y = 0)
        closeWindowToolTip = CTkToolTip(self.closeWindowButton, message = "Close Window")
        self.closeWindowButton.bind("<Button-1>", self.closeWindow)
        self.closeWindowButton.bind("<Enter>", self.startCloseWindowHover)
        self.closeWindowButton.bind("<Leave>", self.stopCloseWindowHover)

    def loginInSignIn(self) -> None:
        try:
            table = sqlite3.connect("Src/Database/airVentureDB.db")
            cursor = table.cursor()
            email = self.loginPageEmailEntry.get().strip()
            password = self.loginPagePasswordEntry.get().strip()
            try:
                data = cursor.execute("SELECT email FROM users").fetchall()
                data = [email[0] for email in data]
            except Exception as e:
                print(e)
            if email == "" or password == "": return self.emptyFields("login")
            elif not self.isValidemail(email): return self.incorrectEmailWarning("login")
            elif email not in data: return self.incorrectEmailNotLinked2Account("login")
            datas = cursor.execute("SELECT email, password, nameSurname FROM users WHERE email = ?", (email,)).fetchone()
            if password != datas[1]: return self.incorrectLoginPassword()
            elif datas[0] == email and datas[1] == password:
                self.root.account = datas
                self.destroy()
                BookFlightPage(self.root)
                print("Login Successful")
            cursor.close()
            table.close()
        except Exception as e:
            print(e)

    def forgotPassword(self, event) -> None:
        self.forgotPasswordFrame = ctk.CTkFrame(master = self.background, width = 415, height = 522, fg_color = "#FFFFFF", bg_color = "#FFFFFF")
        self.forgotPasswordFrame.place(x = 495, y = 24)
        forgetPasswordPageTitle = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 298, height = 36, bg_color = "#FFFFFF", text = "Reset Password", font = ("Inter", 36, "bold"), anchor = "w")
        forgetPasswordPageTitle.place(x = 14, y = 5)
        forgotPasswordPageDescription = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 388, height = 81, bg_color = "#FFFFFF", text = "Enter your email to receive a confirmation\ncode. Use the code to set a new password and\nregain access to your account.", justify = "left", font = ("Inter", 17), anchor = "w")
        forgotPasswordPageDescription.place(x = 14, y = 41)

        forgetPasswordPageEmailHeading = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 72, height = 16, text = "Email", font = ("Roboto", 16), anchor = "w", bg_color = "#FFFFFF")
        forgetPasswordPageEmailHeading.place(x = 14, y = 139)
        self.forgetPasswordPageEmailInput = ctk.CTkEntry(master = self.forgotPasswordFrame, width = 388, height = 48, placeholder_text = "Enter email", corner_radius = 10, bg_color = "#FFFFFF")
        self.forgetPasswordPageEmailInput.place(x = 14, y = 164)

        self.forgetPasswordSubmitButton = ctk.CTkButton(master = self.forgotPasswordFrame, command = lambda: self.sendCode(self.ButtonType), width = 388, height = 52, text = "Send Code", bg_color = "#FFFFFF", font = ("Roboto", 20))
        self.forgetPasswordSubmitButton.place(x = 14, y = 438)
        forgetPasswordPageFooter = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 382, height = 16, text = "© AirVenture 2024 ALL RIGHTS RESERVED", bg_color = "#FFFFFF", font = ("Roboto", 16), text_color = "#0C1421")
        forgetPasswordPageFooter.place(x = 17, y = 506)

    def sendCode(self, buttonType : str) -> None:
        try:
            table = sqlite3.connect("Src/Database/airVentureDB.db")
            cursor = table.cursor()
            email = self.forgetPasswordPageEmailInput.get()
            if buttonType == "code":
                try:
                    data = cursor.execute("SELECT email FROM users").fetchall()
                    data = [email[0] for email in data]
                except Exception as e:
                    print(e)
                if email == "": return self.emptyFields("forgotPassword")
                elif not self.isValidemail(email): return self.incorrectEmailWarning("forgotPassword")
                elif email not in data: return self.incorrectEmailNotLinked2Account("forgotPassword")
                else:
                    self.ButtonType = "SaveNewPassword"
                    self.confirmationCode = sendEmail.generate6CharacterToken()
                    self.resetPasswordCodeSent()
                    sendEmail.sendTokenEmail(email, self.confirmationCode)
                    self.after(5000, self.resetPasswordCodeExpired)
            elif buttonType == "SaveNewPassword":
                try:
                    codeEntered = ""
                    for counter in range(1, 7):
                        entryPoint = f"entry{counter}"
                        codeEntered += getattr(self, entryPoint).get()
                    newPassword = self.newPasswordEntry.get()
                    if self.checkEmptyCodeEntry(): return self.incorrectMissingCode()
                    print(1)
                    if self.confirmationCode == None: return self.incorrectResetCodeExpire()
                    print(2)
                    if codeEntered != self.confirmationCode: return self.incorrectResetCode()
                    print(3)
                    if newPassword == "": return self.incorrectNewPasswordFieldEmpty()
                    print(4)
                    data = cursor.execute("UPDATE users SET password = ? WHERE email = ?", (newPassword, email))
                    table.commit()
                    self.correctPasswordReset()
                    self.forgotPasswordFrame.destroy()
                except Exception as e:
                    print(e)
            cursor.close()
            table.close()
        except Exception as e:
            print(e)

    def checkEmptyCodeEntry(self):
        for counter in range(1, 7):
            entryPoint = f"entry{counter}"
            entryData = getattr(self, entryPoint).get()
            if not entryData.strip():
                return True
        return False

    def incorrectLoginPassword(self) -> None:
        incorrectPassword = ctk.CTkLabel(master = self.background, width = 390, height = 53, text = "", image = imageLoader.Images().errorIncorrectPassword)
        incorrectPassword.place(x = 495, y = 402)
        self.after(3000, incorrectPassword.destroy)

    def resetPasswordCodeExpired(self) -> None:
        self.confirmationCode = None
        print("Expired")
        print(self.confirmationCode)

    def correctPasswordReset(self) ->  None:
        self.forgotPasswordFrame.destroy()
        passwordSuccess = ctk.CTkLabel(master = self.background, width = 390, height = 53, text = "", image = imageLoader.Images().successPasswordReset, bg_color ="#FFFFFF")
        passwordSuccess.place(x = 495, y = 402)
        self.after(3000, passwordSuccess.destroy)

    def incorrectResetCodeExpire(self) ->  None:
        resetCodeExpired = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorResetCodeExpired, bg_color ="#FFFFFF")
        resetCodeExpired.place(x = 12, y = 437)
        self.after(3000, resetCodeExpired.destroy)
        self.forgotPasswordFrame.destroy()
        self.forgotPasswordFrame.mainloop()
        self.ButtonType = "code"

    def incorrectPasswordLength(self) ->  None:
        passwordLength = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorPasswordLength, bg_color ="#FFFFFF")
        passwordLength.place(x = 12, y = 437)
        self.after(3000, passwordLength.destroy)

    def incorrectEmailNotLinked2Account(self, frame : str) ->  None:
        if frame == "forgotPassword":
            emailNotLinked = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorNewPasswordEmailNotFound, bg_color ="#FFFFFF")
            emailNotLinked.place(x = 12, y = 437)
            self.after(3000, lambda : self.redirectToCreateAccountPage(emailNotLinked))
        elif frame == "login":
            emailNotLinked = ctk.CTkLabel(master = self.background, width = 390, height = 53, text = "", image = imageLoader.Images().errorNewPasswordEmailNotFound, bg_color ="#FFFFFF")
            emailNotLinked.place(x = 495, y = 402)
            self.after(3000, lambda : self.redirectToCreateAccountPage(emailNotLinked))

    def redirectToCreateAccountPage(self, label : ctk.CTkLabel) -> None:
        label.destroy()
        self.destroy()
        from Src.Views.createAccountPage import CreateAccountPage
        CreateAccountPage(self.root)

    def incorrectNewPasswordFieldEmpty(self) ->  None:
        passwordEmptyField = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorNewPasswordFieldEmpty, bg_color ="#FFFFFF")
        passwordEmptyField.place(x = 12, y = 437)
        self.after(3000, passwordEmptyField.destroy)

    def incorrectResetCode(self) ->  None:
        wrongResetCode = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorResetCodeWrong, bg_color ="#FFFFFF")
        wrongResetCode.place(x = 12, y = 437)
        self.after(3000, wrongResetCode.destroy)

    def incorrectMissingCode(self) ->  None:
        missingResetCode = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorMissingCode, bg_color ="#FFFFFF")
        missingResetCode.place(x = 12, y = 437)
        self.after(3000, missingResetCode.destroy)

    def incorrectEmailWarning(self, frame : str) ->  None:
        if frame == "forgotPassword":
            emailWarning = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorEmail, bg_color ="#FFFFFF")
            emailWarning.place(x = 12, y = 437)
            self.after(3000, emailWarning.destroy)
        elif frame == "login":
            emailWarning = ctk.CTkLabel(master = self.background, width = 390, height = 53, text = "", image = imageLoader.Images().errorEmail, bg_color ="#FFFFFF")
            emailWarning.place(x = 495, y = 402)
            self.after(3000, emailWarning.destroy)

    def emptyFields(self, frame : str) -> None:
        if frame == "forgotPassword":
            emptyFields = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorEmptyField, bg_color ="#FFFFFF")
            emptyFields.place(x = 12, y = 437)
            self.after(3000, emptyFields.destroy)
        elif frame == "login":
            emptyFields = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 390, height = 53, text = "", image = imageLoader.Images().errorEmptyField, bg_color ="#FFFFFF")
            emptyFields.place(x = 495, y = 402)
            self.after(3000, emptyFields.destroy)

    def resetPasswordCodeSent(self) -> None:
        self.forgetPasswordSubmitButton.configure(text = "Change Password")
        resetPasswordMessage = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 336, height = 26, text = "Check your email for confirmation code.", bg_color = "#FFFFFF", font = ("Inter", 17), anchor = "w")
        resetPasswordMessage.place(x = 14, y = 223)
        resetCodeHeading = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 80, height = 16, text = "Enter Code", bg_color = "#FFFFFF", font = ("Roboto", 16), anchor = "w")
        resetCodeHeading.place(x = 14, y = 256)
        self.enterCode()
        newPasswordHeading = ctk.CTkLabel(master = self.forgotPasswordFrame, width = 151, height = 16, text = "Enter New Password", bg_color = "#FFFFFF", font = ("Roboto", 16), anchor = "w")
        newPasswordHeading.place(x = 14, y = 347)

        self.newPasswordEntry = ctk.CTkEntry(master = self.forgotPasswordFrame, width = 388, height = 48, placeholder_text = "At least 8 characters", bg_color = "#FFFFFF", show = "*")
        self.newPasswordEntry.place(x = 14, y = 372)
        self.newPasswordEntryPasswordIcon = ctk.CTkLabel(master = self.newPasswordEntry, image = imageLoader.Images().viewPassword, width = 24, height = 24, text ="")
        self.newPasswordEntryPasswordIcon.place(x = 352, y = 12)
        newPasswordEntryPasswordToolTip = CTkToolTip(self.newPasswordEntryPasswordIcon, message = "View your Password")
        self.newPasswordEntryPasswordIcon.bind("<Button-1>", self.newPasswordView)

    def enterCode(self) -> None:
        self.entry1 = ctk.CTkEntry(master = self.forgotPasswordFrame, width = 48, height = 48, bg_color = "#FFFFFF", placeholder_text = "______")
        self.entry1.place(x = 12, y = 281)
        self.entry2 = ctk.CTkEntry(master = self.forgotPasswordFrame, width = 48, height = 48, bg_color = "#FFFFFF", placeholder_text = "______")
        self.entry2.place(x = 78, y = 281)
        self.entry3 = ctk.CTkEntry(master = self.forgotPasswordFrame, width = 48, height = 48, bg_color = "#FFFFFF", placeholder_text = "______")
        self.entry3.place(x = 144, y = 281)
        self.entry4 = ctk.CTkEntry(master = self.forgotPasswordFrame, width = 48, height = 48, bg_color = "#FFFFFF", placeholder_text = "______")
        self.entry4.place(x = 210, y = 281)
        self.entry5 = ctk.CTkEntry(master = self.forgotPasswordFrame, width = 48, height = 48, bg_color = "#FFFFFF", placeholder_text = "______")
        self.entry5.place(x = 276, y = 281)
        self.entry6 = ctk.CTkEntry(master = self.forgotPasswordFrame, width = 48, height = 48, bg_color = "#FFFFFF", placeholder_text = "______")
        self.entry6.place(x = 342, y = 281)

    def goToCreateAccountPage(self, event) -> None:
        try:
            self.destroy()
            from Src.Views.createAccountPage import CreateAccountPage
            CreateAccountPage(self.root)
        except Exception as e:
            print(e)

    def passwordView(self, event) -> None:
        try:
            if self.viewPassword:
                self.loginPagePasswordEntry.configure(show = "*")
                self.loginPageViewPasswordIcon.configure(image = imageLoader.Images().viewPassword)
                self.viewPassword = False
            elif not self.viewPassword:
                self.loginPagePasswordEntry.configure(show = "")
                self.loginPageViewPasswordIcon.configure(image = imageLoader.Images().noViewPassword)
                self.viewPassword = True
        except Exception as e:
            print(e)

    def newPasswordView(self, event) -> None:
        try:
            if self.viewPassword:
                self.newPasswordEntry.configure(show = "*")
                self.newPasswordEntryPasswordIcon.configure(image = imageLoader.Images().viewPassword)
                self.viewPassword = False
            elif not self.viewPassword:
                self.newPasswordEntry.configure(show = "")
                self.newPasswordEntryPasswordIcon.configure(image = imageLoader.Images().noViewPassword)
                self.viewPassword = True
        except Exception as e:
            print(e)

    def isValidemail(self, email : str) -> bool:
        regexPatternEmailValidator = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(regexPatternEmailValidator, email))

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

        