from django.contrib.postgres.fields import ArrayField
from django.db import models
from pilot.enumerations import *
from pilot.fields import FrequencyArrayField, URIArrayField

import re
import xml.etree.ElementTree as et

#S100
#abstract element types
class AbstractInformationType(models.Model):
    class Meta:
        abstract = True

#from GML
#abstract attributes
class AssociationAttributeGroup(models.Model):
    SHOW_CHOICES = [
        ("new", "New"),
        ("replace", "Replace"),
        ("embed", "Embed"),
        ("other", "Other"),
        ("none", "None")
    ]

    ACTUATE_CHOICES = [
        ("onLoad", "On Load"),
        ("onRequest", "On Request"),
        ("other", "Other"),
        ("none", "None")
    ]

    namespace = "xlink:"
    type = "simple"
    href = models.TextField(blank=True)
    role = models.TextField(blank=True)
    arcrole = models.TextField(blank=True)
    title = models.TextField(blank=True)
    show = models.CharField(max_length=100, blank=True, choices = SHOW_CHOICES)
    actuate = models.CharField(max_length=100, blank=True, choices = ACTUATE_CHOICES)

    class Meta:
        abstract = True

#S127 attribute models
#Abstract base classes
class ElementBase(models.Model):
    capitalize_element_name = False
    element_name = None
    namespace = ""
    
    class Meta:
        abstract = True 

    def element(self):
        fields = self.__class__._meta.get_fields()

        main_element_name = None

        if self.element_name:
            main_element_name = self.element_name
        elif self.capitalize_element_name:
            main_element_name = self.__class__.__name__
        else:
            main_element_name = re.sub("^(.)", lambda m: m.groups()[0].lower(), self.__class__.__name__)

        main_element = et.Element("%s%s" % (self.namespace, main_element_name))

        if hasattr(self, "gml_id"):
            main_element.attrib["gml:id"] = self.gml_id

        for field in fields:
            #skip gml_id since it's an attribute
            if field.name == "gml_id":
                continue

            #fields with a "field" attribute are many to many relationships that originate in a different model
            if hasattr(field, "field"):
                continue

            #check for a manually set element name for the field, otherwise change delimited names to camel case
            element_name = getattr(field, "element_name",
                re.sub("_([a-z])", lambda m: m.groups()[0].capitalize(), field.name)) 

            fc = field.__class__

            if fc == models.BooleanField:
                element = et.SubElement(main_element, element_name)
                element.text = "1" if getattr(self, field.name) else "0"
            elif (fc == models.CharField or fc == models.TextField) and getattr(self, field.name):
                element = et.SubElement(main_element, element_name)
                element.text = getattr(self, field.name)
            elif fc == models.ForeignKey and getattr(self, field.name):
                element = main_element.append(getattr(self, field.name).element())
            elif fc == models.ManyToManyField and getattr(self, field.name).exists():
                for i in getattr(self, field.name).all():
                    if getattr(field, "use_id", False):
                        element = et.SubElement(main_element, element_name)
                        element.attrib["xlink:href"] = i.gml_id
                    else:
                        main_element.append(i.element())
            elif fc == ArrayField and getattr(self, field.name):
                for i in getattr(self, field.name):
                    element = et.SubElement(main_element, element_name)
                    element.text = str(i)
            elif fc == FrequencyArrayField and getattr(self, field.name):
                for i in getattr(self, field.name):
                    element = et.SubElement(main_element, element_name)
                    element.text = i.to_eng_string().replace(".", "")
            elif fc == URIArrayField and getattr(self, field.name):
                for i in getattr(self, field.name):
                    element = et.SubElement(main_element, element_name)
                    element.attrib["xlink:href"] = i

        return main_element

class BaseRadiocommunications(ElementBase):
    category_of_comm_pref = models.CharField(max_length=20, choices=CATEGORY_OF_COMM_PREF)
    communication_channel = ArrayField(models.TextField(blank=True), blank=True)
    contact_instructions = models.TextField(blank=True)
    frequency_pair = models.ManyToManyField("FrequencyPair", blank=True)
    time_intervals_by_day_of_week = models.ManyToManyField("TimeIntervalsByDayOfWeek")

    element_name = "radiocommunications"

    class Meta:
        abstract = True

