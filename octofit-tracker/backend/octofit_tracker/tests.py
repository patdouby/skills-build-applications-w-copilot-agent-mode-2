from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team.name)
        self.assertEqual(user.name, 'Iron Man')
        self.assertEqual(user.team, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='DC', description='DC Superheroes')
        self.assertEqual(team.name, 'DC')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=team.name)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-12-01')
        self.assertEqual(activity.type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team.name)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Full Body Blast', description='Intense full body workout', suggested_for='Marvel')
        self.assertEqual(workout.name, 'Full Body Blast')
