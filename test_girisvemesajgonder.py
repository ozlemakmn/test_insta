from girisUserInfo import username ,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys
from constants.globalconstants import *
import pytest
from time import sleep

class Test_İnsGiris:
    def setup_method(self): #her test öncesi çalışır.
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
    
    
    def teardown_method(self): #her test bitiminden sonra çalışır.
        self.driver.quit()
        
    @pytest.mark.skip     
    def test_kayit_ol(self):
        kayitolbutton=self.waitForElementVisible((By.XPATH,kayiyolbutton_id))
        kayitolbutton.click()
        emailInput=self.waitForElementVisible((By.NAME,emailInput_id))
        emailInput.send_keys("ozlemakman16")
        adInput =self.waitForElementVisible((By.NAME,adInput_id))
        adInput.send_keys("özlem")
        kullaniciad=self.waitForElementVisible((By.NAME,kullaniciad_id))
        kullaniciad.send_keys("akman123")
        öneri =self.waitForElementVisible((By.XPATH,öneri_id))
        öneri.click()
        öneri2=self.waitForElementVisible((By.XPATH,öneri2_id))
        öneri2.click()
        passwordInput=self.waitForElementVisible((By.NAME,paswordInput_İd))
        passwordInput.send_keys("123456789")
        kayitolusturbutton=self.waitForElementVisible((By.XPATH,kayitolusturbutton_id))
        kayitolusturbutton.click()
        errorMessage=self.waitForElementVisible((By.ID,errorMessage_id))
        assert errorMessage.text == errorMessage_text

        
    @pytest.mark.skip    
    def test_invalidlogin(self):
        self.driver.get("https://www.instagram.com/accounts/login")
        emailInputt = self.waitForElementVisible((By.NAME,email_id))
        emailInputt.send_keys("22222222")
        passwordInputt = self.waitForElementVisible((By.NAME,password_id))
        passwordInputt.send_keys("555555s")
        loginButton = self.waitForElementVisible((By.XPATH,loginbutton_id))
        loginButton.click()
        sleep(20)
        errormessagee= self.waitForElementVisible((By.XPATH,errormessagee_id))
        assert errormessagee.text == errormessagee_text 
        sleep(20) 
        
  
    @pytest.mark.skip    
    def test_sifremi_unuttum(self):
    
        unuttumbutton = self.waitForElementVisible((By.XPATH,unuttumbutton_id))
        unuttumbutton.click()    
       
        unuttumInput=self.waitForElementVisible((By.NAME,unuttumInput_id))
        unuttumInput.send_keys("ozlemlewebtasarim@gmail.com")
        Baglantigonder=self.waitForElementVisible((By.XPATH,Baglantigonder_id))
        Baglantigonder.click()
            
  
    @pytest.mark.skip
    def test_giris(self):
        emailInput=self.waitForElementVisible((By.NAME,email_id))
        passwordInput=self.waitForElementVisible((By.NAME,password_id))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(emailInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform() #depoladığım aksiyonları çalıştır
        loginButton = self.waitForElementVisible((By.XPATH,loginButton_id))
        loginButton.click()
        kaydedilsinmi=self.waitForElementVisible((By.XPATH,kaydedilsinmi_id))
        kaydedilsinmi.click()
        bildirimler=self.waitForElementVisible((By.XPATH,bildirimler_id))
        bildirimler.click()
        mesaj=self.waitForElementVisible((By.XPATH,mesaj_id))
        mesaj.click()
        MesajGonder=self.waitForElementVisible((By.XPATH,MesajGonder_id))
        actions = ActionChains(self.driver)
        actions.move_to_element(MesajGonder).perform()
        MesajGonder.click()
        mesajInput = self.waitForElementVisible((By.XPATH,mesajInput_id))
        mesajInput.send_keys("Merhaba, Nasılsınız?",Keys.ENTER)
    
    def waitForElementVisible(self,locator,timeout=5):
     return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
 
 
    