class DateRange(ElementBase):
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True

    def element(self):
        main_element = et.Element(self.element_name)

        if self.date_start:
            outer_date_start = et.SubElement(main_element, "dateStart")
            inner_date_start = et.SubElement(outer_date_start, "date")
            inner_date_start.text = self.date_start.strftime("%Y-%m-%d")
        if self.date_end:
            outer_date_end = et.SubElement(main_element, "dateEnd")
            inner_date_end = et.SubElement(outer_date_end, "date")
            inner_date_end.text = self.date_end.strftime("%Y-%m-%d")

        return main_element

#regular models
class ContactAddress(ElementBase):
    delivery_point = ArrayField(models.TextField(blank=True), blank=True)
    city_name = models.TextField(blank=True)
    administrative_division = models.TextField(blank=True)
    country_name = models.TextField(blank=True)
    postal_code = models.TextField(blank=True)

class ContactDetailsRadiocommunications(BaseRadiocommunications):
    pass

class FeatureName(ElementBase):
    display_name = models.BooleanField(default=True)
    language = models.CharField(max_length = 3, default="eng")
    name = models.TextField()

class FixedDateRange(DateRange):
    pass

class FrequencyPair(ElementBase):
    frequency_shore_station_transmits = FrequencyArrayField(models.DecimalField(
        decimal_places=1, max_digits=10, blank=True, null=True), blank=True)
    frequency_shore_station_receives = FrequencyArrayField(models.DecimalField(
        decimal_places=1, max_digits=10, blank=True, null=True), blank=True)
    contact_instructions = models.TextField(blank=True)

class Information(ElementBase):
    file_locator = models.TextField(blank=True)
    file_reference = models.TextField(blank=True)
    headline = models.TextField(blank=True)
    language = models.CharField(max_length=3, default="eng")
    text = models.TextField(blank=True)

class NoticeTime(ElementBase):
    notice_time_hours = ArrayField(models.FloatField(blank=True, null=True), blank=True)
    notice_time_text = models.TextField(blank=True)
    operation = models.CharField(max_length=20, blank=True, choices=OPERATION)

class OnlineResource(ElementBase):
    linkage = models.TextField()
    protocol = models.CharField(max_length=20, blank=True)
    application_profile = models.TextField(blank=True)
    name_of_resource = models.TextField(blank=True)
    online_resource_description = models.TextField(blank=True)
    online_function = models.CharField(max_length=100, choices=ONLINE_FUNCTION, blank=True)
    protocol_request = models.TextField(blank=True)

class PeriodicDateRange(DateRange):
    pass

class SourceIndication(ElementBase):
    category_of_authority = models.CharField(max_length=100, choices=CATEGORY_OF_AUTHORITY, blank=True)
    country_name = models.CharField(blank=True, max_length=100)
    feature_name = models.ManyToManyField("FeatureName", blank=True) 
    reported_date = models.DateField(blank=True)
    source = models.TextField(blank=True)
    source_type = models.CharField(max_length=100, choices=SOURCE_TYPE, blank=True)

class Radiocommunications(BaseRadiocommunications):
    category_of_maritime_broadcast = ArrayField(models.CharField(max_length=30, choices=
        CATEGORY_OF_MARITIME_BROADCAST), blank=True) #use checkboxes for types
    category_of_radio_method = ArrayField(models.CharField(max_length=30, choices=
        CATEGORY_OF_RADIO_METHOD), blank=True) #use checkboxes for types
    signal_frequency = FrequencyArrayField(models.DecimalField(
        decimal_places=1, max_digits=10, blank=True, null=True), blank=True)
    transmission_content = models.TextField(blank=True)

class ScheduleByDayOfWeek(ElementBase):
    category_of_schedule = models.CharField(max_length=20, choices=CATEGORY_OF_SCHEDULE, blank=True)
    time_intervals_by_day_of_week = models.ManyToManyField("TimeIntervalsByDayOfWeek")

#FIXME Needs custom form field to limit to two days if range 
class TimeIntervalsByDayOfWeek(ElementBase):
    day_of_week = ArrayField(models.PositiveIntegerField())
    day_of_week_is_range = models.BooleanField(default=False)
    time_of_day_start = models.TimeField(blank=True, null=True)
    time_of_day_end = models.TimeField(blank=True, null=True)

    element_name = "timeIntervalsByDayOfWeek"

