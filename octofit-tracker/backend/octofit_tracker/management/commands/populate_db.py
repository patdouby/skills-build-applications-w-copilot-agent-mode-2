from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name)
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc.name)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc.name)

        # Activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2025-12-01')
        Activity.objects.create(user=spiderman, type='Cycling', duration=45, date='2025-12-02')
        Activity.objects.create(user=batman, type='Swimming', duration=60, date='2025-12-03')
        Activity.objects.create(user=superman, type='Yoga', duration=20, date='2025-12-04')

        # Leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=spiderman, points=80)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=95)

        # Workouts
        Workout.objects.create(name='Full Body Blast', description='Intense full body workout', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
