from django.db import models


class Kansuu(models.Model):
    program_name = models.CharField(max_length=200)
    kansu_name = models.CharField(max_length=200)
    setsumei = models.CharField(max_length=200)

    def __str__(self):
        # return self.program_name
        return self.kansu_name


class FuncName(models.Model):
    func_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