class Telecommunications(ElementBase):
    category_of_comm_pref = models.CharField(max_length=20, choices=CATEGORY_OF_COMM_PREF)
    contact_instructions = models.TextField(blank=True)
    telecom_carrier = models.TextField(blank=True)
    schedule_by_day_of_week = models.ForeignKey("ScheduleByDayOfWeek", blank=True, null=True)

class TextContent(ElementBase):
    category_of_text = models.CharField(max_length=100, choices=CATEGORY_OF_TEXT, blank=True)
    information = models.ManyToManyField("Information", blank=True)
    online_resource = models.ForeignKey("OnlineResource", blank=True, null=True)
    source_indication = models.ForeignKey("SourceIndication", blank=True, null=True)

#S127
#abstract element types
class S127ElementBase(ElementBase):
    namespace = "S127:" 
    capitalize_element_name = True

    class Meta:
        abstract = True

class InformationType(AbstractInformationType):
    gml_id = models.TextField(unique=True)
    fixed_date_range = models.ForeignKey("FixedDateRange", blank=True, null=True)
    periodic_date_range = models.ManyToManyField("PeriodicDateRange", blank=True) 
    feature_name = models.ManyToManyField("FeatureName", blank=True)
    source_indication = models.ManyToManyField("SourceIndication", blank=True)
    provides_information = URIArrayField(models.TextField(blank=True), blank=True, null=True)

    def __str__(self):
        return self.gml_id

    class Meta:
        abstract = True

#complex type elements
class Authority(InformationType, S127ElementBase):
    category_of_authority = models.CharField(max_length=100, choices=CATEGORY_OF_AUTHORITY, blank=True, null=True)
    textContent = models.ForeignKey("TextContent", blank=True, null=True)
    theContactDetails = models.ManyToManyField("ContactDetails", blank=True)
    theServiceHours = models.ManyToManyField("ServiceHours", blank=True)
    theShipReport = models.ManyToManyField("ShipReport", blank=True)

#the way this is implied to work in the xsd file doesn't go along with how Information is actually handled
#there's also no example in the sample data
    theInformation = models.ManyToManyField("Information", blank=True)

    setattr(theContactDetails, "use_id", True)
    setattr(theShipReport, "use_id", True)

class ContactDetails(InformationType, S127ElementBase):
    call_name = models.TextField(blank=True)
    call_sign = models.TextField(blank=True)
    category_of_comm_pref = models.CharField(max_length=20, choices=CATEGORY_OF_COMM_PREF)
    communication_channel = models.TextField(blank=True)
    contact_address = models.ManyToManyField("ContactAddress", blank=True)
    contact_instructions = models.TextField(blank=True)
    frequency_pair = models.ManyToManyField("FrequencyPair", blank=True)
    information = models.ManyToManyField("Information", blank=True)
    language = models.CharField(max_length=3, blank=True)
    mmsi_code = models.CharField(max_length=9, blank=True) #use regexfield in form, \d{9}
    online_resource = models.ManyToManyField("OnlineResource", blank=True)
    telecommunications = models.ManyToManyField("Telecommunications", blank=True)
    radiocommunications = models.ManyToManyField("ContactDetailsRadiocommunications", blank=True)
    
    #FIXME
#   theAuthority #grab from authority_set

    setattr(mmsi_code, "element_name", "mMSICode")

class ServiceHours(InformationType, S127ElementBase):
    schedule_by_day_of_week = models.ManyToManyField("ScheduleByDayOfWeek")
    information = models.ManyToManyField("Information", blank=True)
    partial_working_day = URIArrayField(models.TextField(blank=True), blank=True, null=True) 

    #FIXME
#   theAuthority_srvHrs #grab from authority_set

class ShipReport(InformationType, S127ElementBase):
    category_of_ship_report = models.CharField(max_length=100, choices=CATEGORY_OF_SHIP_REPORT)
    imo_format_for_report = models.BooleanField(default=False)
    report_to = URIArrayField(models.TextField(blank=True), blank=True, null=True)
    notice_time = models.ManyToManyField("NoticeTime")
    text_content = models.ForeignKey("TextContent", blank=True, null=True)
    must_by_filed_by = URIArrayField(models.TextField(blank=True), blank=True, null=True)
