from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        user_objects = {}
        for user_data in test_users:
            # Debug: Log user creation
            print(f"Creating user: {user_data['username']}, email: {user_data['email']}")
            user = User.objects.create(username=user_data['username'], email=user_data['email'], password=user_data['password'])
            user_objects[user_data['username']] = user

        # Populate teams
        for team_data in test_teams:
            team = Team.objects.create(name=team_data['name'])
            team.members.add(*[user_objects[username] for username in team_data['members']])

        # Populate activities
        for activity_data in test_activities:
            Activity.objects.create(user=user_objects[activity_data['username']], activity_type=activity_data['activity_type'], duration=activity_data['duration'])

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            Leaderboard.objects.create(user=user_objects[leaderboard_data['username']], score=leaderboard_data['score'])

        # Populate workouts
        for workout_data in test_workouts:
            Workout.objects.create(name=workout_data['name'], description=workout_data['description'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
