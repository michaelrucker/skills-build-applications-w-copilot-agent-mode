from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Clear existing data
            Activity.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()
            Leaderboard.objects.all().delete()

            # Create teams
            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            # Create users

            users = []
            users.append(User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True))
            users.append(User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True))
            users.append(User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True))
            users.append(User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True))

            # Create activities
            Activity.objects.create(user=users[0], type='Run', duration=30, date='2024-01-01')
            Activity.objects.create(user=users[1], type='Swim', duration=45, date='2024-01-02')
            Activity.objects.create(user=users[2], type='Bike', duration=60, date='2024-01-03')
            Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2024-01-04')

            # Create workouts
            workout1 = Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
            workout2 = Workout.objects.create(name='Agility Training', description='Agility workout for heroes')
            workout1.suggested_for.add(marvel, dc)
            workout2.suggested_for.add(marvel)

            # Create leaderboards
            Leaderboard.objects.create(team=marvel, points=200)
            Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
