from django.db import models


class BookStoreBaseModel(models.Model):

    class Meta:
        abstract = True
    
    def __str__(self):
        return f'<{self.__class__.__name__} : {self.pk}>'


class TimeStampMixin(BookStoreBaseModel):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_at']