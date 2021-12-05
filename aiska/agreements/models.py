from django.db import models


# Таблица наименование организации/ФОИВ
class Foiv(models.Model):
    title = models.CharField(max_length=250)
    short = models.CharField(max_length=20)

    class Meta:
        verbose_name = u"ФОИВ"
        verbose_name_plural = u"ФОИВы"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Таблица Подразделения
class Department(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name = u"Подразделение"
        verbose_name_plural = u"Подразделения"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Таблица Соглашения
class Agreements(models.Model):
    foiv_id = models.ForeignKey(Foiv, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=250)
    number = models.CharField(max_length=20)
    reg_date = models.DateField()
    inv_number = models.CharField(max_length=20)
    subject = models.TextField()
    departments = models.ManyToManyField(
        Department,
        verbose_name=u"Уполномоченные подразделения",
    )
    note = models.TextField()
    file = models.FileField(upload_to='agreements/')

    @property
    def display_dept(self):
        return ", ".join([departments.title for departments in self.departments.all()])

    class Meta:
        verbose_name = u"Соглашение"
        verbose_name_plural = u"Соглашения"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Таблица Дополнительные соглашения
class Additional(models.Model):
    agr_id = models.ForeignKey(Agreements, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=250)
    number = models.CharField(max_length=20)
    reg_date = models.DateField()
    inv_number = models.CharField(max_length=20)
    subject = models.TextField()
    departments = models.ManyToManyField(
        Department,
        verbose_name=u"Уполномоченные подразделения",
    )
    note = models.TextField()
    file = models.FileField(upload_to='additional/')

    @property
    def display_dept(self):
        return ", ".join([departments.title for departments in self.departments.all()])

    class Meta:
        verbose_name = u"Доп. соглашение"
        verbose_name_plural = u"Доп. соглашения"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Таблица Типы протоколов
class Type(models.Model):
    type_protocol = models.CharField(max_length=50)

    class Meta:
        verbose_name = u"Тип протокол"
        verbose_name_plural = u"Типы протоколов"

    def __unicode__(self):
        return self.type_protocol

    def __str__(self):
        return self.type_protocol


# Таблица Протоколы
class Protocol(models.Model):
    agr_id = models.ForeignKey(Agreements, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=250)
    number = models.CharField(max_length=20)
    reg_date = models.DateField()
    inv_number = models.CharField(max_length=20)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    from_mvd = models.TextField()  # Перечень сведений от МВД
    for_mvd = models.TextField()  # Перечень сведений для МВД
    note = models.TextField()
    file = models.FileField(upload_to='protocol/')

    class Meta:
        verbose_name = u"Протокол"
        verbose_name_plural = u"Протоколы"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
