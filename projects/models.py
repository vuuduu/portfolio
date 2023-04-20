# We'll be using ORM, Object Relational Mapper (Django built in database management system)
# ORM it's just python Classes (collumn) and Instances of those classes (rows)

from django.db import models

# title: a short string field to hold the name of your project.
# description: a larger string field to hold a longer piece of text.
# technology: a string field, but its contents will be limited to a select number of choices.
# image: an image field that holds the file path where the image is stored.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

