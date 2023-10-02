from django.db import models
from django.contrib.auth.models import User

class VideoCompletion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)


class UserVideos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_1 = models.BooleanField(default=False)
    video_2 = models.BooleanField(default=False)
    video_3 = models.BooleanField(default=False)
    video_4 = models.BooleanField(default=False)
    video_5 = models.BooleanField(default=False)
    video_6 = models.BooleanField(default=False)
    video_7 = models.BooleanField(default=False)
    video_8 = models.BooleanField(default=False)
    video_9 = models.BooleanField(default=False)
    video_10 = models.BooleanField(default=False)

    # Add a field for total calories burned
    total_calories_burned = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Videos"

    # Method to update the total calories burned
    def update_calories_burned(self):
        # Define calorie values for each video (you can adjust these values)
        calorie_values = {
            'video_1': 10,
            'video_2': 15,
            'video_3': 20,
            'video_4': 25,
            'video_5': 30,
            'video_6': 35,
            'video_7': 40,
            'video_8': 45,
            'video_9': 50,
            'video_10': 55,
        }

        # Calculate the total calories burned based on completed videos
        total_calories = sum(calorie_values[key] for key in calorie_values if getattr(self, key))

        # Update the total calories burned field
        self.total_calories_burned = total_calories

    # Override the save method to handle the case when no videos are completed
    def save(self, *args, **kwargs):
        # Calculate the total calories burned
        self.update_calories_burned()
        super(UserVideos, self).save(*args, **kwargs)


class Visit(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()  # Height is required and cannot be null
    weight = models.FloatField()  # Weight is required and cannot be null
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    sport_choice = models.CharField(
        max_length=50,
        choices=[('basketball', 'Basketball'), ('swimming', 'Swimming'), ('Taekwondo', 'Taekwondo')],
        blank=True,
        null=True
    )
