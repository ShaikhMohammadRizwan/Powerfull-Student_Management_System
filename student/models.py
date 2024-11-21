from django.db import models
from django.utils.text import slugify  # Import slugify

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_contact = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=254)  # Updated max_length

    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_contact = models.CharField(max_length=15)
    mother_email = models.EmailField(max_length=254)  # Updated max_length

    parent_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self) -> str:
        return f'{self.father_name} {self.mother_name}'
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.IntegerField()  # Removed max_length
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ]
    )
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)  # Increased length to accommodate longer religions
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=20)  # Changed to CharField for better formatting (e.g., +91)
    admission_number = models.IntegerField()  # Removed max_length
    section = models.CharField(max_length=20)
    student_image = models.ImageField(upload_to='student/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name} {self.last_name} {self.student_id}')
        super(Student, self).save(*args, **kwargs)  # Ensure this is called after slug creation

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.student_id}'
