from django.db import models

class Like(models.Model):
    category = models.CharField(max_length=20)
    store = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank=True, upload_to="review/%Y/%m/%d/")
    # image = models.ImageField(default='menu/no_image.png', upload_to="menu/%Y/%m/%d/") 기본 이미지
    feel = models.CharField(max_length=200)
    star = models.IntegerField(default=0)

    def __str__(self):
        return f'카테고리: {self.category}, 가게이름 : {self.store}, 이름: {self.name}, 가격: {self.price}, 느낀점: {self.feel}, 평점: {self.star}'

class Where(Like):
    pass

class Eat(Like):
    pass
