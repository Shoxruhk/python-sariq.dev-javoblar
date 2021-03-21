# biz bu dasturda lambda haqida tanishamiz
# lambda bu bir martalik funksiya hisoblanadi va faqat bitta qiymat qabul qiladi lekin cheksiz argument qabul qiladi
# qani bolmasa boshladik bir sinaylikchi hammaga omad

# sozlar nomli ro'yhat yaratim olamiz
sozlar = ['anor','behi','anjir','qalampir','salom','dunyo','pomidor','anhor','kompyuter','ism','shoxrux']
print(list(filter(lambda matn:(matn.startswith('a') or matn.endswith("m")),sozlar)))
