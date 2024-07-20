from captcha.image import ImageCaptcha
from PIL import Image

captcha_text = input("Введіть текст капчі: ")

captcha = ImageCaptcha()

captcha_image = captcha.generate(captcha_text)

captcha_image_pil = Image.open(captcha_image)

captcha_image_pil.save(captcha_text + ".png")

