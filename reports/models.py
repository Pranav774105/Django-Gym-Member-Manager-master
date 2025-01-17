from django.db import models
from members.models import Member
from django.forms import ModelForm
import datetime
import calendar
from datetime import timezone

# Generate year choices dynamically
YEAR_CHOICES = []
current_year = datetime.datetime.now(timezone.utc).year
for year in range(2016, current_year + 5):
    YEAR_CHOICES.append((year, year))

# Define batch options
BATCH = (
    ('morning', 'Morning'),
    ('evening', 'Evening'),
    ('', 'All')
)

# Define month choices
MONTHS_CHOICES = tuple(zip(range(1, 13), (calendar.month_name[i] for i in range(1, 13))))

# Define models
class GenerateReports(models.Model):
    month = models.IntegerField(choices=MONTHS_CHOICES, default=datetime.datetime.now().month, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
    batch = models.CharField(
        max_length=30,
        choices=BATCH,
        default=BATCH[2][0],
        blank=True
    )

# Define forms
class GenerateReportForm(ModelForm):
    class Meta:
        model = GenerateReports
        fields = '__all__'
