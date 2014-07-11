from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    first_name = models.CharField(verbose_name=_("First name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=255)
    patronymic = models.CharField(verbose_name=_("Patronymic"), max_length=255, blank=True)
    birth_date = models.DateField()


CONTACT_INFO_TYPES = (('phone', _("Phone")),
                      ('email', _("email")),
                      ('instant_messenger', _("Instant messenger")),
                      ('other', _("Other")))


class ContactInfo(models.Model):
    person = models.ForeignKey(Person, related_name='contact_info')
    type = models.CharField(choices=CONTACT_INFO_TYPES, max_length=255)
    value = models.CharField(max_length=255)
    is_preferred = models.BooleanField(default=False, blank=True)


class IdentificationDocument(models.Model):
    person = models.ForeignKey(Person, related_name='identification_ducuments')
    document_type = models.CharField(max_length=255)
    document_date = models.DateField()
    additional_info = models.TextField()


class Relationship(models.Model):
    who = models.ForeignKey(Person, related_name="relationship_from")
    to = models.ForeignKey(Person, related_name="relationship_to")
    relationship = models.CharField(max_length=255)


class FormerNames(models.Model):
    first_name = models.CharField(verbose_name=_("First name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=255)
    patronymic = models.CharField(verbose_name=_("Patronymic"), max_length=255, blank=True)
    reason = models.TextField()
    start_date = models.DateField()


class PersonCitizenShip(models.Model):
    person = models.ForeignKey(Person, related_name='citizenships')
    country = models.CharField(max_length=255)
    start_date = models.DateField()
    reason = models.CharField(max_length=255)


EDUCATION_TYPES = (('school', _("School")),
                   ('colledge', _("Colledge")),
                   ('university', _("university")),
                   ('courses', _("Courses")),
                   ('other', _("Other")))


class Education(models.Model):
    person = models.ForeignKey(Person, related_name="education")
    place = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.CharField(choices=EDUCATION_TYPES, max_length=255)
    completed = models.BooleanField(blank=True)
    certificate = models.BooleanField(blank=True)


class EductionDegree(models.Model):
    education = models.ForeignKey(Education, related_name='degree')
    degree = models.CharField(max_length=255)
    degree_date = models.DateField()
    thesis = models.TextField()
    curator = models.ForeignKey(Person)


PROFESSIONAL_EPRERICENCE_TYPES = (
    ('commercial', _("Commercial")),
    ('governmental', _("Governmental")),
    ('non-governmetal', _("Non-Governmental")),
    ('military', _("Military")),
)


class ProfessionalExperience(models.Model):
    person = models.ForeignKey(Person, related_name='work')
    type = models.CharField(choices=PROFESSIONAL_EPRERICENCE_TYPES, max_length=255)
    place = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)


class ProfessionalDegree(models.Model):
    professional_exprerience = models.ForeignKey(ProfessionalExperience, related_name='professional_degree')
    title = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    degree_date = models.DateField()


class Awards(models.Model):
    person = models.ForeignKey(Person, related_name='awards')
    award_date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class ProfessionalSkills(models.Model):
    person = models.ForeignKey(Person, related_name='skills')
    skill = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    notes = models.TextField(blank=True)


class CriminalRecords(models.Model):
    person = models.ForeignKey(Person, related_name='criminal_records')
    record_date = models.DateField()
    description = models.TextField()


class Places(models.Model):
    place_content_type = models.ForeignKey(ContentType, related_name='place_type', verbose_name=_('object type'))
    place_object_id = models.PositiveIntegerField(verbose_name=_('object id'))
    place_object = generic.GenericForeignKey('place_content_type', 'place_object_id')
    country = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    description = models.TextField(blank=True)
    current = models.BooleanField(blank=True, default=False)


class Events(models.Model):
    event_content_type = models.ForeignKey(ContentType, related_name='event_type', verbose_name=_('From object type'))
    event_object_id = models.PositiveIntegerField(verbose_name=_('object id'))
    event_object = generic.GenericForeignKey('event_content_type', 'event_object_id')

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    event_date = models.DateTimeField()


class Files(models.Model):
    object_content_type = models.ForeignKey(ContentType, related_name='', verbose_name=_('object type'))
    object_id = models.PositiveIntegerField(verbose_name=_('From object id'))
    related_object = generic.GenericForeignKey('object_content_type', 'object_id')

    file = models.FileField(upload_to='files')
    description = models.TextField()
    upload_date = models.DateField()







